import json

from django.contrib import admin
from django.contrib.messages import constants as messages
from django.utils.safestring import mark_safe
from django_q.tasks import async_task
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer

from questions.models import FileUpload, ImageUpload, Submission
from questions.services.slack import send_submission_slack
from questions.services.submission import send_submission_email
from questions.services.actionstep import send_submission_actionstep


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    readonly_fields = ("answers_json",)
    exclude = ("questions", "answers")
    list_display = (
        "id",
        "topic",
        "created_at",
        "modified_at",
        "num_answers",
        "complete",
    )
    list_filter = ("topic", "complete")

    actions = ["notify", "integrate"]

    def integrate(self, request, queryset):
        for submission in queryset:
            async_task(send_submission_actionstep, str(submission.pk))

        self.message_user(request, "Integrations sent.", level=messages.INFO)

    integrate.short_description = "Integrate with external systems"

    def notify(self, request, queryset):
        for submission in queryset:
            async_task(send_submission_email, str(submission.pk))
            async_task(send_submission_slack, str(submission.pk))

        self.message_user(request, "Notifications sent.", level=messages.INFO)

    notify.short_description = "Send notifications"

    def answers_json(self, instance):
        return dict_to_json_html(instance.answers)


@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display = ("id", "created_at", "modified_at", "image")


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display = ("id", "created_at", "modified_at", "file")


def dict_to_json_html(data):
    json_str = json.dumps(data, sort_keys=True, indent=2)
    formatter = HtmlFormatter(style="colorful")
    highlighted = highlight(json_str, JsonLexer(), formatter)
    style = "<style>" + formatter.get_style_defs() + "</style><br>"
    return mark_safe(style + highlighted)
