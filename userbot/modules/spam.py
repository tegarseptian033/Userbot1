# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

import asyncio
from asyncio import wait, sleep

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register
from telethon.tl.functions.users import GetFullUserReques



@register(pattern=".whois(?: |$)(.*)", outgoing=True)
async def who(event):

    await event.edit(
        "`Sit tight while I steal some data from Mark Zuckerburg...`")

    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)

    replied_user = await get_user(event)

    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        event.edit("`Could not fetch info of that user.`")
        return

    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.client.send_file(event.chat_id,
                                     photo,
                                     caption=caption,
                                     link_preview=False,
                                     force_document=False,
                                     reply_to=message_id_to_reply,
                                     parse_mode="html")

        if not photo.startswith("http"):
            os.remove(photo)
        await event.delete()

    except TypeError:
        await event.edit(caption, parse_mode="html")


async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(
                GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return replied_user


async def fetch_info(replied_user, event):
    """ Get details from the User object. """
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.user.id,
                             offset=42,
                             max_id=0,
                             limit=80))
    replied_user_profile_photos_count = "Person needs help with uploading profile picture."
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError as e:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = "Couldn't fetch DC ID!"
        location = str(e)
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(user_id,
                                                      TEMP_DOWNLOAD_DIRECTORY +
                                                      str(user_id) + ".jpg",
                                                      download_big=True)
    first_name = first_name.replace(
        "\u2060", "") if first_name else ("This User has no First Name")
    last_name = last_name.replace(
        "\u2060", "") if last_name else ("This User has no Last Name")
    username = "@{}".format(username) if username else (
        "This User has no Username")
    user_bio = "This User has no About" if not user_bio else user_bio


    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Ambil Pistol")
        await asyncio.sleep(0.3)
        await e.edit("Arahin Pala Sendiri")
        await asyncio.sleep(0.2)
        await e.edit("Tembak")
        await asyncio.sleep(0.5)
        await e.edit("Jeder!")
        await asyncio.sleep(0.2)
        await e.edit("Meninggal")
        await asyncio.sleep(0.3)
        await e.edit("ditembak")
        await asyncio.sleep(0.3)
        await e.edit("diri sendiri")
        await asyncio.sleep(0.3)
        await e.edit("Aku Mati Bunuh Diri pake Pestol")

@register(outgoing=True, pattern="^.kill$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        


@register(outgoing=True, pattern="^.cspam (.*)")
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#CSPAM\n"
            "TSpam was executed successfully")


@register(outgoing=True, pattern="^.wspam (.*)")
async def tmeme(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#WSPAM\n"
            "WSpam was executed successfully")


@register(outgoing=True, pattern="^.spam (.*)")
async def spammer(e):
    counter = int(e.pattern_match.group(1).split(' ', 1)[0])
    spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
    await e.delete()
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    if BOTLOG:
        await e.client.send_message(BOTLOG_CHATID, "#SPAM\n"
                                    "Spam was executed successfully")


@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    message = e.text
    text = message.split()
    counter = int(text[1])
    link = str(text[2])
    await e.delete()
    for i in range(1, counter):
        await e.client.send_file(e.chat_id, link)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#PICSPAM\n"
            "PicSpam was executed successfully")


@register(outgoing=True, pattern="^.delayspam (.*)")
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#DelaySPAM\n"
            "DelaySpam was executed successfully")

@register(outgoing=True, pattern="^.gangsta$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("EVERyBOdy")
        await asyncio.sleep(0.3)
        await e.edit("iZ")
        await asyncio.sleep(0.2)
        await e.edit("GangSTur")
        await asyncio.sleep(0.5)
        await e.edit("UNtIL ")
        await asyncio.sleep(0.2)
        await e.edit("I")
        await asyncio.sleep(0.3)
        await e.edit("ArRivE")
        await asyncio.sleep(0.3)
        await e.edit("🔥")
        await asyncio.sleep(0.3)
        await e.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥")

@register(outgoing=True, pattern="^.bunuhdiri")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Ambil Pistol")
        await asyncio.sleep(0.3)
        await e.edit("Arahin Pala Sendiri")
        await asyncio.sleep(0.2)
        await e.edit("Tembak")
        await asyncio.sleep(0.5)
        await e.edit("Jeder!")
        await asyncio.sleep(0.2)
        await e.edit("Meninggal")
        await asyncio.sleep(0.3)
        await e.edit("ditembak")
        await asyncio.sleep(0.3)
        await e.edit("diri sendiri")
        await asyncio.sleep(0.3)
        await e.edit("Aku Mati Bunuh Diri pake Pestol")

@register(outgoing=True, pattern="^.kill$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Target")
        await asyncio.sleep(0.3)
        await e.edit("Terkunci")
        await asyncio.sleep(0.2)
        await e.edit("Tembak")
        await asyncio.sleep(0.5)
        await e.edit("Jeder!")
        await asyncio.sleep(0.2)
        await e.edit("Meninggal")
        await asyncio.sleep(0.3)
        await e.edit("kena")
        await asyncio.sleep(0.3)
        await e.edit("AWM")
        await asyncio.sleep(0.3)
        await e.edit("Aku Menembaknya Headshot Dengan AWM {first_name}\n")

@register(outgoing=True, pattern="^.upro$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("EVERyBOdy")
        await asyncio.sleep(0.3)
        await e.edit("iZ")
        await asyncio.sleep(0.2)
        await e.edit("PrO")
        await asyncio.sleep(0.5)
        await e.edit("UNtIL ")
        await asyncio.sleep(0.2)
        await e.edit("U")
        await asyncio.sleep(0.3)
        await e.edit("ArRivE")
        await asyncio.sleep(0.3)
        await e.edit("🔥")
        await asyncio.sleep(0.3)
        await e.edit("EVERyBOdy iZ PrO UNtIL U ArRivE 🔥")

@register(outgoing=True, pattern="^.repo")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await asyncio.sleep(0.5)
        await e.edit("InI")
        await asyncio.sleep(0.3)
        await e.edit("AdalaH")
        await asyncio.sleep(0.5)
        await e.edit("RePo")
        await asyncio.sleep(0.5)
        await e.edit("Dari ")
        await asyncio.sleep(0.3)
        await e.edit("Bod")
        await asyncio.sleep(0.2)
        await e.edit("Ini")
        await asyncio.sleep(0.2)
        await e.edit("🔥")
        await asyncio.sleep(0.3)
        await e.edit("Klik [Disini](https://github.com/luqmanvps/Userbot1) Untuk Melihat Repo Bot Ini🔥") 


@register(outgoing=True, pattern="^.gitdev")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("InI")
        await asyncio.sleep(0.3)
        await e.edit("AdalaH")
        await asyncio.sleep(0.5)
        await e.edit("GITHUB")
        await asyncio.sleep(0.5)
        await e.edit("Dari ")
        await asyncio.sleep(0.3)
        await e.edit("Developer")
        await asyncio.sleep(0.5)
        await e.edit("Bod")
        await asyncio.sleep(0.2)
        await e.edit("Ini 🔥")
        await asyncio.sleep(0.5)
        await e.edit("[Dev Bot Ini](https://github.com/luqmanvps)") 




CMD_HELP.update({
    "spam":
    ".cspam <text>\
\nUsage: Spam the text letter by letter.\
\n\n.spam <count> <text>\
\nUsage: Floods text in the chat !!\
\n\n.wspam <text>\
\nUsage: Spam the text word by word.\
\n\n.picspam <count> <link to image/gif>\
\nUsage: As if text spam was not enough !!\
\n\n.delayspam <delay> <count> <text>\
\nUsage: .bigspam but with custom delay.\
\n\n\nNOTE : Spam at your own risk !!"
})
