from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
from dotenv import load_dotenv
from os import streror
import os
import sys

# Write element from dropdown that you want to scrape
Body = sys.argv[1]


def configure():
    load_dotenv()


class SelectCar:

    PATH = Service(f'{os.getenv("path_chrom_browser")}')
    driver = webdriver.Chrome(service=PATH)
    url = 'https://www.autovit.ro'
    driver.get(url)
    driver.maximize_window()

    @staticmethod
    def accept_cookies():
        # Agree to cookie
        WebDriverWait(SelectCar.driver, 20).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))).click()

    @staticmethod
    def select_body():
        global Body

        SelectCar.accept_cookies()

        caroserie = WebDriverWait(SelectCar.driver, 5).\
            until(EC.presence_of_element_located((By.ID, 'filter_enum_body_type')))

        caroserie.click()
        sleep(1)
        if Body:
            WebDriverWait(SelectCar.driver, 5).\
                until(EC.presence_of_element_located((By.XPATH, f"// span[text() = '{Body}']"))).click()
            # Select all cars button
            WebDriverWait(SelectCar.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ooa-1ys84iq"))).click()
            sleep(3)

        # Get the URL for make filtering
        filtered_url = SelectCar.driver.current_url

        SelectCar.driver.quit()
        return filtered_url


obj = SelectCar()
try:
    
    with open(r'C:\Users\itelescu\Documents\Scrapy_test\crawling_project\crawling_project\spiders\parser_link.txt', 'w')\
            as file:
        f_link = file.write(obj.select_body())
except Exception as exep:
    print('Error occured: ', strerror(exep.errno))
