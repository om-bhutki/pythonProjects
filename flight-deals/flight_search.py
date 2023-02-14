import requests

from data_manager import DataManager
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.endpoint_2 = "https://tequila-api.kiwi.com/v2/search"
        self.api_key = "NNBAFHePY7BeVhsv5GqpaeapMU4cspSS"
        self.header = {
            "accept": "application/json",
            "apikey": self.api_key
        }

    def get_code(self,city_name):

        params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "active_only": "true"
        }
        response = requests.get(url=self.endpoint,params=params,headers=self.header)
        response.raise_for_status()
        code = response.json()['locations'][0]['city']['code']
        return code

    def get_flight_price(self,city_code):
        parameters = {
            "fly_from": "BOM",
            "fly_to": city_code,
            "date_from": "03/09/2022",
            "date_to": "03/03/2023",
            "flight_type": "oneway",
            "adults": 1,
            "adult_hold_bag": 1,
            "adult_hand_bag": 1,
            "limit": 500,
            "curr": "INR"
        }
        response = requests.get(url=self.endpoint_2,params=parameters,headers=self.header)
        response.raise_for_status()
        price = response.json()['data'][0]['price']
        return price


