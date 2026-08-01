from bs4 import BeautifulSoup
from config import *

class ZillowScraper:

    def __init__(self):
        self.addresses = []
        self.prices = []
        self.links = []

    def scrape(self):


        with open("data/zillow.html", "r", encoding="utf-8") as file:
            website = file.read()

        soup = BeautifulSoup(website, "lxml")

        listings = soup.select(".StyledPropertyCardDataWrapper")

        for listing in listings:

            try:
                address = listing.select_one(
                    "address"
                ).get_text().strip()

                link = listing.select_one(
                    "a"
                )["href"]

                price = listing.select_one(
                    ".PropertyCardWrapper__StyledPriceLine"
                ).get_text().split("+")[0]

                self.addresses.append(address)
                self.links.append(link)
                self.prices.append(price)

            except AttributeError:
                pass

        return self.addresses, self.prices, self.links