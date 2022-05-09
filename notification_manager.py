import smtplib

from twilio.rest import Client
import my_configuration

TWILIO_SID = my_configuration.twilio_account_id
TWILIO_AUTH_TOKEN = my_configuration.twilio_api_token
TWILIO_VIRTUAL_NUMBER = my_configuration.twilio_virtual_number
TWILIO_VERIFIED_NUMBER = my_configuration.twilio_verified_number

EMAIL_PROVIDER_SMTP_ADDRESS = my_configuration.email_provider_smtp_address
EMAIL_PORT = my_configuration.email_port
MY_EMAIL = my_configuration.email_sender
MY_PASSWORD = my_configuration.email_password

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

    def send_emails(self, emails, message, google_flight_link):
        # print(EMAIL_PROVIDER_SMTP_ADDRESS)
        # print(EMAIL_PORT)
        # print(MY_EMAIL)
        # print(MY_PASSWORD)
        with smtplib.SMTP(host=EMAIL_PROVIDER_SMTP_ADDRESS, port=EMAIL_PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                # print(email)
                # print(message)
                # print(google_flight_link)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )