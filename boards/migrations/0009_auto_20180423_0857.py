# Generated by Django 2.0.4 on 2018-04-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_introduction_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='headline',
            field=models.CharField(default=1232, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='subhead',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]