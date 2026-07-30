import requests
import smtplib

from bs4 import BeautifulSoup
from config import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}

response = requests.get(PRODUCT_URL, headers=headers)

response.raise_for_status()

print(response.status_code)

with open("amazon.html", "w", encoding="utf-8") as file:
    file.write(response.text)


soup = BeautifulSoup(response.text, "lxml")

title = soup.find(id="productTitle").get_text().strip()

price = soup.find(class_="a-offscreen").get_text()

price = price.replace("$", "").replace(",", "")

current_price = float(price)

print(title)
print(current_price)

if current_price < TARGET_PRICE:

    message = f"""
Subject:Amazon Price Alert!

{title}

Price dropped to ${current_price}

{PRODUCT_URL}
"""

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:

        connection.starttls()

        connection.login(
            EMAIL,
            PASSWORD
        )

        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER,
            msg=message.encode("utf-8")
        )

print("Done")