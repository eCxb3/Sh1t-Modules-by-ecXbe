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
        except errors.UserIsBlocked:
          await self._app.unblock_user("@downloader_tiktok_bot")
          await conv.ask(link)
        response = await conv.get_response()
        await message.delete()
        await app.send_video(local, str(response.video.file_id))
    elif 'youtube.com' in link or 'youtu.be' in link:
      await utils.answer(message, '🔄 Загрузка...')
        
      async with fsm.Conversation(app, "@youtubednbot", True) as conv:
        try:
          await conv.ask(link)
        except errors.UserIsBlocked:
          await self._app.unblock_user("@youtubednbot")
          await conv.ask(link)
        response = await conv.get_response()
        await message.delete()
        await app.send_video(local, str(response.video.file_id))
    else:
      return await utils.answer(message, '❌ Ссылка не найдена')
