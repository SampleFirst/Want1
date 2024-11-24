
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch
import yt_dlp
import os
import requests

async def advanced_search(query, max_results=1):
    """Perform advanced YouTube search."""
    search = VideosSearch(query, limit=max_results)
    results = await search.next()
    return results["result"]

@Client.on_message(filters.command(["video", "movie", "trailer"]))
async def find_video(client, message: Message):
    """Find and send a video."""
    query = " ".join(message.command[1:])
    if not query:
        await message.reply("**Please provide a video/movie name to search.**")
        return

    m = await message.reply("**Searching for your video...**")
    try:
        results = await advanced_search(query, max_results=1)
        if not results:
            await m.edit("**No results found. Please try a different query.**")
            return

        video_data = results[0]
        link = video_data["link"]
        title = video_data["title"]
        duration = video_data["duration"]
        thumbnail_url = video_data["thumbnails"][0]["url"]

        # Download thumbnail
        thumb_path = f"thumb_{title}.jpg"
        thumb_content = requests.get(thumbnail_url).content
        with open(thumb_path, "wb") as f:
            f.write(thumb_content)

        # Download video
        ydl_opts = {
            "format": "best",
            "outtmpl": f"{title}.mp4",
            "quiet": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            video_file = f"{title}.mp4"

        await client.send_video(
            message.chat.id,
            video=open(video_file, "rb"),
            caption=f"🎬 **[{title}]({link})**\n🔗 Powered by Video Finder Bot",
            thumb=thumb_path,
            supports_streaming=True,
        )

        await m.delete()
        os.remove(video_file)
        os.remove(thumb_path)
    except Exception as e:
        await m.edit("**An error occurred while processing your request.**")
        print(e)
