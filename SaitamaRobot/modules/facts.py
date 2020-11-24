#Made By @MadePranav
import html
import random
import requests
import os
import random
import nekos
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


@run_async
def fact(update: Update, context: CallbackContext):
    msg = update.effective_message
    fact = requests.get("https://nekos.life/api/v2/fact").json()
    fact = fact.get("fact")  
    msg.reply_text(fact)

FACT_HANDLER = DisableAbleCommandHandler("fact", fact)

dispatcher.add_handler (FACT_HANDLER)
