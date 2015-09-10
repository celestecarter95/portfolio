# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='image',
            field=models.ImageField(null=True, upload_to=b'items/%Y/%m/%d', blank=True),
        ),
    ]
