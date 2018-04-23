# Generated by Django 2.0.4 on 2018-04-19 11:19

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'db_table': 'clients',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('project_url', models.URLField(verbose_name='Project URL')),
                ('description', models.TextField(blank=True)),
                ('completion_date', models.DateField()),
                ('in_development', models.BooleanField()),
                ('is_public', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bns.Client')),
            ],
            options={
                'db_table': 'project',
                'ordering': ('-completion_date',),
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('image_path', models.CharField(blank=True, max_length=100)),
                ('image', models.FileField(blank=True, upload_to='img/portfolio')),
                ('credit', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_featured', models.BooleanField(verbose_name='Is this image featured on your main pages?')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'db_table': 'project_images_new',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'type',
                'db_table': 'project_types',
                'verbose_name_plural': 'types',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'roles',
                'ordering': ('role',),
            },
        ),
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(to='bns.ProjectImage'),
        ),
        migrations.AddField(
            model_name='project',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bns.Role'),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ManyToManyField(blank=True, to='bns.ProjectType'),
        ),
    ]
