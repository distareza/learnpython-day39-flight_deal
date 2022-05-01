import my_configuration
import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0fef89f09eb88a13f921e2aac5911ded/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}
        self.bearer_headers = {
            "Authorization": f"Bearer {my_configuration.sheet_token}"
        }

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.bearer_headers)
        data = response.json()

        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.bearer_headers
            )
            print(response.text)

    def update_destination_code(self, city_name:str, iata_code:str):
        for row in self.destination_data:
            if row['city'] == city_name:
                row_id = row['id']
                new_data = {
                    "price": {
                        "iataCode": iata_code
                    }
                }
                row['iataCode'] = iata_code
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
                    json=new_data,
                    headers=self.bearer_headers
                )
                if response.status_code == 200:
                    print("update successfully")
                else:
                    print("not able to update")


