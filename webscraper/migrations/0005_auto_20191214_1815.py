# Generated by Django 3.0 on 2019-12-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0004_auto_20191213_1318'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='scrapedurl',
            index=models.Index(fields=['queue'], name='webscraper__queue_8c3e3e_idx'),
        ),
    ]
