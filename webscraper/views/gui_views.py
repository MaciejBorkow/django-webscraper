import os
import requests

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

from webscraper.models import ScrapedUrl, UrlContentType
from webscraper.tasks import CeleryStatuses
from webscraper.utils.queue import update_one_task_status_in_db

# TODO: update task_statuses_in_db as serializer for views
# TODO: use drf class serializers


def home(request):
    return HttpResponse('Home sweet home!')


@require_http_methods(['POST'])
@csrf_exempt
def url_form(request):
    url = ScrapedUrl.objects.create(url=request.POST['url'])
    content_type = [int(i) for i in request.POST.getlist('content_type')]
    url.content_type.add(*UrlContentType.objects.filter(id__in=content_type))
    return HttpResponseRedirect(reverse('webscraper:detail', kwargs={'pk': str(url.id)}))



def index(request):
    scraped_url_list = ScrapedUrl.objects.all()
    content_type_list = UrlContentType.objects.all()
    template = 'webscraper/index.html'
    context = {
        'scraped_url_list': scraped_url_list,
        'content_type_list': content_type_list,
    }
    return render(request, template, context)


# @require_http_methods(['GET'])
# def detail(request, pk):
#     scraped_url = get_object_or_404(ScrapedUrl, pk=pk)
#     template = 'webscraper/detail.html'
#     context = {'scraped_url': scraped_url}
#     return render(request, template, context)

class DetailView(generic.DetailView):
    model = ScrapedUrl
    template_name = 'webscraper/detail.html'


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
