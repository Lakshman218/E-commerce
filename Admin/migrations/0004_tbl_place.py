# Generated by Django 4.1.7 on 2023-03-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Admin", "0003_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="tbl_Place",
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
                ("plc_name", models.CharField(max_length=50)),
            ],
        ),
    ]
