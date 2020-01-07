import os
import requests

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from webscraper.serializers import ScrapedUrlSerializer
from webscraper.models import ScrapedUrl
from webscraper.tasks import download_all_pages_wrap, CeleryStatuses
from webscraper.utils.queue import update_tasks_status_in_db, update_one_task_status_in_db

# TODO: update task_statuses_in_db as serializer for views
# TODO: use drf class serializers


@require_http_methods(['POST', 'GET'])
@csrf_exempt
def index(request):
    """
    List all scraped url tasks, or create a new task.

    POST Json example:
    {
        "url": "https://pl.wikipedia.org/wiki/Volkswagen_Golf",
        "image": true, - scrap images or not if False
        "text": true - scrap text or not if False
    }
    """
    if request.method == 'GET':
        update_tasks_status_in_db()
        scraped_urls = ScrapedUrl.objects.all()
        serializer = ScrapedUrlSerializer(scraped_urls, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        url = data['url']
        context = {}
        # TODO: validation to separate function
        try:
            r = requests.get(url)
        except Exception as e:
            return HttpResponse(f'Your url GET return cause exception{e}', status=400)
        if r.status_code != 200:
            return HttpResponse(f'Your url GET return status code {r.status_code}', status=400)
        image_flag = bool(data.get('image', False))
        text_flag = bool(data.get('text', False))
        if image_flag or text_flag:
            scraped_url = ScrapedUrl.objects.create(url=url, images=image_flag, text=text_flag)
        else:
            return HttpResponse(f'You have set all text adn images flag to False in the request Json: {data}')

        try:
            task = download_all_pages_wrap.delay(
                url=scraped_url.url, output_path=scraped_url.path(), scrap_img=image_flag, scrap_text=text_flag
            )
        except Exception as e:
            scraped_url.delete()
            return JsonResponse({'exception': str(e)}, status=500)
        scraped_url.queue = task.id
        scraped_url.status = task.status
        scraped_url.save()
        context['task_id'] = task.id
        context['task_status'] = task.status
        context['web_id'] = scraped_url.id

        return JsonResponse(context, status=201)

@require_http_methods(['GET'])
def detail(request, pk):
    """
    :param pk: scraped url task id
    :return: Json with detail for one task
    """
    update_one_task_status_in_db(pk)
    scraped_urls = get_object_or_404(ScrapedUrl, pk=pk)
    serializer = ScrapedUrlSerializer(scraped_urls, many=False)
    return JsonResponse(serializer.data, safe=False)


@require_http_methods(['GET'])
def images(request, pk):
    """Send images as pk_images.zip file"""
    update_one_task_status_in_db(pk)
    scraped_img_obj = get_object_or_404(ScrapedUrl, pk=pk, images=True, status=CeleryStatuses.SUCCESS)
    path = os.path.join(scraped_img_obj.path(), 'img.zip')
    response = HttpResponse(open(path, 'rb'), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{str(pk)}_img.zip"'
    return response


@require_http_methods(['GET'])
def text(request, pk):
    """Send text as pk_text.txt file"""
    update_one_task_status_in_db(pk)
    scraped_text_obj = get_object_or_404(ScrapedUrl, pk=pk, text=True, status=CeleryStatuses.SUCCESS)
    path = os.path.join(scraped_text_obj.path(), 'text.txt')
    response = HttpResponse(open(path, 'rb'), content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{str(pk)}_text.txt"'
    return response

