from asyncio import sleep

from pyrogram import Client, types, errors
from .. import loader, utils, inline, database, fsm, __version__

@loader.module(name="DownVideo", author="ecXbe")
class DdlMod(loader.Module):
  
  """Скачивает видео с ютуба и тиктока благодаря ботам"""
  
  async def ddl_cmd(self, app: Client, message: types.Message, args: str):
   
    """Использование -ddl <link/replay>"""
    
    reply = message.reply_to_message
    local = message.chat.id
    if args:
      if 'vm.tiktok.com' in args:
        await utils.answer(message, '🔄 Загрузка...')
        
        async with fsm.Conversation(app, "@SaveAsBot", True) as conv:
          await conv.ask(args)
          response = await conv.get_response()
          await response.forward(local)
      elif 'youtube.com' in args:
        await utils.answer(message, '🔄 Загрузка...')
        
        async with fsm.Conversation(app, "@youtubednbot", True) as conv:
          await conv.ask(args)
          response = await conv.get_response()
          await app.forward_message(local, message_id=response.message_id)
        
      else:
        return await utils.answer(message, 'Неподоходящая ссылка')
    else:
      if reply:
        return await utils.answer(message, 'It is reply')
      else:
        return await utils.answer(message, 'Нет аргумента и реплая')
