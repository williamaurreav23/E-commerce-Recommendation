# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0020_auto_20171001_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 32, 44, 278694, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 32, 44, 279471, tzinfo=utc), null=True, blank=True),
        ),
    ]
