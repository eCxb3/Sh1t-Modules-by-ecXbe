from asyncio import sleep

from pyrogram import Client, types, errors
from .. import loader, utils, inline, database, fsm, __version__

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
        
        async with fsm.Conversation(app, "@SaveAsBot", True) as conv:
          await conv.ask(args)
          response = await conv.get_response()
          return response
        await app.send_message(local, response) 
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
