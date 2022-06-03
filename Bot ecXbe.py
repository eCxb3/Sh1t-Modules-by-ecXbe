from asyncio import sleep
from pyrogram import Client, types, filters
from .. import loader, utils, fsm
from random import randint, choice
from aiogram.utils.markdown import hlink
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

@loader.module(name="ecxbeBOT", author="ecXbe")
class ExbotMod(loader.Module):
  
  @loader.on_bot(lambda self, app, message: message.text[:4] == "/dnl")
  async def dnl_message_handler(self, app: Client, message: Message):
    
    args_ = message.text.split(maxsplit=1)
    if len(args_) == 2:
      args = args_[1]
    else:
      args = False
    
    reply = message.reply_to_message
    local = message.chat.id
    if args != False:
      link = args
    elif reply:
      if not reply.text:
        return await message.reply('❌ В реплае нет текста')
      else:
        link = reply.text
    else:
      return await message.reply('❌ Нет аргумента и реплая')

    if 'tiktok.com' in link:
      loading = await message.reply(text="🔄 Загрузка...")
        
      async with fsm.Conversation(app, "@downloader_tiktok_bot", True) as conv:
        try:
          await conv.ask(link)
        except:
          await app.unblock_user("@downloader_tiktok_bot")
          await conv.ask(link)
        try:
          response = await conv.get_response(60)
        except:
          return await self.bot.edit_message_text(message_id=loading.message_id, chat_id=message.chat.id, text='❌ Превышено время ожидания')
        bt = await app.send_video('@sh1tub_8VVd1k_bot', video=str(response.video.file_id))
        await sleep(1)
        await loading.delete()
        
        await message.delete()
        await self.bot.send_video(message.chat.id, video=str(bt.video.file_id), caption=f"Скачано по ссылке: {link}\n Пользователем: <a href=\"tg://user?id={message.from_user.id}\">{utils.get_display_name(message.from_user)}</a>")
        await bt.delete()
    elif 'youtube.com' in link or 'youtu.be' in link:
      loading = await message.reply(text="🔄 Загрузка...")
        
      async with fsm.Conversation(app, "@youtubednbot", True) as conv:
        try:
          await conv.ask(link)
        except:
          await app.unblock_user("@youtubednbot")
          await conv.ask(link)
        try:
          response = await conv.get_response(60)
        except:
          return await self.bot.edit_message_text(message_id=loading.message_id, chat_id=message.chat.id, text='❌ Превышено время ожидания')
        bt = await app.send_video('@sh1tub_8VVd1k_bot', video=str(response.video.file_id))
        await sleep(1)
        await loading.delete()
        
        await message.delete()
        await self.bot.send_video(message.chat.id, video=str(bt.video.file_id), caption=f"Скачано по ссылке: {link}\n Пользователем: <a href=\"tg://user?id={message.from_user.id}\">{utils.get_display_name(message.from_user)}</a>")
        await bt.delete()
    else:
      return await message.reply('❌ Ссылка не найдена')
    
    
  @loader.on_bot(lambda self, app, message: message.text[:4] == "/ben")
  async def ben_message_handler(self, app: Client, message: Message):
    
    def say_ben():
      ben = randint(1, 4)
      if ben == 1:
        return "Й"+"Е"*randint(1,3)+"С"
      elif ben == 2:
        return "ОХ"*randint(2, 4)+"ОУ"
      elif ben == 3:
        return "Н"+"О"*randint(1, 3)+"У"*randint(1,2)
      elif ben == 4:
        return "БУ"+"Э"*randint(2,5)
    
    args_ = message.text.split(maxsplit=1)
    if len(args_) == 2:
      args = args_[1]
    else:
      args = False
    reply = message.reply_to_message  
    
    if args != False:
      ben = say_ben()
      return await message.reply(ben)
    elif reply:
      ben = say_ben()
      return await reply.reply(ben)
    else:
      return await message.reply("Р"*randint(3,7))

  @loader.on_bot(lambda self, app, message: message.text[:7] == "/random")
  async def random_message_handler(self, app: Client, message: Message):
    args_ = message.text.split(maxsplit=1)
    if len(args_) == 2:
      args = args_[1]
    else:
      args = False 
    
    if args != False:
      args = args.split("//")
      index = 0
      for x in args:
        args[index] = x.strip()
        index += 1
      await message.reply(choice(args))
    else:
      return await message.reply("❌ Отсутствует список")
    
  @loader.on_bot(lambda self, app, message: message.text[:8] == "/randint")
  async def rand_message_handler(self, app: Client, message: Message):
    args_ = message.text.split(maxsplit=1)
    if len(args_) == 2:
      args = args_[1]
    else:
      args = False 

    if args != False:
      if args.find(":") == -1:
        return await message.reply("❌ Отсутствует разделительный знак \":\"")
      range = args.split(":")
      index = 0
      for x in range:
        range[index] = x.strip()
        index += 1
      if range[0].isdigit() == False or range[1].isdigit() == False:
        return await message.reply("❌ Диапазон должен быть целыми числами")
      if int(range[0]) > int(range[1]):
        return await message.reply("❌ Первое число должно быть меньше второго")
      return await message.reply(randint(int(range[0]), int(range[1])))  
    else:
      return await message.reply("❌ Отсутствует диапазон")
