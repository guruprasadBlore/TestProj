# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('Can_Modify', 'Can Modify the blog content'),)},
        ),
    ]
