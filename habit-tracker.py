import requests
from datetime import datetime as dt
USERNAME = "om-bhutki"
TOKEN = "rgehashershgszrrsgwgef"
ENDPOINT = "https://pixe.la/v1/users"
ID = "code1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}


# response = requests.post(url="https://pixe.la/v1/users",json=user_params)
# print(response.text)

graph_config = {
    "id": ID,
    "name": "Coding Tracking",
    "unit": "h",
    "type": "int",
    "color": "shibafu"

}

header_token = {
    "X-USER-TOKEN": TOKEN
}
today = dt(year=2022, month=8, day=9)

DATE = today.strftime("%Y%m%d")

pixel_config = {
    "date": DATE,
    "quantity": "4",


}
# response = requests.post(url=f"https://pixe.la//v1/users/{USERNAME}/graphs",json=graph_config,headers=header_token)
# print(response.text)

update_pixel = {
    "quantity": "8"

}

response = requests.delete(url=f"{ENDPOINT}/{USERNAME}/graphs/{ID}/{DATE}",headers=header_token)
print(response.text)
print(response.status_code)