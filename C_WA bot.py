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
    if not args:
      return await utils.answer(message, 'Нет аргумента')
    if not args.isdigit():
      return await utils.answer(message, 'Количество должно быть целым числом')
    await utils.answer(message, '🔄 Загрузка...')
    
    async with fsm.Conversation(app, "@clan_warsbot", True) as conv:
      await conv.ask('🏦 Ограбление банка (1 час)')
      await conv.get_response()
      await sleep(2)
      await conv.ask('🔍Найти подельников')
      response = await conv.get_response()
      await sleep(1)
      await conv.ask('🥷🏿Рейд')
      await conv.get_response()
      
      while True:
        history = app.get_history("@clan_warsbot", limit=1)
        if '🥷🏿Упаковываем оружие, гладим лыжные маски и выдвигаемся на дело. У нас есть всего один час, чтобы ограбить этот чёртов банк…' in history[0].text:
          break
        else:
          await sleep(2)
        
      await response.click()
      await get_response()
      for _ in range(int(args)):
        await conv.ask('💎 Бриллиантовая афера (3 часа)')
        await conv.get_response()
        await response.click()
        await conv.get_response()
      await message.delete()  
      await app.send_message(message.chat.id, '✅ CWA script ended')
      
