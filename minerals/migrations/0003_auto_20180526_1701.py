# Generated by Django 2.0.5 on 2018-05-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0002_auto_20180526_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='image_filename',
            field=models.ImageField(max_length=255, null=True, upload_to=''),
        ),
    ]
