# Generated by Django 4.1.7 on 2023-04-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Seller", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tbl_slrproduct", name="prdct_rate", field=models.IntegerField(),
        ),
    ]
