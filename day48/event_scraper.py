from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

for event in events:
    print(event.text)

driver.quit()