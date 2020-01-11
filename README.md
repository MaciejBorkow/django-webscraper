=====
Polls
=====

Webscraper is a Django app with RESTapi to scrap data url addresses. It allow to scrap and download text and images from on url or all found suburls in the same domain recursively.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'webscraper',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('webscraper/', include('webscraper.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. TODO Celery, Redis
