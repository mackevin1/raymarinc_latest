# Generated by Django 2.0.4 on 2018-04-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0024_auto_20180424_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='description',
            new_name='proddescription',
        ),
    ]
