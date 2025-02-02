# Generated by Django 4.2.13 on 2024-06-09 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Authors",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=255)),
                ("data_birth", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Books",
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
                ("title", models.CharField(max_length=200)),
                ("publish_date", models.DateField()),
                ("description", models.CharField(max_length=255)),
                (
                    "author_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.authors"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Members",
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
                ("name", models.CharField(max_length=100)),
                ("join_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="BorrowingRecords",
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
                ("borrow_date", models.DateField()),
                ("return_date", models.DateField()),
                (
                    "book_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.books"
                    ),
                ),
                (
                    "member_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.members"
                    ),
                ),
            ],
        ),
    ]
