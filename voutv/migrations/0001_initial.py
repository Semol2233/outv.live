# Generated by Django 2.2.5 on 2020-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('details', models.TextField(blank=True)),
                ('img', models.ImageField(upload_to='Academic_Info/')),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apps_about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=100)),
                ('details', models.TextField(blank=True)),
                ('facebook_link', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Apps_linkup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
                ('link', models.URLField(max_length=500)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apps_slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='apps_Academic_Info/')),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='class_note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('details', models.TextField(blank=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='coverimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverimg', models.ImageField(upload_to='coverimg/')),
                ('img_title', models.CharField(max_length=200)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='livtv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_tv_url', models.URLField(max_length=500)),
                ('live_logo', models.ImageField(upload_to='live_tv_logo/')),
                ('channel_name', models.CharField(max_length=120)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice_bord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField(blank=True)),
                ('img', models.ImageField(upload_to='notice img/')),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='img/')),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
