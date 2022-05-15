from asyncio import sleep
from pyrogram import Client, types
from .. import loader, utils, fsm

@loader.module(name="DownVideo", author="ecXbe")
class DnlMod(loader.Module):
  
  """Скачивает видео с ютуба и тиктока благодаря ботам"""
  
  async def dnl_cmd(self, app: Client, message: types.Message, args: str):
   
    """Использование .dnl <link/replay>"""
    
    reply = message.reply_to_message
    local = message.chat.id
    if args:
      link = args
    elif reply:
      if not reply.text:
        return await utils.answer(message, '❌ В реплае нет текста')
      else:
        link = reply.text
    else:
      return await utils.answer(message, '❌ Нет аргумента и реплая')
    
    if 'tiktok.com' in link:
      await utils.answer(message, '🔄 Загрузка...')
        
      async with fsm.Conversation(app, "@downloader_tiktok_bot", True) as conv:
        try:
          await conv.ask(link)
        except:
          await app.unblock_user("@downloader_tiktok_bot")
          await conv.ask(link)
        try:
          response = await conv.get_response(60)
        except:
          return await utils.answer(message, '❌ Превышено время ожидания')
        await message.delete()
        if reply:
          await app.send_video(local, str(response.video.file_id), reply_to_message_id=message.reply_to_message_id)
        else:
          await app.send_video(local, str(response.video.file_id))
    elif 'youtube.com' in link or 'youtu.be' in link:
      await utils.answer(message, '🔄 Загрузка...')
        
      async with fsm.Conversation(app, "@youtubednbot", True) as conv:
        try:
          await conv.ask(link)
        except:
          await app.unblock_user("@youtubednbot")
          await conv.ask(link)
        try:
          response = await conv.get_response(60)
        except:
          return await utils.answer(message, '❌ Превышено время ожидания')
        await message.delete()
        if reply:
          await app.send_video(local, str(response.video.file_id), reply_to_message_id=message.reply_to_message_id)
        else:
          await app.send_video(local, str(response.video.file_id))
    else:
      return await utils.answer(message, '❌ Ссылка не найдена')

  @loader.on_bot(lambda self, app, message: "-dnl" in message.text)
  async def dlv_message_handler(self, app: Client, message: types.Message, args: str):
    
    reply = message.reply_to_message
    local = message.chat.id
    if args:
      link = args
    elif reply:
      if not reply.text:
        return await utils.answer(message, '❌ В реплае нет текста')
      else:
        link = reply.text
    else:
      return await utils.answer(message, '❌ Нет аргумента и реплая')
    
    if 'tiktok.com' in link:
      await utils.answer(message, '🔄 Загрузка...')
        
      async with fsm.Conversation(app, "@downloader_tiktok_bot", True) as conv:
        try:
          await conv.ask(link)
        except:
          await app.unblock_user("@downloader_tiktok_bot")
          await conv.ask(link)
        try:
          response = await conv.get_response(60)
        except:
          return await utils.answer(message, '❌ Превышено время ожидания')
        await message.delete()
        if reply:
          await app.send_video(local, str(response.video.file_id), reply_to_message_id=message.reply_to_message_id)
        else:
          await app.send_video(local, str(response.video.file_id))
    elif 'youtube.com' in link or 'youtu.be' in link:
      await utils.answer(message, '🔄 Загрузка...')
        
      async with fsm.Conversation(app, "@youtubednbot", True) as conv:
        try:
          await conv.ask(link)
        except:
          await app.unblock_user("@youtubednbot")
          await conv.ask(link)
        try:
          response = await conv.get_response(60)
        except:
          return await utils.answer(message, '❌ Превышено время ожидания')
        await message.delete()
        if reply:
          await app.send_video(local, str(response.video.file_id), reply_to_message_id=message.reply_to_message_id)
        else:
          await app.send_video(local, str(response.video.file_id))
    else:
      return await utils.answer(message, '❌ Ссылка не найдена')
