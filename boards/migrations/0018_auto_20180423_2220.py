# Generated by Django 2.0.4 on 2018-04-23 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0017_auto_20180423_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=100)),
                ('images', models.FileField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('productid', models.CharField(max_length=100)),
                ('tbipartnumber', models.TextField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('value', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('searchkeys', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boards.Category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boards.Products')),
            ],
        ),
        migrations.AddField(
            model_name='productimages',
            name='images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boards.Products'),
        ),
        migrations.AddField(
            model_name='productimages',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boards.Products'),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boards.Products'),
        ),
    ]