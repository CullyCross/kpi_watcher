# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20150518_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='avg_rating',
            field=models.DecimalField(default=0, editable=False, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='avg_rating',
            field=models.DecimalField(default=0, editable=False, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='voted_teachers',
            field=models.ManyToManyField(related_name='rated_groups', editable=False, to='ratings.Teacher'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='avg_rating',
            field=models.DecimalField(default=0, editable=False, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='voted_students',
            field=models.ManyToManyField(related_name='rated_teachers', editable=False, to='ratings.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='avg_rating',
            field=models.DecimalField(default=0, editable=False, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
    ]
