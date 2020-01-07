from rest_framework import serializers

from .models import ScrapedUrl


class ScrapedUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScrapedUrl
        fields = ['id', 'task', 'date_init', 'path']
