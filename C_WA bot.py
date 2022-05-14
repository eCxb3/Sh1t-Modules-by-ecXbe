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

@loader.module(name="ClanWarsAuto", author="ecXbe")
class CwaMod(loader.Module):
  
  """Запустить cwa"""
  
  async def cwa_cmd(self, app: Client, message: types.Message, args: str):
    await utils.answer(message, '🔄 Загрузка...')
    
    async with fsm.Conversation(app, "@Testbot_testbot_botbot", True) as conv:
        await conv.ask('/random')
        res = await conv.get_response()
        await res.click()
        
  """ 
    async with fsm.Conversation(app, "@clan_warsbot", True) as conv:
      await conv.ask('🏦 Ограбление банка (1 час)')
      await conv.get_response()
      await conv.ask('🔍Найти подельников')
      response = await conv.get_response()
      await message.delete()
      try:
        await app.send_message(message.chat.id, response)
      except:
        print(response)
  """
