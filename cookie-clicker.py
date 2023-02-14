
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_exe_path = Service("C:\\Users\\ombhu\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_exe_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, 'cookie')

items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute('id') for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5
ten_min = time.time() + 60 * 10
while True:

    cookie.click()
    if time.time() > timeout:
        raw_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        item_prices = []
        for raw_price in raw_prices:
            raw_text = raw_price.text
            if raw_text != "":
                item_price = int(raw_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(item_price)

        upgrade_items = {}

        for items in range(len(item_prices)):
            upgrade_items[item_prices[items]] = item_ids[items]

        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        affordable_items = {}
        for cost, _id in upgrade_items.items():
            if cost < cookie_count:
                affordable_items[cost] = _id

        most_expensive_affordable_item = max(affordable_items)
        print(most_expensive_affordable_item)
        most_expensive_affordable_item_id = affordable_items[most_expensive_affordable_item]
        item_to_purchase = driver.find_element(By.ID, most_expensive_affordable_item_id)

        item_to_purchase.click()
        timeout = time.time() + 20

