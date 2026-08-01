from scraper import ZillowScraper
from form_filler import FormFiller


scraper = ZillowScraper()

addresses, prices, links = scraper.scrape()

print(addresses)
print(prices)
print(links)

bot = FormFiller()

bot.fill_form(
    addresses,
    prices,
    links
)