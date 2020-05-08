import logging

from django.views.decorators.http import require_http_methods
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.http import HttpResponseBadRequest, HttpResponse

from .models import WebflowContact

logger = logging.getLogger(__file__)

from twilio.rest import Client

from twilio.twiml.voice_response import VoiceResponse, Gather


@require_http_methods(["GET"])
def twilio_call_view(request):
    r = VoiceResponse()
    dial_number_str = request.GET.get("Digits")
    if dial_number_str:
        r.say(f"Connecting you to dialled number.")
        if dial_number_str.startswith("04"):
            dial_number_str = "+61" + dial_number_str[1:]
        r.dial(
            dial_number_str,
            method="GET",
            action="/twilio/end/",
            record="record-from-answer",
            recordingStatusCallback="/twilio/record/",
        )
    else:
        gather = Gather(action="/twilio/", method="GET", timeout=10)
        gather.say("Dial a number then press hash.")
        r.append(gather)

    return TwimlResponse(r)


from django.views.decorators.csrf import csrf_exempt


@require_http_methods(["GET", "POST"])
@csrf_exempt
def twilio_record_call_view(request):
    """
    Receive recalling status callbacl
    request.POST
    <QueryDict: {
        'RecordingSource': ['DialVerb'],
        'RecordingSid': ['zzzz'],
        'RecordingUrl': ['zz'],
        'RecordingStatus': ['completed'],
        'RecordingChannels': ['1'],
        'ErrorCode': ['0'],
        'CallSid': ['zzzz'],
        'RecordingStartTime': ['Sat, 02 May 2020 00:45:44 +0000'],
        'AccountSid': ['zzz'],
        'RecordingDuration': ['7']
    }>
    """
    return HttpResponse("Success?")


@require_http_methods(["GET"])
def twilio_end_call_view(request):
    """Thank user & hang up."""
    r = VoiceResponse()
    r.say("Successful call.")
    r.hangup()
    return TwimlResponse(r)


class TwimlResponse(HttpResponse):
    """
    HTTP response returning Twilio Markup Language (TwiML)
    """

    def __init__(self, twiml_obj, **kwargs):
        super_kwargs = {"status": 200, "content_type": "application/xml", **kwargs}
        return super().__init__(str(twiml_obj), **super_kwargs)


@api_view(["POST"])
def webflow_form_view(request):
    """
    Save data from webflow form submission.
    Can't use DRF serializers here because the form names are ugly as fuck.

    By the way this is super insecure and you can spam the shit out of this using curl from anywhere.
    curl \
        --header "Content-Type: application/json" \
        --request POST  \
        --data '{"data": {"name": "Matt", "email": "matt@foo.com", "phone": "11111"}}' \
        http://localhost:8000/api/webhooks/webflow-form/

    But don't because it'd be a shitty thing to do.
    """
    try:
        data = request.data["data"]
        model_kwargs = {"name": data["Name"], "email": data["Email"], "phone": data["Phone Number"]}
    except KeyError:
        raise ValidationError("Invalid request format.")

    WebflowContact.objects.create(**model_kwargs)
    return Response({"message": "We got the form. :)"}, status=201)
