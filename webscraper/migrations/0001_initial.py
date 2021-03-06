# Generated by Django 3.0 on 2019-12-09 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrapedUrlText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('data', models.BinaryField()),
                ('Scraped_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webscraper.ScrapedUrl')),
            ],
        ),
        migrations.CreateModel(
            name='ScrapedUrlImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('data', models.BinaryField()),
                ('Scraped_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webscraper.ScrapedUrl')),
            ],
        ),
    ]
