import os
from unittest.mock import patch

from django.test import TestCase
from django.conf import settings

from webscraper.models import ScrapedUrl


class ScrapedURLModelTest(TestCase):
    def setUp(self):
        self.url = 'www.example.pl'
        self.scraped_url = ScrapedUrl.objects.create(url=self.url)
        a = patch('webscraper.models.os.makedirs').start()

    def test_path(self):
        path = os.path.join(settings.WEBSCRAPER_ROOT_DIR, str(self.scraped_url.id))
        self.assertEquals(path, self.scraped_url.path())
