# Generated by Django 4.1.4 on 2023-01-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0005_remove_care_photo_care_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="care", name="place", field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="care", name="title", field=models.CharField(max_length=15),
        ),
    ]