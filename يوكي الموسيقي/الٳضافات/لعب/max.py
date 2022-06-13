import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مطور السورس","مكس","ماكس"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.postimg.cc/Gpsy08WJ/IMG-20220506-232324-397.jpg",
        caption=f"""- مبرمج سورس مكس .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مڪس", url=f"https://t.me/l_Mix_1"),
                ],
            ]
        ),
    )
