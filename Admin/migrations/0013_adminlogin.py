# Generated by Django 4.1.7 on 2023-04-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Admin", "0012_tbl_feedback_tbl_complaint"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adminlogin",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
