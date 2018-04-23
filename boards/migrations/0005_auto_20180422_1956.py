# Generated by Django 2.0.4 on 2018-04-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20180422_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='BNShome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('headline', models.TextField(blank=True)),
                ('subhead', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='bns_home',
        ),
    ]