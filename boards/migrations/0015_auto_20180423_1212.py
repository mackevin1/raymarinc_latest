# Generated by Django 2.0.4 on 2018-04-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0014_board_sectionridrbody'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='imagenoc1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='board',
            name='imagenoc2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='board',
            name='imagenoc3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='board',
            name='imagenoc4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnoc1',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnoc1head',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnoc2',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnoc2head',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnoc3',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnoc3head',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnoc4',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnoc4head',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnocbody',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnocheadline',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='board',
            name='sectionnocsubhead',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
