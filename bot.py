from flask import Flask
from pyrogram import Client
import os

app = Flask(__name__)

# Pyrogram client
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_NAME = os.getenv("BOT_NAME")

client = Client(
    name=BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Flask route to start the bot
@app.route("/start", methods=["GET"])
def start_bot():
    client.start()
    return "Bot started successfully!"

# Flask route to stop the bot
@app.route("/stop", methods=["GET"])
def stop_bot():
    client.stop()
    return "Bot stopped successfully!"

# Flask route to handle requests to the root URL
@app.route("/", methods=["GET"])
def index():
    return "Your bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
