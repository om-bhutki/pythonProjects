# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

sheet = DataManager()
city_list = sheet.get_city()
flight = FlightSearch()
code_list = [flight.get_code(name) for name in city_list]
# for code in code_list:
#     sheet.add_code_to_sheet(code_list.index(code) + 2, code)

price_list = [flight.get_flight_price(code) for code in code_list]
for price in price_list:
    sheet.add_price_to_sheet(price_list.index(price) + 2, price)
for i in range(2,11):
    print(f"{city_list[i]}:₹{price_list[i]}")

