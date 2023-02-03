# Generated by Django 4.1.5 on 2023-02-03 13:40

import community.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                ("content", models.TextField(verbose_name="댓글")),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Comment",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                ("content", models.TextField(verbose_name="대댓글")),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Image",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                (
                    "image",
                    models.ImageField(upload_to=community.models.image_upload_to),
                ),
            ],
            options={"verbose_name": "Image", "verbose_name_plural": "Images",},
        ),
        migrations.CreateModel(
            name="Post",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                ("title", models.CharField(max_length=200, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
                ("view_cnt", models.BigIntegerField(default=0)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="PostCount",
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
                ("ip", models.CharField(max_length=30)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="community.post"
                    ),
                ),
            ],
        ),
    ]
