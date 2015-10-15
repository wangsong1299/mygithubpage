# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('infotype', models.CharField(default=b'DF', max_length=2, choices=[(b'SW', b'\xe8\x87\xaa\xe5\xb7\xb1\xe9\x97\xb9\xe7\x9d\x80\xe7\x8e\xa9'), (b'PT', b'\xe5\x85\xbc\xe8\x81\x8c\xe5\x8a\xaa\xe5\x8a\x9b\xe5\x81\x9a'), (b'FT', b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x9c\xa8\xe5\x93\xaa\xe9\x87\x8c'), (b'DF', b'\xe6\x9a\x82\xe6\x97\xb6\xe4\xb8\x8d\xe5\x88\x86\xe7\xb1\xbb')])),
                ('tag', models.CharField(max_length=32)),
                ('abstract', models.CharField(max_length=100)),
                ('reward', models.CharField(max_length=32)),
                ('noreward', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
