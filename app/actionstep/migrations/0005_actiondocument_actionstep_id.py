# Generated by Django 3.0.6 on 2020-05-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actionstep", "0004_actiondocument"),
    ]

    operations = [
        migrations.AddField(
            model_name="actiondocument",
            name="actionstep_id",
            field=models.CharField(default="", max_length=64),
        ),
    ]
