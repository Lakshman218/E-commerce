# Generated by Django 4.1.7 on 2023-03-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Admin", "0006_tbl_place_district_alter_tbl_place_plc_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="tbl_Category",
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
            ],
        ),
    ]