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
def why(update: Update, context: CallbackContext):
    msg = update.effective_message
    why = requests.get("https://nekos.life/api/v2/why").json()
    why = why.get("why")  
    msg.reply_photo(why)

WHY_HANDLER = DisableAbleCommandHandler("why", why)

dispatcher.add_handler(WHY_HANDLER)
