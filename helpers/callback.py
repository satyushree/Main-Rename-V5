import logging
logger = logging.getLogger(__name__)

from main import *
from ..config import Config
from pyrogram import Client as RenameBot, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserBannedInChannel, UserNotParticipant


################## Callback for help button ##################

@RenameBot.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()
    await help(c, m, True)


################## Callback for donate button ##################

@RenameBot.on_callback_query(filters.regex('^donate$'))
async def donate(c, m):
    button = [[
        InlineKeyboardButton("Hom"', callback_data='back'),
        InlineKeyboardButton("About", callback_data='about')
        ],[
        InlineKeyboardButton("Close", callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    await m.answer()
    await m.message.edit(
        text=Config.DONATE_USER.format(m.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


################## Callback for close button ##################

@RenameBot.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


################## Callback for home button ##################

@RenameBot.on_callback_query(filters.regex('^back$'))
async def back_cb(c, m):
    await m.answer()
    await start(c, m, True)


################## Callback for about button ##################

@RenameBot.on_callback_query(filters.regex('^about$'))
async def about_cb(c, m):
    await m.answer()
    await about(c, m, True)
