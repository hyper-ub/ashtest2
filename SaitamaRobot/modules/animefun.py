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
    msg.reply_text(why)


@run_async
def fact(update: Update, context: CallbackContext):
    msg = update.effective_message
    fact = requests.get("https://nekos.life/api/v2/fact").json()
    fact = why.get("fact")  
    msg.reply_text(fact)


WHY_HANDLER = DisableAbleCommandHandler("why", why)
FACT_HANDLER = DisableAbleCommandHandler("fact", fact)

dispatcher.add_handler(FACT_HANDLER)
