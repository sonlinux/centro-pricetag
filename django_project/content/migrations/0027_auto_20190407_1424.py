# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_hub'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutUs',
        ),
        migrations.DeleteModel(
            name='Foreword',
        ),
        migrations.DeleteModel(
            name='smartcare',
        ),
    ]
