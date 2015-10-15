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
                ('infotype', models.CharField(default=b'DF', max_length=3, choices=[(b'EM', b'\xe6\x84\x9f\xe6\x80\xa7\xe6\x96\x87\xe7\xab\xa0'), (b'DI', b'\xe6\x9d\xbe\xe9\xbc\xa0\xe6\x97\xa5\xe8\xae\xb0'), (b'AR', b'\xe5\xa5\x87\xe6\x96\x87\xe5\x85\xb1\xe8\xb5\x8f'), (b'SO', b'\xe9\x9a\x8f\xe4\xbe\xbf\xe6\xba\x9c\xe6\xba\x9c'), (b'DF', b'\xe6\x9c\xaa\xe5\x88\x86\xe7\xb1\xbb\xe5\x9c\xb0')])),
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
