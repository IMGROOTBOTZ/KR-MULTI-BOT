import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from variables import FORCE_SUB


async def BanChek(bot: Client, cmd: Message):
    if not FORCE_SUB:
      return False
    try:
        user = await bot.get_chat_member(chat_id=(int(FORCE_SUB) if FORCE_SUB.startswith("-100") else FORCE_SUB), user_id=cmd.from_user.id)                 
        if user.status == "banned":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="β οΈ**ππΎπππ π³ππ³π΄ ππΎπ π°ππ΄ π±π°π½π½π΄π³ \nπ°π²π²π΄ππ π³π΄π½πΈπ΄π³ β οΈ π²πΎπ½ππ°π²π [πππΏπΏπΎππ πΆππΎππΏ](https://t.me/KR_Join)**",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:                
        return 400
    except Exception:        
        return 400
    return 200
