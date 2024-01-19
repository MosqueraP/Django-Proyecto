# Generated by Django 5.0.1 on 2024-01-19 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Website",
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
                ("url", models.URLField()),
                ("release_date", models.DateField()),
                ("reting", models.IntegerField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userApp.user"
                    ),
                ),
            ],
        ),
    ]