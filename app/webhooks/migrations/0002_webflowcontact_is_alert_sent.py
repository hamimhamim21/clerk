# Generated by Django 3.0.5 on 2020-04-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webhooks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="webflowcontact",
            name="is_alert_sent",
            field=models.BooleanField(default=False),
        ),
    ]
