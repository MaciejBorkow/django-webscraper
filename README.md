# WEBSCRAPER APP
Webscraper is a Django app with RESTapi to scrap data from url addresses. It allow to scrap and download a few data types:
 text and images from an url or all found suburls in the same domain recursively. 
 
# Comment from author
- Tech stack: Python 3.7, Django 3.0, Djangorestframework, BeautifulSoup v4, Celery, Redis, SQLite, unittest
- Test: tests are really superficial.
- RestApi: in views shall be used class from DRF instead method
- Code: scrapservice/webscraper/utils/scraper.py has to be refactored - i started developing with functions but over time it grown and now class design would be better imo.

# Installation
- downloading
    - as git repo for development
        - clone repo
        - create virtual env: `python -m pipenv install`
    - as package for a project
        - Run in your virtual env: `pip install git+https://github.com/MaciejBorkow/django-webscraper.git#egg=django-webscraper` 
- Redis installation
    - Download the Redis tarball file and extract it in some directory
    - extract tarball and run inside the directory:  `sudo make install`


# Setup your Django project
1. Add "webscraper" to your INSTALLED_APPS setting in `settings.py`:
    ```
   INSTALLED_APPS = [
        ...
        'webscraper',
    ]
   ```
1. Include the webscraper URLconf in your project `urls.py`:
    ```
   urlpatterns = [
        ... 
        path('webscraper/', include('webscraper.urls')),
   ]
   ```
1. Add path for scraped data to `settings.py`
    ```
    SCRAPED_DATA_DIR = os.path.join(BASE_DIR, 'scraped_url')
   ```
1. Config Celery for your project. Example configuration: 
    - Add `example/scrapservice/celery.py` file to your Django project or create own one
    - Add Celery configuration in settings.py:
        ```
        CELERY_BROKER_URL = 'redis://localhost:6379'
        CELERY_RESULT_BACKEND = 'redis://localhost:6379'
        CELERY_ACCEPT_CONTENT = ['application/json']
        CELERY_RESULT_SERIALIZER = 'json'
        CELERY_TASK_SERIALIZER = 'json'
        ```
1. go to `/manage.py` directory and run in shell:
    - `python manage.py makemigrations`
    - `python manage.py migrate`

# Run app
1. Run Redis in shell: `redis-server`

1. Run Celery python script in shell: `celery worker -A scraperservice --loglevel=info` in manage.py directory

1. Run web serverDjango in shell: `python manage.py runserver`

THE END :D - should work

# API
* `/webscraper/url/`
    * GET - return JSON list with data about all scraped URL with statuses 
    ```
    {"id": task_id:int,
   "status": task_status:str,
   "url": scraped_url:str,
   "queue": queue_id:str,
   "images": scraped_or_not:bool,
   "text": scraped_or_not:bool,
   "suburls": scraped_or_not:bool,
   "date_init_request":request_date:str
  }
   exapmple JSON:
   {"id": 7, "status": "SUCCESS", "url": "https://pl.wikipedia.org/wiki/Volkswagen_Golf", "queue": "test", "images": true, "text": true, "suburls": false, "date_init_request": "2019-12-12T01:39:25.675399+01:00"}
    ```
    * POST JSON 
    ```
  {"url": url_to_scrap:str, 
  "image": scraped_or_not:bool, 
  "text": scraped_or_nor:bool}    
  
  example: 
  {
        "url": "https://pl.wikipedia.org/wiki/Volkswagen_Golf",
        "image": true, - scrap images or not if False
        "text": true - scrap text or not if False
    }
  ```
* `/webscraper/url/<task_id>/` 
    * GET - the same information as /webscraper/url/ GET but for only one id
* `/webscraper/url/<task_id>/images/` 
    * GET - download scraped images in zip file <task_id>_img.zip
* `/webscraper/url/<task_id>/text/` 
    * GET - download scraped text in txt file <task_id>_text.txt

