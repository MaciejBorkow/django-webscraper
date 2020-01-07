from celery import current_app
from django.core.exceptions import ObjectDoesNotExist

from webscraper.models import ScrapedUrl
from webscraper.tasks import CeleryStatuses


def update_tasks_status_in_db():
    """Update all not successful Celery queue tasks statuses in ScrapedURL db table"""
    scraped_urls_to_update = ScrapedUrl.objects.exclude(status=CeleryStatuses.SUCCESS)
    for scraped_url in scraped_urls_to_update:
        scraped_url.status = current_app.AsyncResult(scraped_url.queue).status
        scraped_url.save()


def update_one_task_status_in_db(pk):
    """Update one Celery queue task status in ScrapedURL table as 'status' attribute based on pk."""
    try:
        scraped_url = ScrapedUrl.objects.exclude(status=CeleryStatuses.SUCCESS).get(pk=pk)
    except ObjectDoesNotExist:
        return
    scraped_url.status = current_app.AsyncResult(scraped_url.queue).status
    scraped_url.save()
