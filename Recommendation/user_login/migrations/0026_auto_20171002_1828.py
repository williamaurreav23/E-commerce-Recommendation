# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0025_auto_20171002_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 18, 28, 22, 788694, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 18, 28, 22, 789469, tzinfo=utc), null=True, blank=True),
        ),
    ]
