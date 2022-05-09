#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Read data from Google Sheet
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

#  check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
# if sheet_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     print(f"sheet_data:\n {sheet_data}")
#
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()

from flight_search import FlightSearch
flight_search = FlightSearch()
for row in sheet_data:
    city = row["city"]
    iataCode = row["iataCode"]
    if iataCode == "":
        iataCode = flight_search.get_destination_code(city)
        data_manager.update_destination_code(city, iataCode)
    print(f"city {city} ( {iataCode } ) ")

import pprint
pprint.pprint(sheet_data)

# get date of tomorrow and six month from today
from datetime import datetime, timedelta
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

from notification_manager import NotificationManager
notification_manager = NotificationManager()

# search for cheap flight
ORIGIN_CITY_IATA = "LON"
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # For some destinations, certain time periods, there will be no flights available.
    # We need to add exception handling to our code so that it doesn't break and crash in these situations.
    if flight is None:
        continue
    if destination["lowestPrice"] is None:
        continue

    # If Flight Price Lower than in Google Sheet send an SMS
    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        #notification_manager.send_sms(message)
        print(message)
        notification_manager.send_emails(emails, message, link)
