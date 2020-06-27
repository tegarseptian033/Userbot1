# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

import asyncio
from asyncio import wait, sleep

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register


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

@register(outgoing=True, pattern="^.nikal$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Nikal")
        await asyncio.sleep(0.3)
        await e.edit("lavde")
        await asyncio.sleep(0.2)
        await e.edit("pehli")
        await asyncio.sleep(0.5)
        await e.edit("fursat")
        await asyncio.sleep(0.2)
        await e.edit("me")
        await asyncio.sleep(0.3)
        await e.edit("nikal")
        await asyncio.sleep(0.3)
        await e.edit("🤬")
        await asyncio.sleep(0.3)
        await e.edit("Nikal lavde pehli fursat me nikal 🤬")


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
        
        
        
@register(outgoing=True, pattern="^.kill")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Scope")
        await asyncio.sleep(1.5)
        await e.edit("Arahin Pala")
        await asyncio.sleep(0.7)
        await e.edit("Tembak")
        await asyncio.sleep(0.3)
        await e.edit("Jeder!")
        await asyncio.sleep(0.3)
        await e.edit("Meninggal")
        await asyncio.sleep(0.3)
        await e.edit("Headshot")
        await asyncio.sleep(0.3)
        await e.edit("pake")
        await asyncio.sleep(0.3)
        await e.edit("AWM")
        await asyncio.sleep(0.3)
        await e.edit("Dia, Mati ku-Headshot pake AWM")


@register(outgoing=True, pattern="^.repo")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Ini")
        await asyncio.sleep(0.3)
        await e.edit("Adalah")
        await asyncio.sleep(0.5)
        await e.edit("Repo")
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











