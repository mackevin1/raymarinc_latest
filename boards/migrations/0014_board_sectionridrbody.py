# Generated by Django 2.0.4 on 2018-04-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0013_auto_20180423_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='sectionridrbody',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
