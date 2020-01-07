from unittest.mock import patch

from django.test import TestCase

from webscraper.models import ScrapedUrl
from webscraper.utils.queue import update_tasks_status_in_db, update_one_task_status_in_db
from webscraper.tasks import CeleryStatuses


class TaskStatusUpdateTest(TestCase):
    def setUp(self):
        celery_mock = patch('webscraper.utils.queue.current_app.AsyncResult').start()
        self.celery_mock_instance = celery_mock.return_value

    def tearDown(self) -> None:
        patch.stopall()

    def test_update_all_queue_tasks_statuses_in_db_when_all_success(self):
        self.celery_mock_instance.status = CeleryStatuses.PENDING
        statuses_in = 3*[CeleryStatuses.SUCCESS]
        statuses_out = 3*[CeleryStatuses.SUCCESS]
        [ScrapedUrl.objects.create(status=s) for s in statuses_in]
        update_tasks_status_in_db()
        statuses_out_ok = list(ScrapedUrl.objects.all().values_list('status', flat=True))
        self.assertListEqual(statuses_out, statuses_out_ok)

    def test_update_all_queue_tasks_statuses_in_db_when_mixed(self):
        self.celery_mock_instance.status = CeleryStatuses.PENDING
        statuses_in = [CeleryStatuses.FAILURE, CeleryStatuses.PENDING, CeleryStatuses.SUCCESS]
        statuses_out = [CeleryStatuses.PENDING, CeleryStatuses.PENDING, CeleryStatuses.SUCCESS]
        [ScrapedUrl.objects.create(status=s) for s in statuses_in]
        update_tasks_status_in_db()
        statuses_out_ok = list(ScrapedUrl.objects.all().values_list('status', flat=True))
        self.assertListEqual(statuses_out, statuses_out_ok)

    def test_update_all_queue_tasks_statuses_in_db_when_nodata(self):
        self.celery_mock_instance.status = CeleryStatuses.PENDING
        statuses_in = []
        statuses_out = []
        [ScrapedUrl.objects.create(status=s) for s in statuses_in]
        update_tasks_status_in_db()
        statuses_out_ok = list(ScrapedUrl.objects.all().values_list('status', flat=True))
        self.assertListEqual(statuses_out, statuses_out_ok)

    def test_Update_one_qieie_task_status_in_db_when_not_success(self):
        self.celery_mock_instance.status = CeleryStatuses.PENDING
        statuses_in = [CeleryStatuses.FAILURE, CeleryStatuses.SUCCESS, CeleryStatuses.STARTED]
        statuses_out = [CeleryStatuses.PENDING, CeleryStatuses.SUCCESS, CeleryStatuses.STARTED]
        obj = [ScrapedUrl.objects.create(status=s) for s in statuses_in]
        update_one_task_status_in_db(obj[0].pk)
        statuses_out_ok = list(ScrapedUrl.objects.all().values_list('status', flat=True))
        self.assertListEqual(statuses_out, statuses_out_ok)

    def test_Update_one_qieie_task_status_in_db_when_success(self):
        self.celery_mock_instance.status = CeleryStatuses.PENDING
        statuses_in = [CeleryStatuses.SUCCESS, CeleryStatuses.STARTED, CeleryStatuses.FAILURE]
        statuses_out = [CeleryStatuses.SUCCESS, CeleryStatuses.STARTED, CeleryStatuses.FAILURE]
        obj = [ScrapedUrl.objects.create(status=s) for s in statuses_in]
        update_one_task_status_in_db(obj[0].pk)
        statuses_out_ok = list(ScrapedUrl.objects.all().values_list('status', flat=True))
        self.assertListEqual(statuses_out, statuses_out_ok)

    def test_Update_one_qieie_task_status_in_db_when_no_data(self):
        self.celery_mock_instance.status = CeleryStatuses.PENDING
        statuses_in = []
        statuses_out = []
        obj = [ScrapedUrl.objects.create(status=s) for s in statuses_in]
        update_one_task_status_in_db(123)
        statuses_out_ok = list(ScrapedUrl.objects.all().values_list('status', flat=True))
        self.assertListEqual(statuses_out, statuses_out_ok)
