import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "om3153testing@gmail.com"
password = "eoitwohbjoyufptp"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                  "Safari/537.36 "

}
response = requests.get(url="https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS",
                        headers=headers)
response.raise_for_status()
amazon_web_age = response.text
soup = BeautifulSoup(amazon_web_age, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").getText().split(sep="$")[1])
message = "Subject:🔔Amazon Price Alert!🔔\n\n Instant Pot Duo 7-in-1 Electric Pressure Cooker,Slow Cooker, " \
          "Rice Cooker, " \
          "Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer,Includes App With Over 800 Recipes, Stainless Steel, " \
          "6 Quart is now at $80! Go buy it! https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp" \
          "/B00FLYWNYQ ".encode("utf-8")
if price <= 100.00:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=message)
