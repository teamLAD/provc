from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAItmWD3OC0m03OLIcpSzfiJMCDxm4xJAAKFAwACH8C5V-U9VextES_XIAQ")
    await message.reply_text(
        f"""**ʜᴇʟʟᴏ [✅](https://telegra.ph/file/e52ea215ed4639a1b0c42.jpg) ᴀᴍ {bn}
𒐬𝙸 𝙰𝙼 𝙰𝙽 𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 𝚅𝙲 𝙱𝙾𝚃. 
𒐬𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙵𝙾𝚁 𝙵𝚁𝙴𝙴 𝙼𝚄𝚂𝙸𝙲.**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ", url="https://t.me/camillamusicbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url="https://t.me/teamladz_bothub"
                    ),
                    InlineKeyboardButton(
                        "ᴅᴇᴠ", url="https://t.me/alavalaathy"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "ᴀssɪsᴛ", url="https://t.me/ladz_vcplayer"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ alive✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/teamladz_bothub")
                ]
            ]
        )
   )
