import html

from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html

from SaitamaRobot import (DEV_USERS, LOGGER, OWNER_ID, DRAGONS, DEMONS, TIGERS,
                          WOLVES, dispatcher)
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import (bot_admin, connection_status,
                                                           user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user_and_text
from SaitamaRobot.modules.helper_funcs.string_handling import extract_time
from SaitamaRobot.modules.log_channel import gloggable, loggable
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, run_async)


@run_async
@connection_status
@bot_admin
@user_admin
@loggable


async def zombies(show, update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    """ For /zombies command, list all the ghost/deleted/zombie accounts in a chat. """
    bot = context.bot
    args = context.args

    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`No deleted accounts found, Group is clean`"

    if con != "clean":
        await show.edit("`Searching for ghost/deleted/zombie accounts...`")
        async for user in show.client.iter_participants(show.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"`Found` **{del_u}** ghost/deleted/zombie account(s) in this group,\
            \nclean them by using `.zombies clean`"
        await show.edit(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit("`I am not an admin here!`")
        return

    await show.edit("`Deleting deleted accounts...\nOh I can do that?!?!`")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await show.edit("`I don't have ban rights in this group`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    await show.edit(del_status)
    await sleep(2)
    await show.delete()

    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            "#CLEANUP\n"
            f"Cleaned **{del_u}** deleted account(s) !!\
            \nCHAT: {show.chat.title}(`{show.chat_id}`)",
        )

@run_async
@connection_status
@bot_admin
@user_admin
@loggable

async def rm_deletedacc(show):
    bot = context.bot
    args = context.args
    if show.fwd_from:
        return
    con = show.pattern_match.group(1)
    """ For .zombies command, list all the ghost/deleted/zombie accounts in a chat. """

    del_u = 0
    del_status = "`No deleted accounts found, Group is clean`"

    if con != "clean":
        avengers = await show.reply("`Searching for ghost/deleted/zombie accounts...`")
        await asyncio.sleep(2)
        await avengers.delete()
        async for user in show.client.iter_participants(show.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"`Found` **{del_u}** ghost/deleted/zombie account(s) in this group,\
            \nclean them by using `.zombies clean`"
        await show.reply(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.reply("`I am not an admin here!`")
        return

    avengers2 = await show.reply("`Deleting deleted accounts...\nOh I can do that?!?!`")
    await asyncio.sleep(2)
    await avengers2.delete()
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await show.reply("`I don't have ban rights in this group`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    avengers3 = await show.reply(del_status)
    await sleep(2)
    await avengers3.delete()


ZOMBIES_HANDLER = CommandHandler("zombies", zombies)

dispatcher.add_handler(ZOMBIES_HANDLER)

__help__ = """
   /zombies :- remove deleted accounts
"""
__mod_name__ = "Zombies"

__handlers__ = [
    ZOMBIES_HANDLER
]
