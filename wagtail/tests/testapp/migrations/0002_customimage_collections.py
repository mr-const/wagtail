# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='collection',
            field=models.ForeignKey(default=wagtail.wagtailcore.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection'),
        ),
        migrations.AddField(
            model_name='customimagefilepath',
            name='collection',
            field=models.ForeignKey(default=wagtail.wagtailcore.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection'),
        ),
    ]
