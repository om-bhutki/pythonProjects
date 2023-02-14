import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_PATH = "C:\\Users\\ombhu\\Development\\chromedriver.exe"
TARGET = "bepis.man"
EMAIL = "zoro_drippy"
PASSWORD = "i7FiHCOdw$G@f7u"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(executable_path=CHROME_PATH))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        user = self.driver.find_element(By.NAME, 'username')
        user.send_keys(EMAIL)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        btn.click()
        time.sleep(5)
        dont_save = self.driver.find_element(By.CSS_SELECTOR, '._ac8f button')
        dont_save.click()
        time.sleep(2)
        notifications = self.driver.find_element(By.CSS_SELECTOR, '._a9--._a9_1')
        notifications.click()
        time.sleep(3)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET}/")
        time.sleep(10)
        followers = self.driver.find_element(By.CSS_SELECTOR, '._aa_5 a')
        followers.click()
        time.sleep(5)
        followers_container = self.driver.find_element(By.CSS_SELECTOR, '._aano div div button')
        for n in range(500):
            followers_container.send_keys(Keys.END)
        time.sleep(20)

    def follow(self):
        follow_btns = self.driver.find_elements(By.CSS_SELECTOR, '._aano div div button')
        for btns in follow_btns:
            try:
                btns.click()
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.CSS_SELECTOR,'._a9--._a9_1')
                cancel_btn.click()
            finally:
                time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
