import html
from PIL import Image
import requests
import os
import random
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


@run_async
def animewall(update: Update, context: CallbackContext):
    msg = update.effective_message
    anime = requests.get("https://api.computerfreaker.cf/v1/anime").json()
    url = anime.get("url")  
    msg.reply_photo(url)

ANIMEWALL_HANDLER = DisableAbleCommandHandler("animewall", animewall)

dispatcher.add_handler(ANIMEWALL_HANDLER)
