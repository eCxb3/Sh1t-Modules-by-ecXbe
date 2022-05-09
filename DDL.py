from asyncio import sleep

from pyrogram import Client, types
from .. import loader, utils, inline

@loader.module(name="DownVideo", author="ecXbe")
class DdlMod(loader.Module):
  
  """Скачивает видео с ютуба и тиктока благодаря ботам"""
  
  async def ddl_cmd(self, app: Client, message: types.Message, args: str):
   
    """Использование -ddl <link/replay>"""
    
    reply = message.reply_to_message
    
    if args:
      local = message.chat.id
      if 'vm.tiktok.com' in args:
        await utils.answer(message, '🔄 Загрузка...')
        await app.send_message(523131145, args)
      
      elif 'youtube.com' in args:
        await utils.answer(message, '🔄 Загрузка...')
        await app.send_message(1482008667, args)
      else:
        return await utils.answer(message, 'Неподоходящая ссылка')
    else:
      if reply:
        return await utils.answer(message, 'It is reply')
      else:
        return await utils.answer(message, 'Нет аргумента и реплая')
      
  async def watcher(self, app: Client, message: types.Message, video: types.Video):
    if message.chat.id == 523131145:
      global local
      await utils.answer(message, 'Получил видео')
      await app.send_message(local, 'Получил видео')
      await app.forward_message(local, message_id=video.file_id)
