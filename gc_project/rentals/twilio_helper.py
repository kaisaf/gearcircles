import json

from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException


with open('rentals/twilio_settings.json') as data_file:
    twilio_settings = json.load(data_file)


def create_twilio_client():
    account_sid = twilio_settings["account_sid"]
    auth_token  = twilio_settings["auth_token"]
    return TwilioRestClient(account_sid, auth_token)


def send_sms(phone, text):
    client = create_twilio_client()
    message = client.messages.create(
        body = text,
        to = phone,
        from_ = twilio_settings["number"]) # Twilio number

# def validate_number(phone):
#     """
#     Return None if phone is valid or error message
#     params: phone String "+12223334444"
#     """
#     client = create_twilio_client()
#     try:
#         response = client.caller_ids.validate(phone)
#         code = response.get("validation_code")
#         return code
#     except TwilioRestException as e:
#         return e.msg
#     return None
