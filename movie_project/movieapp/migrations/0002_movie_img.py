# Generated by Django 4.1.1 on 2022-10-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=-2022, upload_to='pics'),
            preserve_default=False,
        ),
    ]
