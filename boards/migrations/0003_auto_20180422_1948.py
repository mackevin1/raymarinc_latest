# Generated by Django 2.0.4 on 2018-04-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_bns_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline1', models.CharField(max_length=250)),
                ('backimage', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('headline', models.TextField(blank=True)),
                ('subhead', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'homepage',
            },
        ),
        migrations.AddField(
            model_name='bns_home',
            name='headline',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bns_home',
            name='subhead',
            field=models.TextField(blank=True),
        ),
    ]
