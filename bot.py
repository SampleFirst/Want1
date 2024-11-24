
from pyrogram import Client
import os

# Import handlers
from handlers.song import find_song
from handlers.video import find_video

# Bot Configuration
API_ID = os.getenv("API_ID", "your_api_id")  # Replace with your actual API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with your actual API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Replace with your bot token

# Initialize the bot
app = Client(
    "music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Add handlers
app.add_handler(find_song)
app.add_handler(find_video)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()
