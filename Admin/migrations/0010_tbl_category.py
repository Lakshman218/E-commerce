# Generated by Django 4.1.7 on 2023-03-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Admin", "0009_remove_tbl_subcategory_category_delete_tbl_category_and_more"),
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
                ("cat_name", models.CharField(max_length=50)),
            ],
        ),
    ]
