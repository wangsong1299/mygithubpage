# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, blank=True)),
                ('infotype', models.CharField(default=b'DF', max_length=2, choices=[(b'TR', b'\xe8\xae\xa9\xe5\xbf\x83\xe7\x81\xb5\xe5\x8e\xbb\xe6\x97\x85\xe8\xa1\x8c'), (b'WS', b'\xe6\x9d\xbe\xe9\xbc\xa0\xe8\xae\xb0\xe5\xbd\x95\xe5\x86\x8c'), (b'DF', b'\xe6\x9a\x82\xe6\x97\xb6\xe4\xb8\x8d\xe5\x88\x86\xe7\xb1\xbb')])),
                ('address', models.CharField(max_length=32)),
                ('reward', models.CharField(max_length=32)),
                ('noreward', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
