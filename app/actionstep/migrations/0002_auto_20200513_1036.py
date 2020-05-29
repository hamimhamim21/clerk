# Generated by Django 3.0.6 on 2020-05-13 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("actionstep", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="accesstoken",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="accesstoken",
            name="expires_at",
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
