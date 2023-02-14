import requests
from twilio.rest import Client

MY_LAT = 19.218330  # Your latitude
MY_LONG = 72.9780882  # Your longitude

api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "ACc70c1880e6fe872391a1dc933fb774e9"
auth_token = "00bd3ed5cdf16fed8078a4fc4fff5faf"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data['hourly'][0:12]

will_rain = False

for hour in hourly_data:
    weather = hour['weather']
    if weather[0]['id'] <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella ☂",
        from_='+13159020809',
        to='+919372914509'
    )
    print(message.status)



