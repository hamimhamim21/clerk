# Generated by Django 2.2.1 on 2019-05-26 10:50

from django.db import migrations, models
import django.utils.timezone
import questions.models.image_upload
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageUpload",
            fields=[
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "modified_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=questions.models.image_upload.get_s3_key
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
