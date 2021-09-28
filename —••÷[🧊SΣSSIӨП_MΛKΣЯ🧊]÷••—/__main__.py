
"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""

import os
import logging
import asyncio
from pyromod import listen
from asyncio.exceptions import TimeoutError
from pyrogram import filters, Client, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import SessionPasswordNeeded, FloodWait,PhoneNumberInvalid, ApiIdInvalid,PhoneCodeInvalid, PhoneCodeExpired

"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""

async def exit_work(hn, text: str):
    if text.startswith("/exit"):
        await hn.reply("Process Cancelled.")
        return True
    return False

"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""


SERVER = os.environ.get('HEROKU')
if SERVER == "HEROKU":
    API_ID = os.environ.get('API_ID')
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
else:
    API_ID = 6372795
    API_HASH = "4b7731b0a6d8e15bef82863887feb293"
    BOT_TOKEN = "1977359439:AAEhXQJ_M8dgivEW8wCCve_jYsiQZlp7E-A"


"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""

HYPENAME = Client(
"—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—",
api_id=API_ID,
api_hash=API_HASH,
bot_token=BOT_TOKEN
)

"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""

PHONE_NUMBER_TEXT = """
Now send your Telegram account's Phone number in International Format.Including Country code. 
Example: **+919000000000**

ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.
"""

OTP =  """
÷•• ᴀɴ ᴏᴛᴘ ɪꜱ ꜱᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ

÷•• ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴏᴛᴘ ɪɴ `1 2 3 4 5` [**DO NOT FORGET SPACES IN BETWEEN**]

÷•• ɪꜰ 𝕡𝕪𝕣𝕠𝕘𝕣𝕒𝕞 ɴᴏᴛ ꜱᴇɴᴅɪɴɢ ᴏᴛᴘ ᴛʜᴇɴ ᴛʀʏ ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴛᴀꜱᴋ ᴀɢᴀɪɴ ᴡɪᴛʜ /start ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʙᴏᴛ.



ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.
"""

ZENO = "**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n"

MIB=InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]])

"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""


@HYPENAME.on_message(
filters.private
& filters.command("basic"))
async def genStr(client, hn: Message):
    try:
        await hn.delete()
        chat = hn.chat
        HYPE_ASK_API = await hn.reply_photo(
        photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
        caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


ɴᴏᴡ ꜱᴇɴᴅ ʏᴏᴜʀ `API_ID` ᴛᴏ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴘʏʀᴏɢʀᴀᴍ ꜱᴇꜱꜱɪᴏɴ ɴᴀᴍᴇ.


**ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴇɪᴛʜᴇʀ ᴏꜰ ᴛʜᴏꜱᴇ ᴛʜᴇɴ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ʙᴏᴛ**

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))


        HYPE_API = await HYPENAME.ask(
        chat.id,
        f"**÷••>**")


        await HYPE_ASK_API.delete()


        if await exit_work(hn, HYPE_API.text):
            return


        
        try:
            HYPE_API_CHECK = int(HYPE_API.text)
        except Exception:
            await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


`API_ID` ɪꜱ ɪɴᴠᴀʟɪᴅ.
ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return

        
        api_id = HYPE_API.text
        HYPE_ASK_HASK =  await hn.reply_photo(
        photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
        caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


ɴᴏᴡ ꜱᴇɴᴅ ʏᴏᴜʀ `API_HASH`.

ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))

        HYPE_HASH = await HYPENAME.ask(
        chat.id,
        f"**÷••>**")
        await HYPE_ASK_HASK.delete()
        await HYPE_API.delete()


        
        if await exit_work(hn, HYPE_HASH.text):
            return


        
        if not len(HYPE_HASH.text) >= 30:
            await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


🔴 ＣＯＤＥ－ＲＥＤ 🔴
`API_HASH` ɪꜱ ɪɴᴠᴀʟɪᴅ.
ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return



        
        api_hash = HYPE_HASH.text
        while True:
            number = await HYPENAME.ask(chat.id,PHONE_NUMBER_TEXT)
            if not number.text:
                continue
            if await exit_work(hn, number.text):
                return
            phone = number.text
            HYPE_ASK_Y = await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


ɪꜱ ```{phone}``` ᴄᴏʀʀᴇᴄᴛ? (y/n)

Ｓｅｎｄ： `y` 
or
Ｓｅｎｄ： `n` 

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))

            confirm = await HYPENAME.ask(
            chat.id,
            f"**÷••>**")
            await HYPE_HASH.delete()

            if await exit_work(hn, confirm.text):
                return
            if "y" in confirm.text:
                await  HYPE_ASK_Y.delete()
                await confirm.delete()
                break
            



        
        try:
            morphed = Client(
            "my_account",
            api_id=api_id,
            api_hash=api_hash
            )
        except Exception as e:
            await HYPENAME.send_photo(
            chat.id,
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            text=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`
ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return


        
        try:
            await morphed.connect()
        except ConnectionError:
            await morphed.disconnect()
            await morphed.connect()



        
        try:
            code = await morphed.send_code(phone)
        except FloodWait as e:
            await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


ʏᴏᴜ ʜᴀᴠᴇ ꜰʟᴏᴏᴅᴡᴀɪᴛ ᴏꜰ {e.x} ꜱᴇᴄᴏɴᴅꜱ

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return


        except ApiIdInvalid:
            await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


**ᴀᴘɪ ɪᴅ** ᴀɴᴅ **ᴀᴘɪ ʜᴀꜱʜ** ᴀʀᴇ ɪɴᴠᴀʟɪᴅ.

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return


        except PhoneNumberInvalid:
            await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪꜱ ɪɴᴠᴀʟɪᴅ.

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return



        
        try:
            HYPE_OTP = await HYPENAME.ask(
            chat.id,
            OTP,
            timeout=300)
        except TimeoutError:
            await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴ.

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return



          
        if await exit_work(hn, HYPE_OTP.text):
            return



        
        HYPE_otp_CODE = HYPE_OTP.text
        try:
            await morphed.sign_in(
            phone,
            code.phone_code_hash,
            phone_code=' '.join(str(HYPE_otp_CODE)))

        except PhoneCodeInvalid:
            await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
ɪɴᴠᴀʟɪᴅ ᴄᴏᴅᴇ.


ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return


        except PhoneCodeExpired:
            await hn.reply_photo(
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
ᴄᴏᴅᴇ ɪꜱ **𝐄𝐗𝐏𝐈𝐑𝐄𝐃** ᴏʀ ʏᴏᴜ ꜰᴏʀɢᴏᴛ ᴛᴏ **𝐏𝐔𝐓 𝐏𝐑𝐎𝐏𝐄𝐑 𝐒𝐏𝐀𝐂𝐄𝐒**

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return


        except SessionPasswordNeeded:
            try:
                await hn.reply_photo(
                photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
                caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴠᴇ **𝐓𝐰𝐨-𝐒𝐭𝐞𝐩 𝐕𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧.**
ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀꜱꜱᴡᴏʀᴅ.

ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
                HYPE_PASSCODE = await HYPENAME.ask(chat.id,f"**÷••>**",timeout=300)


            except TimeoutError:
                await hn.reply_photo(
                photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
                caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


`ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴ`

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.`

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
                return


        
            if await exit_work(hn,HYPE_PASSCODE.text):
                return



        
            HYPE_GOT_CODE = HYPE_PASSCODE.text
            try:
                await morphed.check_password(HYPE_GOT_CODE)
            except Exception as e:
                await hn.reply_photo(
                photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
                caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
                return

        
        except Exception as e:
            await HYPENAME.send_photo(
            chat.id,
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            text=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return


        try:
            SESSION_HYPED = await morphed.export_NAMER_MAKERion_string()
            await morphed.send_photo(
            "me",
            "https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ 𝘽𝙖𝙨𝙞𝙘 𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙎𝙚𝙨𝙨𝙞𝙤𝙣 𝙉𝙖𝙢𝙚:

```{SESSION_HYPED}```

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))


        
            await morphed.disconnect()
            await HYPENAME.send_photo(
            chat.id,
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


``𝘚𝘵𝘳𝘪𝘯𝘨 𝘨𝘦𝘯𝘦𝘳𝘢𝘵𝘪𝘰𝘯 𝘸𝘢𝘴 𝘚𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘤𝘰𝘮𝘱𝘭𝘦𝘵𝘦𝘥``

ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))


        
        except Exception as e:
            await HYPENAME.send_photo(
            chat.id,
            photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
            caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
            return



        
    except Exception as e:
        await HYPENAME.send_photo(
        chat.id,
        photo="https://telegra.ph/file/375f047a3252dd8f4d6d9.jpg",
        caption=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`

—••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••—
""",
    reply_markup = InlineKeyboardMarkup([[
    InlineKeyboardButton(
    text="🏷Group",
    url="https://t.me/Krakns"),],[
    InlineKeyboardButton(
    text="💰Channel",
    url="https://t.me/HYPEVOIDLAB"),],[
    InlineKeyboardButton(
    text="⚜️Dev+Git",
    url="https://t.me/KrakinzBot")
    ]]))
        return


"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""


from loguru import *
class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL: "CRITICAL",
        logging.ERROR: "ERROR",
        logging.WARNING: "WARNING",
        logging.INFO: "INFO",
        logging.DEBUG: "DEBUG"}
    def _get_level(self, record):
        return self.LEVELS_MAP.get(record.levelno, record.levelno)
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info, ansi=True, lazy=True)
        logger_opt.log(self._get_level(record), record.getMessage())
logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
LOGGER = logging.getLogger(__name__)

"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""

LOGGER.info("Starting")
HYPENAME.start()
LOGGER.info("\n\nStarted")
idle()
LOGGER.info("Stopping")
HYPENAME.stop()
LOGGER.info("\n\nStopped")

"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🧊SΣSSIӨП_MΛKΣЯ🧊]÷••— 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""