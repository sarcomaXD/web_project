# Generated by Django 4.1.4 on 2023-01-22 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

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
                ("content", models.TextField(verbose_name="내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author_answer",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Care",
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
                ("title", models.CharField(max_length=30)),
                ("place", models.CharField(max_length=30)),
                ("content", models.TextField(default="", null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("photo", models.ImageField(blank=True, null=True, upload_to="")),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("view_cnt", models.BigIntegerField(default=0)),
                (
                    "best",
                    models.ManyToManyField(
                        related_name="best",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="추천수",
                    ),
                ),
            ],
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
                ("content", models.TextField(verbose_name="내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                (
                    "answer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="board.answer",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="board.care",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CareCount",
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
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="board.care"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="board.care"
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_answer",
                to=settings.AUTH_USER_MODEL,
                verbose_name="추천수",
            ),
        ),
    ]