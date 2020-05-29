# Generated by Django 3.0.6 on 2020-05-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccessToken",
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
                ("expires_in", models.IntegerField()),
                ("api_endpoint", models.URLField()),
                ("orgkey", models.CharField(max_length=256)),
                ("token", models.CharField(max_length=1024)),
                ("refresh_token", models.CharField(max_length=1024)),
            ],
        ),
    ]