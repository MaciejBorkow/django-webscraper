from unittest.mock import patch
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from django.test import TestCase

from webscraper.utils.scraper import (find_text, find_images_src, standardize_img_url, get_url_content,
                                      URLGetStatusNot200Error, URLContentNotTextTypeError)
from webscraper.tests.fixtures import ExamplePage, text_loremipsum


class TextFinderTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self) -> None:
        pass

    def test_find_text_in_html(self):
        soup = BeautifulSoup(ExamplePage.raw_text, 'html.parser')
        url_text = find_text(soup)
        self.assertEqual(url_text, ExamplePage.text)

    def test_find_text_in_plain_text(self):
        soup = BeautifulSoup(text_loremipsum, 'html.parser')
        url_text = find_text(soup)
        self.assertEqual(url_text, text_loremipsum)

    def test_find_text_empty(self):
        soup = BeautifulSoup("", 'html.parser')
        url_text = find_text(soup)
        self.assertEqual(url_text, "")


class ImageSrcFinderTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_find_images_src(self):
        soup = BeautifulSoup(ExamplePage.raw_text, 'html.parser')
        src_set = find_images_src(soup, urlparse(ExamplePage.url))
        self.assertSetEqual(src_set, ExamplePage.img_src_normalized)

    def test_image_url_serialization(self):
        img_src = {standardize_img_url(url, urlparse(ExamplePage.url)) for url in ExamplePage.img_src_raw}
        self.assertSetEqual(img_src, ExamplePage.img_src_normalized)

class RequestURLTest(TestCase):
    def setUp(self) -> None:
        request_mock = patch('webscraper.utils.scraper.requests.get').start()
        self.request_mock_instance = request_mock.return_value

    def tearDown(self) -> None:
        pass

    def test_request_with_status_code_200(self):
        self.request_mock_instance.status_code = 200
        self.request_mock_instance.encoding = '123'
        self.request_mock_instance.headers.get.return_value = 'text/html'
        content = 'my content 123!'
        self.request_mock_instance.content = content
        self.assertEqual(get_url_content('www.abc.df'), content)


    # def test_request_with_status_code_not_200(self):
    #     self.request_mock_instance.status_code = 404
    #     self.assertRaises(URLGetStatusNot200Error, get_url_content(ExamplePage.url))


    def test_request_header_content_type_validation(self):
        pass

    def test_request_content_extraction(self):
        pass

class ScrapSinglePageTest(TestCase):
    pass

class ScrapAndDownloadPageTest(TestCase):
    pass


