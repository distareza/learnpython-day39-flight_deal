import configparser

config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

sheet_token = config.get("sheety.co", "sheety.token")
tequila_token = config.get("tequila-api.kiwi.com", "tequila.token")

twilio_account_id = config.get("twilio.com", "twilio.api.sid")
twilio_api_token = config.get("twilio.com", "twilio.api.token")
twilio_virtual_number = config.get("my-personal-info", "my_virtual_number")
twilio_verified_number = config.get("my-personal-info", "my_verified_number")