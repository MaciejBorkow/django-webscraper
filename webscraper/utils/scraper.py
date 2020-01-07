from urllib.parse import urlparse, urlunparse
from typing import Set, Tuple
import shutil
import os

from bs4 import BeautifulSoup
import requests


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class URLGetStatusNot200Error(Error):
    pass


class URLContentNotTextTypeError(Error):
    pass


def find_images_src(html_soup: BeautifulSoup, url_ancestor_parse) -> Set[str]:
    """Find all <img> tags, extract images source links, add schema and domain to the links if needed"""
    imgs_src_set = {standardize_img_url(img['src'], url_ancestor_parse) for img in html_soup.find_all('img', src=True)}

    return imgs_src_set


def download_image(image_url, image_file_name, image_directory=''):
    """Download an image from image_url and save to image_directory; evaluate image type base on 'cotent-type' header"""
    try:
        with requests.get(image_url, stream=True) as r:
            r_content_type = r.headers.get('content-type', '')
            image_file_path = os.path.join(image_directory, f'{image_file_name}.{r_content_type.split(r"/")[1]}')
            if 'image' in r_content_type and r.status_code == 200:
                with open(image_file_path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
    except Exception as e:
        print("image download exception: ", e)


def download_images(images_src_set: Set[str], image_directory):
    """Download images from links set; handle tmp directory creation, zip to one file 'zip.img' at image_directory """
    tmp_image_directory = os.path.join(image_directory, 'img')
    os.mkdir(tmp_image_directory)
    for ind, image_url in enumerate(images_src_set):
        download_image(image_url, str(ind), tmp_image_directory)
    shutil.make_archive(tmp_image_directory, 'zip', tmp_image_directory)
    shutil.rmtree(tmp_image_directory)


def find_text(html_soup: BeautifulSoup) -> str:
    """Find text in html soup."""
    for tag in html_soup.find_all(['script', 'style']):
        tag.extract()
    text = html_soup.text

    return text


def save_text(text, text_directory):
    """Save given text at given text)directory with text.txt name."""
    with open(os.path.join(text_directory, 'text.txt'), 'w') as f:
        f.write(text)


def find_hrefs(html_soup: BeautifulSoup, url_ancestor_parse) -> Set[str]:
    """Find all href in html_soup(subpages) at the same domain as url_ancestor_parse."""
    urls_set = set()
    for href in (h['href'] for h in html_soup.find_all('a', href=True) if isinstance(h['href'], str)):
        href_standardize = standardize_same_domain_url(href, url_ancestor_parse)
        if href_standardize:
            urls_set |= {href_standardize}

    return urls_set


def standardize_img_url(input_url, url_ancestor_parse):
    """Standardize input_url - add schema, domain and remove variables based on url_ancestor_parse"""
    input_url_parse = urlparse(input_url)
    if not input_url_parse.netloc and not input_url_parse.scheme and input_url_parse.path:
        return urlunparse(input_url_parse._replace(
                scheme=url_ancestor_parse.scheme, netloc=url_ancestor_parse.netloc, params='', query='', fragment=''
            ))
    elif input_url_parse.netloc and not input_url_parse.scheme:
        return urlunparse(input_url_parse._replace(scheme=url_ancestor_parse.scheme, params='', query='', fragment=''))


def standardize_same_domain_url(input_url, url_ancestor_parse):
    """Check if input_url is in the same domain as url_ancestor_parse - add lacking schema and domain if needed"""
    input_url_parse = urlparse(input_url)
    if not input_url_parse.netloc and not input_url_parse.scheme and input_url_parse.path:
        return urlunparse(input_url_parse._replace(
                scheme=url_ancestor_parse.scheme, netloc=url_ancestor_parse.netloc, params='', query='', fragment=''
            ))
    elif input_url_parse.netloc == url_ancestor_parse.netloc:
        return urlunparse(input_url_parse._replace(scheme=url_ancestor_parse.scheme, params='', query='', fragment=''))


def get_url_content(url: str) -> str:
    """Validate url request and extract content only from ['text/html', 'text/plain'] content-tpe header"""
    accepted_content_types = ['text/html', 'text/plain']
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f'Cannot GET from {url}')  # TODO: logging
        raise
    if r.status_code != 200:
        print(f'Cannot GET from {url} status code: {r.status_code}')  # TODO: logging
        raise URLGetStatusNot200Error
    elif not any(ct in r.headers.get('content-type', '') for ct in accepted_content_types):
        raise URLContentNotTextTypeError

    print("req encode", url, r.encoding if "charset" in r.headers.get("content-type", "").lower() else None)
    return r.content


def download_page(url: str, scrap_img=True, scrap_text=True, scrap_href=True) -> Tuple[Set, Set, str]:
    """

    :param url: scraped url address
    :param scrap_img: true - find images links, false - do nothing
    :param scrap_text: true - find text, false - do nothing
    :param scrap_href: true - scrap also all subpages links for give url

    """
    url_content = get_url_content(url)
    url_ancestor_parse = urlparse(url)
    soup = BeautifulSoup(url_content, 'html.parser')
    urls_set = set()
    img_src_set = set()
    url_text = ''

    if scrap_href:
        urls_set = find_hrefs(soup, url_ancestor_parse)
    if scrap_img:
        img_src_set = find_images_src(soup, url_ancestor_parse)
    if scrap_text:
        url_text = find_text(soup)

    return urls_set, img_src_set, url_text


def download_all_pages(url: str, output_path: str,  scrap_img: bool = True,
                       scrap_text: bool = True, scrap_recursive: bool = False):
    """
    :param url: scraped url address
    :param output_path: save there scraped content
    :param scrap_img: true - find images links and download, false - do nothing
    :param scrap_text: true - find text and download, false - do nothing
    :param scrap_recursive: true - scrap also all subpages links for give url
    :return:
    """
    all_urls_list = [url]
    all_urls_set = set(all_urls_list)
    all_img_src_set = set()
    all_urls_text = ''

    for url in all_urls_list:
        try:
            urls_set, img_src_set, url_text = download_page(url, scrap_img, scrap_text)
        except (URLGetStatusNot200Error, URLContentNotTextTypeError, requests.exceptions.ConnectionError):
            continue
        if scrap_recursive:
            all_urls_list.extend(urls_set - all_urls_set)
        all_urls_set |= urls_set
        all_img_src_set |= img_src_set
        all_urls_text = '\n'.join([all_urls_text, url_text])

    if scrap_text:
        save_text(all_urls_text, output_path)

    if scrap_img:
        download_images(all_img_src_set, output_path)
