# Generated by Django 4.1.7 on 2023-06-28 13:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
            ],
        ),
        migrations.CreateModel(
            name="food",
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
                ("Item_Image", models.ImageField(upload_to="")),
                ("Item_Name", models.CharField(max_length=100)),
                ("Item_Quantity", models.CharField(max_length=100)),
                ("Item_Cost", models.DecimalField(decimal_places=2, max_digits=6)),
                ("Item_Published", models.BooleanField(default=True)),
                (
                    "Manufactured_Date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                ("Item_Review", models.TextField()),
                (
                    "Item_Category",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="varieties.category",
                    ),
                ),
            ],
        ),
    ]
