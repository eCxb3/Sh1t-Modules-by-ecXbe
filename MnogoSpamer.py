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
from .. import loader, utils

@loader.module(name="Mnogospam", author="ecXbe")
class MnogospamMod(loader.Module):
  """Спамер в многопотоке"""
  
  def spam_setting(self):
    for _ in range(self.count):
      self.app.send_message(self.message_chat_id, self.text)
    
  def spam_start(self)
    for _ in range(self.c):
      thh = threading.Thread(target=spam_setting)
      thh.start()

  async def mnspam(self, app: Client, message: types.Message, args: str):   # count, th. text
    
    args_ = args.split(maxsplit=3)
    if len(args_) != 3:
      return await utils.answer(message, 'Нехватает аргумета/ов')
    count = args_[0]
    th = args_[1]
    text = args_[2]
    c = round(count/th)
    self.count = count
    self.th = th
    self.text = text
    self.c = c
    self.app = app
    self.message_chat_id = message.chat.id
    
    await spam_start()
