import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/c10adcd6088f6c04203a1a81d5af1183/flightDeals/prices"
        self.header = {"Content-Type": "application/json"}

    def add_code_to_sheet(self,row_id,code):
        code = {'price': {'iataCode': code}}
        response = requests.put(url=f"{self.endpoint}/{row_id}", json=code, headers=self.header)
        response.raise_for_status()

    def add_price_to_sheet(self,row_id,price):
        price_data = {'price': {'lowestPrice': price}}
        response = requests.put(url=f"{self.endpoint}/{row_id}", json=price_data, headers=self.header)
        response.raise_for_status()

    def get_city(self):
        city_names = []
        for i in range(2, 11):
            response = requests.get(url=f"{self.endpoint}/{i}", headers=self.header)
            city_names.append(response.json()['price']['city'])
        return city_names

    def get_city_code(self):
        city_codes = []
        for i in range(2, 11):
            response = requests.get(url=f"{self.endpoint}/{i}", headers=self.header)
            city_codes.append(response.json()['price']['iataCode'])
        return city_codes
