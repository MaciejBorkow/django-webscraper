from django.urls import path, include
from rest_framework import routers

from webscraper.views import gui_views, api_views


app_name = 'webscraper'
urlpatterns = [
    path('', gui_views.home, name='home'),
    path('url_form', gui_views.url_form, name='url_form'),
    path('url/', gui_views.index, name='index'),
    path('url/<int:pk>/', gui_views.DetailView.as_view(), name='detail'),
    path('api/url/', api_views.index, name='api_index'),
    path('api/url/<int:pk>/', api_views.detail, name='api_detail'),
    path('api/url/<int:pk>/images/', api_views.images, name='images'),
    path('api/url/<int:pk>/text/', api_views.text, name='text'),
]
