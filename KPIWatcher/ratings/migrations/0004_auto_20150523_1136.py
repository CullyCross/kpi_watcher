# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20150523_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='avg_rating',
            field=models.DecimalField(default=0, editable=False, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='avg_rating',
            field=models.DecimalField(default=0, editable=False, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='avg_rating',
            field=models.DecimalField(default=0, editable=False, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='avg_rating',
            field=models.DecimalField(default=0, editable=False, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
