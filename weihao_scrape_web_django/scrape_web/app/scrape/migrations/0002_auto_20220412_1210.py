# Generated by Django 3.2.13 on 2022-04-12 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scrapeconfigaccount',
            options={'verbose_name': '船运账号配置', 'verbose_name_plural': '船运账号配置'},
        ),
        migrations.AlterModelOptions(
            name='scrapetask',
            options={'verbose_name': '侦测航线', 'verbose_name_plural': '侦测航线'},
        ),
    ]
