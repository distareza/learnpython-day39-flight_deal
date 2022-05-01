from twilio.rest import Client
import my_configuration

TWILIO_SID = my_configuration.twilio_account_id
TWILIO_AUTH_TOKEN = my_configuration.twilio_api_token
TWILIO_VIRTUAL_NUMBER = my_configuration.twilio_virtual_number
TWILIO_VERIFIED_NUMBER = my_configuration.twilio_verified_number


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        try :
            message = self.client.messages.create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
            )
            # Prints if successfully sent.
            print(message.sid)
        except Exception as ex:
            print(ex)