# Generated by Django 3.0.6 on 2020-05-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actionstep", "0002_auto_20200513_1036"),
    ]

    operations = [
        migrations.AddField(
            model_name="accesstoken",
            name="is_active",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
