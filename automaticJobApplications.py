from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

EMAIL = "om.bhutki@somaiya.edu"
PASS = "Deanambrose3153"
chrome_path = Service("C:\\Users\\ombhu\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3282892510&f_AL=true&geoId=106164952&keywords=python"
           "%20developer&location=Mumbai%2C%20Maharashtra%2C%20India&refresh=true")
time.sleep(2)
sign_in_page = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_page.click()
time.sleep(2)
input_user = driver.find_element(By.ID, 'username')
input_user.send_keys(EMAIL)
input_pass = driver.find_element(By.ID, 'password')
input_pass.send_keys(PASS)
sign_in_btn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_btn.click()
time.sleep(2)
all_jobs = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for job in all_jobs:
    try:
        time.sleep(2)
        job.click()

    except ElementClickInterceptedException:
        save_toast = driver.find_element(By.CSS_SELECTOR,'.artdeco-toast-item')
        while save_toast is not None:
            cross_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-toast-item__dismiss')
            cross_button.click()
    finally:
        job.click()
        time.sleep(2)
        save_job = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
        save_job.click()

# all_job_links = [jobs.find_element(By.CSS_SELECTOR,'div div div div a').get_attribute('href') for jobs in all_jobs]
# print(all_jobs[0].find_element(By.CSS_SELECTOR,'div div div div a').get_attribute('href'))
# save_job = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div['
#                                          '1]/div[3]/div/button')
# save_job.click()
# company_name = driver.find_element(By.LINK_TEXT,'Uplers')
# company_name.click()
