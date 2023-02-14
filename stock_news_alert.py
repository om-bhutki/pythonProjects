import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
all_items = None
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def stock_price():
    global all_items
    api_key = "EA6YTG6X0NH9GD0V"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": api_key,

    }
    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()
    all_items = list(data['Time Series (Daily)'].items())
    yesterday_stock = float(all_items[0][1]['4. close'])
    day_before_yesterday_stock = float(all_items[1][1]['4. close'])
    percent = ((yesterday_stock - day_before_yesterday_stock) / day_before_yesterday_stock) * 100

    return percent


# noinspection PyUnresolvedReferences
def get_news():
    global all_items
    apikey = "5d5c788cdab745c8affdb7547e0ecc65"
    parameters = {
        "q": COMPANY_NAME,
        "from": all_items[7][0],
        "to": all_items[6][0],
        "sortBy": "popularity",
        "pageSize": 3,
        "apikey": apikey,
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data = response.json()
    news_list = [{"Headline": news['title'], "Brief": news['description'], } for news in data['articles']]
    return news_list


account_sid = "ACc70c1880e6fe872391a1dc933fb774e9"
auth_token = "00bd3ed5cdf16fed8078a4fc4fff5faf"

price = round(stock_price())
top_news = get_news()
if stock_price() >= 5 or stock_price() <= -5:
    if stock_price() <= -5:
        price_down = str(price)
        price = f"TSLA: {price_down.replace('-', '')}%🔻"
    else:
        price = f"TSLA: {price}%🔺"
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{price}\n Headline: {top_news[0]['Headline']}\n Brief: {top_news[0]['Brief']}",
        from_='+13159020809',
        to='+919372914509'
    )

    message2 = client.messages \
        .create(
        body=f"{price}\n Headline: {top_news[1]['Headline']}\n Brief: {top_news[1]['Brief']}",
        from_='+13159020809',
        to='+919372914509'
    )
    message3 = client.messages \
        .create(
        body=f"{price}\n Headline: {top_news[2]['Headline']}\n Brief: {top_news[2]['Brief']}",
        from_='+13159020809',
        to='+919372914509'
    )
    print(message.status)
    print(message2.status)
    print(message3.status)

