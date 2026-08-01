import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import FORM_URL


class FormFiller:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

    def fill_form(self, addresses, prices, links):

        for address, price, link in zip(
                addresses,
                prices,
                links
        ):

            self.driver.get(FORM_URL)

            time.sleep(2)

            inputs = self.driver.find_elements(
                By.CSS_SELECTOR,
                "input[type='text']"
            )

            inputs[0].send_keys(address)
            inputs[1].send_keys(price)
            inputs[2].send_keys(link)

            submit = self.driver.find_element(
                By.CSS_SELECTOR,
                "div[role='button']"
            )

            submit.click()

            time.sleep(1)