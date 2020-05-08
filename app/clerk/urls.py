from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from questions.views import apis
from webhooks.views import (
    webflow_form_view,
    twilio_call_view,
    twilio_end_call_view,
    twilio_record_call_view,
)

router = routers.SimpleRouter()
router.register("submission", apis.SubmissionViewSet, basename="submission")
router.register("images", apis.ImageUploadViewSet, basename="images")
urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("twilio/", twilio_call_view),
    path("twilio/end/", twilio_end_call_view),
    path("twilio/record/", twilio_record_call_view),
    path("api/webhooks/webflow-form/", webflow_form_view, name="webflow-form"),
    path("api/", include(router.urls)),
]
