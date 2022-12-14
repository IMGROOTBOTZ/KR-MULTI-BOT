import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file
from helper.utils import not_subscribed
from helper.ban import BanChek

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**β οΈSorry bro,You didn't Joined Our Updates Channel Join now and start againπ**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=client.invitelink)
           ],[
           InlineKeyboardButton("π πππ’ π°ππππ π", url=f"https://t.me/{client.username}?start=start")            
           ]]
           )
       )

@Client.on_message(filters.private & filters.command(["tgmedia", "tgraph", "telegraph"]))
async def telegraph(client, message):
    kikked = await BanChek(client, message)
    if kikked == 400:
        return 
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return    
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    mkn=await message.reply_text(
        text="<code>Trying to processing please weit.....</code>",
        disable_web_page_preview=True
    )
    await asyncio.sleep(2)
    await mkn.delete()
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            text=f"<b>Link:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Oα΄α΄Ι΄ π LΙͺΙ΄α΄", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="SΚα΄Κα΄ π LΙͺΙ΄α΄", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
                [InlineKeyboardButton(text="β CΚα΄sα΄ β", callback_data="close")]
            ]
        )
    )
    finally:
        os.remove(download_location)
