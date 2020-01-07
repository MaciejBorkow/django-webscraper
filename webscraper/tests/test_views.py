import json
from unittest.mock import Mock, patch

from django.test import TestCase
from django.urls import reverse

from webscraper.tasks import CeleryStatuses
from webscraper.models import ScrapedUrl


class TaskStatusUpdateTest(TestCase):
    def setUp(self):
        celery_mock = patch('webscraper.utils.queue.current_app.AsyncResult').start()
        self.celery_mock_instance = celery_mock.return_value
        self.celery_mock_instance.status = CeleryStatuses.PENDING

    def tearDown(self) -> None:
        patch.stopall()

    def test_url_list_view(self):
        ScrapedUrl.objects.create(status=CeleryStatuses.SUCCESS, url='www.abc.pl')
        response = self.client.get(reverse('webscraper:index'))
        self.assertEqual(response.status_code, 200)


    def test_specific_url_view(self):
        su = ScrapedUrl.objects.create(status=CeleryStatuses.SUCCESS, url='www.abc.pl')
        response = self.client.get(f'/webscraper/url/{su.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_image_download(self):
        pass

    def test_text_download(self):
        pass

    def test_url_scrap_post(self):
        request_mock = patch('webscraper.utils.scraper.requests.get').start()
        request_mock_instance = request_mock.return_value
        request_mock_instance.status_code = 200
        download_page_mock = patch('webscraper.tasks.download_all_pages_wrap.delay').start()
        dp_mock_instance = download_page_mock.return_value
        dp_mock_instance.id = '1234'
        dp_mock_instance.status = CeleryStatuses.STARTED

        json_data = {
        "url": "https://pl.wikipedia.org/wiki/Volkswagen_Golf",
        "image": True,
        "text": True
    }
        response = self.client.post('/webscraper/url/', json.dumps(json_data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
