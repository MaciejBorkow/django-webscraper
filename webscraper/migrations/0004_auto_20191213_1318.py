# Generated by Django 3.0 on 2019-12-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0003_auto_20191213_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapedurl',
            name='path',
        ),
        migrations.AddField(
            model_name='scrapedurl',
            name='path_base',
            field=models.TextField(default='/home/maciej/Desktop/semantive/Semantive/scraperservice/scraped_url'),
        ),
    ]