# Generated by Django 5.0.1 on 2024-01-19 04:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userApp", "0006_user_cars"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="website",
            options={
                "ordering": ["reting"],
                "verbose_name": "sitio Web",
                "verbose_name_plural": "sitio Webs",
            },
        ),
        migrations.AlterModelTable(
            name="website",
            table="Nombre de la tabla",
        ),
    ]