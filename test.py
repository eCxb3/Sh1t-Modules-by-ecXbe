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
from .. import loader, utils, inline

@loader.module(name="Example", author="sh1tn3t", version=1)
class ExampleMod(loader.Module):
  
  """dsfa"""
  
  async def testex_cmd(self, app: Client, message: types.Message, args: str):
  
    """ТЕСТ МОИХ МОДУЛЕЙ"""
    
    if args:
      count = message.split(' ') # -fc 10 hi 78 hello
      await utils.answer(message, len(count) + 1)
    else:
      await utils.answer(message, 'Нет аргументов')
