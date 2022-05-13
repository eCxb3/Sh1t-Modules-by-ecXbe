from asyncio import sleep

from aiogram.types import (
    InlineQuery,
    CallbackQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from pyrogram import Client, types
from .. import loader, utils, inline, database, fsm, __version__

@loader.module(name="CWA", author="ecXbe")
class CwaMod(loader.Module):
  
  """Запустить c_wa"""
  
  async cwa_cmd(self, app: Client, message: types.Message, args: str):
    await utils.answer(message, '🔄 Загрузка...')
    
    async with fsm.Conversation(app, "@clan_warsbot", True) as conv:
      await conv.ask('🏦 Ограбление банка (1 час)')
      await conv.get_response()
      await conv.ask('🔍Найти подельников')
      response = await conv.get_respose()
      await message.delete()
      await app.send_message(message.chat.id, response)
      print(response)
      
