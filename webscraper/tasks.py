from celery import shared_task
from webscraper.utils.scraper import download_all_pages


class CeleryStatuses:
    PENDING = 'PENDING'
    STARTED = 'STARTED'
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'
    RETRY = 'RETRY'
    REVOKED = 'REVOKED'


@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def download_all_pages_wrap(url, output_path,  scrap_img: bool = True,
                            scrap_text: bool = True, scrap_recursive: bool = False):
    download_all_pages(url=url, output_path=output_path, scrap_img=scrap_img,
                       scrap_text=scrap_text, scrap_recursive=scrap_recursive)
