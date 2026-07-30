from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

# --------------------------
# Load Environment Variables
# --------------------------
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# --------------------------
# Chrome Setup
# --------------------------
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 20)

# --------------------------
# Open LinkedIn Login Page
# --------------------------
driver.get("https://www.linkedin.com/login")

# --------------------------
# Login
# --------------------------
email = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

print("Logged in successfully.")

# Give time if CAPTCHA appears
input("If LinkedIn asks for CAPTCHA or verification, solve it and press ENTER...")

# --------------------------
# Open Jobs Page
# --------------------------
driver.get("https://www.linkedin.com/jobs/")

# --------------------------
# Search Jobs
# --------------------------
job_box = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search by title, skill, or company']"))
)

job_box.clear()
job_box.send_keys("Python Developer")

location_box = driver.find_element(
    By.CSS_SELECTOR,
    "input[aria-label='City, state, or zip code']"
)

location_box.clear()
location_box.send_keys("London")
location_box.send_keys(Keys.ENTER)

print("Searching jobs...")

time.sleep(5)

# --------------------------
# Collect Jobs
# --------------------------
jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")

print(f"\nFound {len(jobs)} jobs\n")

for index, job in enumerate(jobs, start=1):
    try:
        title = job.find_element(By.CSS_SELECTOR, ".job-card-list__title").text
    except:
        title = "Unknown"

    try:
        company = job.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__subtitle").text
    except:
        company = "Unknown"

    print(f"{index}. {title}")
    print(f"   Company: {company}")
    print("-" * 50)

print("\nFinished.")

driver.quit()