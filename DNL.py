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

  
  
  
  @loader.on_bot(lambda self, app, message: message.text[:4] == "-dnl")
  async def dlv_message_handler(self, app: Client, message: types.Message):
    
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
        
        video_cap_text = "Скачано по ссылке: "+link+"\nПользователем: "+message.from_user.first_name+"(@"+message.from_user.username+")"
        await message.delete()
        await self.bot.send_video(message.chat.id, video=str(bt.video.file_id), caption=video_cap_text)
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
        
        video_cap_text = "Скачано по ссылке: "+link+"\nПользователем: "+message.from_user.first_name+"(@"+message.from_user.username+")"
        await message.delete()
        await self.bot.send_video(message.chat.id, video=str(bt.video.file_id), caption=video_cap_text)
        await bt.delete()
    else:
      return await message.reply('❌ Ссылка не найдена')

    
    
  @loader.on_bot(lambda self, app, message: "@ecXbe" in message.text)
  async def tq_message_handler(self, app: Client, message: types.Message):
    base = {"I've already said it all.", "He's listening to top tracks now", "My creator ponders the meaning of life", "AHAHAHAHAHAHAHAHA", "He's insane.", "Why exactly this fucker created me", "He may have turned off the sound.", "He's waiting for a message"}
    
    #if message.from_user.id == '2005298859':
     # self.app.send_message(message.chat.id, "Ooh ooh my creator, don't overdo it.")
    
    if message.chat.id == '726525996':
      if self.a == 0:
        message.reply("My creator is a dumb idiot who only sits in depression because of personal communication, study problems. While you're fucking about @ecXbe, remember that he's sitting there right now, suffering and wondering why the fuck he even came into existence if everyone is fucking about him and everything is going through his ass. On the night of May 12-13, 2022, he tried to slit his wrists, but only got away with a bruise and then pretended it never happened.")
        i += 1
      else:
        for i in base:
          message.reply(i)
