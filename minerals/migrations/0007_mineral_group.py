# Generated by Django 2.0.6 on 2018-09-04 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0006_merge_20180829_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='group',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
