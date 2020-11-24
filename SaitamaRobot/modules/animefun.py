#AnimeFun Module Made By @madepranav on telegram and github id @darkpokefan

import requests
import html
import BulmaRobot.modules.animequotesstring as animequotesstring
import random
import re
import rapidjson as json
import nekos
import urllib.request
import urllib.parse
from typing import List
from PIL import Image
import os

from telegram import Update, Bot, ParseMode
from telegram.ext import run_async
from telegram.utils.helpers import escape_markdown

from BulmaRobot import dispatcher
from BulmaRobot.modules.disable import DisableAbleCommandHandler
from BulmaRobot.modules.helper_funcs.extraction import extract_user


@run_async
def nep(bot: Bot, update: Update):
    msg = update.effective_message
    target = "neko"
    msg.reply_photo(nekos.img(target))

@run_async
def baka(bot: Bot, update: Update):
    msg = update.effective_message
    target = "baka"
    msg.reply_video(nekos.img(target))

@run_async
def smug(bot: Bot, update: Update):
    msg = update.effective_message
    target = "smug"
    msg.reply_video(nekos.img(target))

@run_async
def kiss(bot: Bot, update: Update):
    msg = update.effective_message
    target = "kiss"
    msg.reply_video(nekos.img(target))

@run_async
def holo(bot: Bot, update: Update):
    msg = update.effective_message
    target = "holo"
    msg.reply_photo(nekos.img(target))

@run_async
def poke(bot: Bot, update: Update):
    msg = update.effective_message
    target = "poke"
    msg.reply_video(nekos.img(target))

@run_async
def feed(bot: Bot, update: Update):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))

@run_async
def tickle(bot: Bot, update: Update):
    msg = update.effective_message
    target = "tickle"
    msg.reply_video(nekos.img(target))

@run_async
def nepgif(bot: Bot, update: Update):
    msg = update.effective_message
    target = "ngif"
    msg.reply_video(nekos.img(target))

@run_async
def wallpaper(bot: Bot, update: Update):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))

@run_async
def slap(bot: Bot, update: Update):
    msg = update.effective_message
    target = "slap"
    msg.reply_photo(nekos.img(target))
    
@run_async
def patgif(bot: Bot, update: Update):
    msg = update.effective_message
    target = "pat"
    msg.reply_video(nekos.img(target))


@run_async
def goose(bot: Bot, update: Update):
    msg = update.effective_message
    target = "goose"
    msg.reply_photo(nekos.img(target))


@run_async
def why(bot: Bot, update: Update):
    msg = update.effective_message
    why = requests.get("https://nekos.life/api/v2/why").json()
    why = why.get("why")
    msg.reply_text(why)
    

@run_async
def pat(bot: Bot, update: Update):
    chat_id = update.effective_chat.id
    msg = str(update.message.text)
    try:
        msg = msg.split(" ", 1)[1]
    except IndexError:
        msg = ""
    msg_id = update.effective_message.reply_to_message.message_id if update.effective_message.reply_to_message else update.effective_message.message_id
    pats = []
    pats = json.loads(urllib.request.urlopen(urllib.request.Request(
    'http://headp.at/js/pats.json',
    headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) '
         'Gecko/20071127 Firefox/2.0.0.11'}
    )).read().decode('utf-8'))
    if "@" in msg and len(msg) > 5:
        bot.send_photo(chat_id, f'https://headp.at/pats/{urllib.parse.quote(random.choice(pats))}', caption=msg)
    else:
        bot.send_photo(chat_id, f'https://headp.at/pats/{urllib.parse.quote(random.choice(pats))}', reply_to_message_id=msg_id)
        
@run_async
def animequotes(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(animequotesstring.ANIMEQUOTES))
   
__help__ = """
 - /animequotes : for random Anime qoutes.
 - /nep : for random Anime Image.
 - /baka: for random Baka Shout GIFs.
 - /smug: for random Smug GIFs.
 - /kiss: for random Anime Kiss GIFs.
 - /holo: for random Anime holo GIFs.
 - /poke: for random Anime poke GIFs
 - /feed: for random Anime feeding GIFs.
 - /tickle: for random Anime tickle GIFs.
 - /nepgif: for random Anime GIFs.
 - /wallpaper : for random Anime Wallpaper.
 - /slap : for random Anime slap gif.
 - /patgif : for random Anime pat gif.
 - /pat: for random Anime pat image.
 - /wall <query> to get wallpaper
 - /goose : for random duck image.
"""
    

NEP_HANDLER = DisableAbleCommandHandler("nep", nep)
BAKA_HANDLER = DisableAbleCommandHandler("baka", baka)
SMUG_HANDLER = DisableAbleCommandHandler("smug", smug)
KISS_HANDLER = DisableAbleCommandHandler("kiss", kiss)
HOLO_HANDLER = DisableAbleCommandHandler("holo", holo)
POKE_HANDLER = DisableAbleCommandHandler("poke", poke)
FEED_HANDLER = DisableAbleCommandHandler("feed", feed)
TICKLE_HANDLER = DisableAbleCommandHandler("tickle", tickle)
NEPGIF_HANDLER = DisableAbleCommandHandler("nepgif", nepgif)
WALLPAPER_HANDLER = DisableAbleCommandHandler("wallpaper", wallpaper)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)
PATGIF_HANDLER = DisableAbleCommandHandler("patgif", patgif)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat, admin_ok=True)
ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)
PATGIF_HANDLER = DisableAbleCommandHandler("patgif", patgif)
GOOSE_HANDLER = DisableAbleCommandHandler("goose", goose)
WHY_HANDLER = DisableAbleCommandHandler("why", why)

dispatcher.add_handler(NEP_HANDLER)
dispatcher.add_handler(BAKA_HANDLER)
dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(HOLO_HANDLER) 
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(NEPGIF_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(PATGIF_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(GOOSE_HANDLER)
dispatcher.add_handler(ANIMEQUOTES_HANDLER)
dispatcher.add_handler(WHY_HANDLER)

__handlers__ = [
    NEP_HANDLER, BAKA_HANDLER, SMUG_HANDLER, KISS_HANDLER, HOLO_HANDLER, POKE_HANDLER, FEED_HANDLER,
TICKLE_HANDLER, NEPGIF_HANDLER, WALLPAPER_HANDLER, SLAP_HANDLER,PATGIF_HANDLER, GOOSE_HANDLER, WHY_HANDLER,
]

__mod_name__ = "NEPTUNEFUN"
