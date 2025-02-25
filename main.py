print("Hello, Instagram-Bot läuft!")
import instaloader
import os
from dotenv import load_dotenv

# .env Datei laden
load_dotenv()

# Instagram-Login
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

bot = instaloader.Instaloader()

try:
    bot.login(USERNAME, PASSWORD)
    print("✅ Erfolgreich bei Instagram eingeloggt!")
except Exception as e:
    print(f"❌ Fehler beim Login: {e}")
