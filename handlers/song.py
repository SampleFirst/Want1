
from pyrogram import Client, filters
from pyrogram.types import Message
from youtube_search import YoutubeSearch
import yt_dlp
import os
import requests

def time_to_seconds(time):
    """Convert time string (hh:mm:ss) to seconds."""
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(":"))))

@Client.on_message(filters.command("song"))
async def find_song(client, message: Message):
    """Find and send a song."""
    query = " ".join(message.command[1:])
    if not query:
        await message.reply("**Please provide a song name to search.**")
        return

    m = await message.reply("**Searching for your song...**")
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            await m.edit("**No results found. Please try a different query.**")
            return

        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail_url = results[0]["thumbnails"][0]
        duration = results[0]["duration"]
        performer = "Music Finder"

        # Download thumbnail
        thumb_path = f"thumb_{title}.jpg"
        thumb_content = requests.get(thumbnail_url).content
        with open(thumb_path, "wb") as f:
            f.write(thumb_content)

        # Download song
        ydl_opts = {"format": "bestaudio[ext=m4a]", "outtmpl": f"{title}.m4a"}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            audio_file = ydl.prepare_filename(info_dict)

        await message.reply_audio(
            audio=open(audio_file, "rb"),
            title=title,
            duration=time_to_seconds(duration),
            performer=performer,
            thumb=thumb_path,
            caption=f"🎵 **[{title}]({link})**\n🔗 Powered by Music Finder Bot",
        )

        await m.delete()
        os.remove(audio_file)
        os.remove(thumb_path)
    except Exception as e:
        await m.edit("**An error occurred while processing your request.**")
        print(e)
