# Generated by Django 3.0.6 on 2020-05-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0008_fileupload"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="is_case_sent",
            field=models.BooleanField(default=False),
        ),
    ]
