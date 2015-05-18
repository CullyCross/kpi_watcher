# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='voted_teachers',
            field=models.ManyToManyField(related_name='rated_groups', to='ratings.Teacher'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='voted_students',
            field=models.ManyToManyField(related_name='rated_teachers', to='ratings.Student'),
            preserve_default=True,
        ),
    ]
