# Generated by Django 3.2.10 on 2022-07-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novelweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='douluo',
            name='content',
            field=models.TextField(verbose_name='正文'),
        ),
    ]
