import os
import shutil

from django.db import models
from django.conf import settings
from django.core.validators import URLValidator
from django.utils import timezone


class Queue(models.Model):
    class NameChoice(models.TextChoices):
        WEBSCRAPER = 'scraperservice'
    name = models.TextField()


class QueueTaskStatus(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = 'PENDING'
        RECEIVED = 'RECEIVED'
        STARTED = 'STARTED'
        SUCCESS = 'SUCCESS'
        FAILURE = 'FAILURE'
        REVOKED = 'REVOKED'
        RETRY = 'RETRY'

    name = models.TextField(unique=True, choices=StatusChoice.choices)


class QueueTask(models.Model):
    queue = models.ForeignKey(Queue, on_delete=models.SET_NULL, null=True)
    task_id = models.TextField(unique=True)
    status = models.ForeignKey(QueueTaskStatus, on_delete=models.SET_NULL, null=True) # default foreign model


class UrlContentType(models.Model):
    class ContentType(models.TextChoices):
        TEXT = 'text'
        IMAGES = 'images'
        RECURSIVE_URL = 'recursive_url'

    name = models.TextField(unique=True, choices=ContentType.choices)

    def __str__(self):
        return self.name


class ScrapedUrlManager(models.Manager):

    def create_with_directory(self, *args, **kwargs):
        url = super().create(*args, **kwargs)
        url.path = os.path.join(url.path, str(url.id))
        url.save()
        try:
            os.makedirs(url.path)
        except FileExistsError:
            shutil.rmtree(url.path)
            os.makedirs(url.path)
        except Exception as e:
            url.delete()
            return
        return url


class ScrapedUrl(models.Model):
    objects = ScrapedUrlManager()

    url = models.URLField()  # TODO: validators=[URLValidator(schemaes=['http', 'https'])])
    task = models.OneToOneField(QueueTask, blank=True, on_delete=models.SET_NULL, null=True)
    content_type = models.ManyToManyField(UrlContentType)
    date_init = models.DateTimeField(default=timezone.now)
    path = models.FilePathField(default=settings.SCRAPED_DATA_DIR)

    def delete(self, *args, **kwargs):
        shutil.rmtree(self.path, ignore_errors=True)
        super().delete(*args, **kwargs)
