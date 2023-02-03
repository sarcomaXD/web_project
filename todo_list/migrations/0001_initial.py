# Generated by Django 4.1.5 on 2023-02-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("complete", models.BooleanField(default=False)),
                ("important", models.BooleanField(default=False)),
                ("start_date", models.DateTimeField(verbose_name="시작일시")),
                ("end_date", models.DateTimeField(verbose_name="종료일시")),
            ],
        ),
    ]
