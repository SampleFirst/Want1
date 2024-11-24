import os
from flask import Flask
from pyrogram import Client

# Create Flask app
app = Flask(__name__)

# Ensure the app listens on the correct port
@app.route('/')
def home():
    return 'Bot is running!'

# Initialize the Telegram Bot
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
client = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.route('/start')
def start():
    return 'Bot is running on Render!'

if __name__ == "__main__":
    # Get PORT from environment variable or default to 5000
    port = int(os.getenv("PORT", 5000))
    
    # Start the Flask server to keep the app alive
    app.run(host="0.0.0.0", port=port)
    
    # Start the bot
    client.run()
