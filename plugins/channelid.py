from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.utils import not_subscribed
from helper.ban import BanChek

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**โ ๏ธSorry bro,You didn't Joined Our Updates Channel Join now and start again๐**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="๐ข๐น๐๐๐ ๐ผ๐ข ๐๐๐๐๐๐ ๐ฒ๐๐๐๐๐๐๐ข", url=client.invitelink)
           ],[
           InlineKeyboardButton("๐ ๐๐๐ข ๐ฐ๐๐๐๐ ๐", url=f"https://t.me/{client.username}?start=start")            
           ]]
           )
       )

@Client.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    kikked = await BanChek(motech, msg)
    if kikked == 400:
        return 
    if msg.forward_from:
        text = "<b><u>๐๐ข๐ฅ๐ช๐๐ฅ๐ ๐๐ก๐๐ข๐ฅ๐ ๐๐ง๐๐ข๐ก ๐</u></b> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<b><u>๐ค Bแดแด Iษดาแด</u></b>"
        else:
            text += "<b><u>๐คUsแดส Iษดาแด</u></b>"
        text += f'\n\n๐จโ๐ผ ๐๐๐ฆ๐ : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\n๐ ๐๐ฌ๐๐ซ๐๐๐ฆ๐ : @{msg.forward_from["username"]} \n\n๐ ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\n๐ ๐๐ : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"โ๏ธ๐๐ซ๐ซ๐จ๐ซ <b><i>{hidden}</i></b> โ๏ธ๐๐ซ๐ซ๐จ๐ซ",
                quote=True,
            )
        else:
            text = f"<b><u>๐๐ข๐ฅ๐ช๐๐ฅ๐ ๐๐ก๐๐ข๐ฅ๐ ๐๐ง๐๐ข๐ก ๐</u></b>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<b><u>๐ข Cสแดษดษดแดส</u></b>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<b><u>๐ฃ๏ธ Gสแดแดแด</u></b>"
            text += f'\n\n๐ ๐๐๐ฆ๐ : {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\nโก๏ธ ๐๐ซ๐จ๐ฆ : @{msg.forward_from_chat["username"]}'
                text += f'\n\n๐ ๐๐ : `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\n๐ ๐๐ `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
