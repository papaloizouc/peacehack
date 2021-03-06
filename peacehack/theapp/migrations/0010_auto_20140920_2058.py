# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0009_auto_20140920_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='Day',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='EventCode',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='EventRootCode',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Month',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='NumArticles',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='NumMentions',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
