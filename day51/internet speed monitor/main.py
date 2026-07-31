from internet_speed import InternetSpeedMonitor
from config import PROMISED_DOWN, PROMISED_UP

bot = InternetSpeedMonitor()

bot.get_speed()

download = float(bot.down)
upload = float(bot.up)

print("\nExpected Download:", PROMISED_DOWN)
print("Expected Upload:", PROMISED_UP)

if download < PROMISED_DOWN or upload < PROMISED_UP:
    print("\n⚠️ Internet speed is lower than promised.")
    print("You can now manually report this to your ISP.")
else:
    print("\n✅ Internet speed meets the promised values.")

bot.close()