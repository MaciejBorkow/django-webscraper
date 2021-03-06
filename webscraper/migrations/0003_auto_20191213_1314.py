# Generated by Django 3.0 on 2019-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0002_auto_20191211_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapedurl',
            name='images',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scrapedurl',
            name='path',
            field=models.TextField(default='/home/maciej/Desktop/semantive/Semantive/scraperservice/scraped_url'),
        ),
        migrations.AddField(
            model_name='scrapedurl',
            name='status',
            field=models.TextField(default='NOT_STARTED'),
        ),
        migrations.AddField(
            model_name='scrapedurl',
            name='suburls',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scrapedurl',
            name='text',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ScrapedUrlData',
        ),
    ]
