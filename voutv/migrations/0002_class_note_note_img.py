# Generated by Django 2.2.5 on 2020-06-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voutv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_note',
            name='note_img',
            field=models.ImageField(default=1, upload_to='note_img/'),
            preserve_default=False,
        ),
    ]