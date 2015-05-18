# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('avg_rating', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('avg_rating', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('avg_rating', models.DecimalField(default=0, editable=False, max_digits=3, decimal_places=2)),
                ('count_of_votes', models.IntegerField(default=0, editable=False)),
                ('department', models.ForeignKey(related_name='groups', to='ratings.Department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_leader', models.BooleanField(default=False)),
                ('group', models.ForeignKey(related_name='students', to='ratings.Group')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avg_rating', models.DecimalField(default=0, editable=False, max_digits=3, decimal_places=2)),
                ('count_of_votes', models.IntegerField(default=0, editable=False)),
                ('department', models.ForeignKey(related_name='teachers', to='ratings.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('voted_students', models.ManyToManyField(related_name='voted_students', to='ratings.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('avg_rating', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='voted_teachers',
            field=models.ManyToManyField(related_name='voted_teachers', to='ratings.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(related_name='faculties', to='ratings.University'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(related_name='departments', to='ratings.Faculty'),
            preserve_default=True,
        ),
    ]
