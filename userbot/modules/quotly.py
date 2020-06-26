import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.q(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Balas Pesan Manapun Untuk Membuat Stiker.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Balas ke Pesan Text ```")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    await event.edit("```Membuat Stiker Dari Pesan Teks (Quotly by Luqman)..```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Tolong unblock @QuotLyBot dan Coba Lagi```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.delete()   
             await bot.forward_messages(event.chat_id, response.message)

CMD_HELP.update({
        "quotly": 
        ".q \
          \nUsage: Enhance ur text to sticker.\n"
    })
