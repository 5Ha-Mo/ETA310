import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/727e6b2141a3656ef0262.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@ETALEE0"
)

CAPTION = f"**سرعة البنج:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/E4V4ER")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
