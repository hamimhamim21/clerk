# Generated by Django 2.2.2 on 2019-06-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0002_imageupload"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="complete",
            field=models.BooleanField(default=False),
        ),
    ]
