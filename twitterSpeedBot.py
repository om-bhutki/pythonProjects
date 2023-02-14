import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TWT_EMAIL = "tmz31531234@gmail.com"
TWT_PASSWORD = " "
PROMISED_UP = 50
PROMISED_DOWN = 50
CHROME_PATH = "C:\\Users\\ombhu\\Development\\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_PATH))
        self.up = 0.0
        self.down = 0.0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # cross_button = self.driver.find_element(By.CSS_SELECTOR,'.onetrust-close-btn-handler')
        # cross_button.click()
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]'
                                                '/a/span[4]')
        go.click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                             '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                             '2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                           '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                           '2]/span').text)
        print(f"down: {self.down}\nup: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(6)
        sign_in = self.driver.find_element(By.LINK_TEXT, 'Sign in')
        sign_in.click()
        time.sleep(6)
        email = self.driver.find_element(By.NAME, 'text')
        email.send_keys(TWT_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(10)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWT_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = f"Hey Internet Provider,why is my internet speed {self.down}down/{self.up}up when i pay " \
                f"for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_btn = self.driver.find_elements(By.TAG_NAME, 'a')
        tweet_btn[9].click()
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, '.DraftEditor-editorContainer div')
        tweet_input.send_keys(tweet)
        tweet_btn = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div['
                                                      '3]/div/div/div[2]/div[4]')
        tweet_btn.click()
        self.driver.quit()
#FixTheDamnWifi

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.up < 50 or bot.down < 50:
    bot.tweet_at_provider()
