# Generated by Django 2.0.4 on 2018-04-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0022_auto_20180424_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.TextField(default=2134, max_length=1000),
            preserve_default=False,
        ),
    ]