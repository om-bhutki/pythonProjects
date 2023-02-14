import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 19.218330  # Your latitude
MY_LONG = 72.9780882  # Your longitude


def is_iss_close():
    response_1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_1.raise_for_status()
    data_1 = response_1.json()

    iss_latitude = float(data_1["iss_position"]["latitude"])
    iss_longitude = float(data_1["iss_position"]["longitude"])

    diff_lat = round(iss_latitude - MY_LAT)
    diff_lng = round(iss_longitude - MY_LONG)

    if diff_lat in range(-5, 6) and diff_lng in range(-5, 6):
        return True


# Your position is within +5 or -5 degrees of the ISS position.

def is_it_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour
    if sunset <= hour_now <= sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

my_email = "om3153testing@gmail.com"
password = "eoitwohbjoyufptp"
while True:
    time.sleep(60)
    if is_it_night() and is_iss_close():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="roronoazoro3153@gmail.com",
                                msg="Subject:👆👆ISS IS OVER YOU!!👆👆\n\nLook up iss is passing by!"
                                )

