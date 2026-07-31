from instagram_bot import InstagramProfileAnalyzer
from config import TARGET_PROFILE

bot = InstagramProfileAnalyzer()

bot.open_profile(TARGET_PROFILE)
bot.get_profile_info()

input("Press Enter to close the browser...")

bot.close()