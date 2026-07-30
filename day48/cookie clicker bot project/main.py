from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")

end_time = time.time() + 30

while time.time() < end_time:
    cookie.click()

print("Finished clicking!")

driver.quit()