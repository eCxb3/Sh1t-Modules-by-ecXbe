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
          if response.media == 'video':
            message.delete()
            await app.send_video(local, str(response.video.file_id))
          else:
            response = await self.app.get_history(self.chat_id, limit=2)
            message.delete()
            await app.send_video(local, str(response[1].video.file_id))
      elif 'youtube.com' in args:
        await utils.answer(message, '🔄 Загрузка...')
        
        async with fsm.Conversation(app, "@youtubednbot", True) as conv:
          await conv.ask(args)
          response = await conv.get_response()
          message.delete()
          await app.send_video(local, str(response.video.file_id))
        
      else:
        return await utils.answer(message, 'Ссылка не найдена')
    else:
      if reply:
        return await utils.answer(message, 'It is reply')
      else:
        return await utils.answer(message, 'Нет аргумента и реплая')
