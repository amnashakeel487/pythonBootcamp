import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class InternetSpeedMonitor:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        self.down = 0
        self.up = 0

    def get_speed(self):

        self.driver.get("https://www.speedtest.net/")

        wait = WebDriverWait(self.driver, 20)

        try:
            consent = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "onetrust-accept-btn-handler")
                )
            )
            consent.click()
        except:
            pass

        start = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "start-text")
            )
        )

        start.click()

        print("Running Speed Test...")
        time.sleep(60)

        self.down = self.driver.find_element(
            By.CLASS_NAME,
            "download-speed"
        ).text

        self.up = self.driver.find_element(
            By.CLASS_NAME,
            "upload-speed"
        ).text

        print(f"Download: {self.down} Mbps")
        print(f"Upload: {self.up} Mbps")

    def close(self):
        self.driver.quit()