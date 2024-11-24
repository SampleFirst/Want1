import os
from pyrogram import Client, filters
from pyrogram.types import Message


PORT = int(os.getenv("PORT", 8080))
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Create a new Pyrogram client
app = Client(
    name=BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Start the bot
if __name__ == "__main__":
    app.run(port=PORT)
