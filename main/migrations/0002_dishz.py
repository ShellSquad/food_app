# Generated by Django 4.2.2 on 2023-06-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dishz",
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
                ("name", models.CharField(max_length=25500)),
                ("location", models.CharField(max_length=25500)),
                ("items", models.CharField(max_length=255000)),
            ],
        ),
    ]
