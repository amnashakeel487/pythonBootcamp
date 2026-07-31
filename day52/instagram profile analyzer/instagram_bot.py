from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class InstagramProfileAnalyzer:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        self.wait = WebDriverWait(self.driver, 20)

    def open_profile(self, username):
        self.driver.get(f"https://www.instagram.com/{username}/")

    def get_profile_info(self):
        try:
            header = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "header"))
            )
            print("Profile page loaded successfully.")
            print(header.text)
        except Exception as e:
            print("Could not retrieve profile information:", e)

    def close(self):
        self.driver.quit()