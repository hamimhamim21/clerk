from django.db import models

from questions.models.timestamped import TimestampedModel


class WebflowContact(TimestampedModel):
    """
    A client contact form submission from anikalegal.com
    """

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    # Tracks whether a Slack alert has been successfully sent.
    is_alert_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} {self.email}"
