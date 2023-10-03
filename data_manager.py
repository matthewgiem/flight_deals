from api_keys import Sheety_Endpoint, Sheety_Baerer_Token
import requests

sheety_headers = {
    "Authorization": f"Bearer {Sheety_Baerer_Token}"
}

# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def read_data_sheet(self):
        response = requests.get(url=Sheety_Endpoint, headers=sheety_headers)
        data = response.json()
        print(data)

    def get_destination_data(self):
        response = requests.get(url=Sheety_Endpoint, headers=Sheety_Baerer_Token)
        data = response.json()
        self.destination_data = data["Lowest Price"]
        print(data)