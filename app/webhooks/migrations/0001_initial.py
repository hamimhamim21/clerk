# Generated by Django 3.0.5 on 2020-04-30 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WebflowContact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "modified_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
            ],
            options={"abstract": False,},
        ),
    ]
