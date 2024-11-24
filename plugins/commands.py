from pyrogram import Client, filters

# /start command handler
async def start_command(client, message):
    if message.command[0] == "start":
        await message.reply(
            "Hello! I am your bot. How can I assist you today? Type /help to get a list of available commands."
        )

# /help command handler
async def help_command(client, message):
    if message.command[0] == "help":
        help_text = """
        Here are the available commands:

        /start - Start the bot
        /help - List available commands
        /about - Get information about this bot
        /song <song name> - Search and download a song
        /video <video name> - Search and download a video
        """
        await message.reply(help_text)

# /about command handler
async def about_command(client, message):
    if message.command[0] == "about":
        about_text = """
        This bot is built to help you search and download songs, videos, and movies.
        Developed by [Your Name/Your Organization].
        """
        await message.reply(about_text)
