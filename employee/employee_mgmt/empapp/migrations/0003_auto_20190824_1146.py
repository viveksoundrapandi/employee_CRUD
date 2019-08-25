# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_auto_20190824_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='won_no',
            new_name='won',
        ),
    ]
