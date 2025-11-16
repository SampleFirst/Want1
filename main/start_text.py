from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="**Please Join My Both Updates Channel to use this Bot!**"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🔥 Join Updates Channel 🔥", url="https://youtube.com/@InvisibleYTV")
        ],[
        InlineKeyboardButton("🎉 Subscribe 🎉", url="https://t.me/+VnG269AYxSM3OGFl")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"hii 👋 {msg.from_user.mention}\ni am simple rename bot with personal usage."
    button= [[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]   
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "just send a file and /rename <new name> with replayed your file\n\n"
    txt += "send photo to set thumbnail automatic \n"
    txt += "/view to see your thumbnail \n"
    txt += "/del to delete your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 𝙲𝙻𝙾𝚂𝙴", callback_data="del"),
        InlineKeyboardButton("⬅️ 𝙱𝙰𝙲𝙺", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/iPepkornBots>𝚒𝙿𝚊𝚙𝚔𝚘𝚛𝚗𝙱𝚘𝚝𝚜</a>"  
    txt=f"<b>𝙱𝙾𝚃 𝙽𝙰𝙼𝙴 : {me.mention}\n𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : <a href=https://github.com/MrMKN>MrMKN</a>\n𝙱𝙾𝚃 𝚄𝙿𝙳𝙰𝚃𝙴 : <a href=https://t.me/iPapkon>𝚒𝙿𝚊𝚙𝚔𝚘𝚛𝚗</a>\n𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 : {Master}"                 
    button= [[        
        InlineKeyboardButton("🚫 𝙲𝙻𝙾𝚂𝙴", callback_data="del"),
        InlineKeyboardButton("⬅️ 𝙱𝙰𝙲𝙺", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


