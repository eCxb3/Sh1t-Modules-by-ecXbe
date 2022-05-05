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

@loader.module(name="TEST", author="ecXbe")
class ExampleMod(loader.Module):
  
  """dsfa"""
  
  async def testex_cmd(self, app: Client, message: types.Message, args: str):
  
    """ТЕСТ МОИХ МОДУЛЕЙ"""
    
    if args:
      count = message.text.split(' ')
      await utils.answer(message, len(count) + 1)
    else:
      await utils.answer(message, 'Нет аргументов')
