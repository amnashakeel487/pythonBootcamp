from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config import TARGET_URL
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 10)

driver.get(TARGET_URL)

text_box = wait.until(
    EC.presence_of_element_located((By.NAME, "my-text"))
)

text_box.send_keys("Day 50 Selenium Automation")

password = driver.find_element(By.NAME, "my-password")
password.send_keys("password123")

textarea = driver.find_element(By.NAME, "my-textarea")
textarea.send_keys("Learning Selenium WebDriver!")

submit = driver.find_element(By.CSS_SELECTOR, "button")

time.sleep(2)
submit.click()

print("Form submitted successfully!")

time.sleep(3)

driver.quit()