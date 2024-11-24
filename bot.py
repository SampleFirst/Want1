import os
from flask import Flask
from pyrogram import Client
from plugins.song import song_command
from plugins.video import video_command

app = Flask(__name__)

# Set environment variables for API and Bot Token
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# Create the Pyrogram client (Telegram bot)
bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Home route to keep the Flask app alive
@app.route('/')
def home():
    return 'Bot is running!'

# Register song and video commands
bot.add_handler(song_command)
bot.add_handler(video_command)

# Start the bot in Flask to keep it running
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if no PORT is provided
    bot.run()  # Start the Pyrogram bot
    app.run(host="0.0.0.0", port=port)  # Start Flask to keep the app alive
