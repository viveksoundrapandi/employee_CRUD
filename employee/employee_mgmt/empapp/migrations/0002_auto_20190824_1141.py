# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WonDetails',
            fields=[
                ('won_no', models.IntegerField(serialize=False, primary_key=True)),
                ('won_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'won_details',
            },
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='econtact',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='eemail',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='end_date',
            field=models.DateField(default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='employee',
            name='start_date',
            field=models.DateField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='won_no',
            field=models.ForeignKey(default=None, to='empapp.WonDetails'),
            preserve_default=False,
        ),
    ]
