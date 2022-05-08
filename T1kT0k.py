from asyncio import sleep
import json, io, re
import urllib.parse

from requests import head,get
from pyrogram import Client, types
from .. import loader, utils

@loader.module(name="TikTok", author="ecXbe & Sairos")
class TiktokMod(loader.Module):
  
  """Скачивает видео с тик ток"""
  
  async def tiktok_cmd(self, app: Client, message: types.Message, args: str):
    
    """Использовать -tiktok <ссылка на видео>"""
    
    reply = message.reply_to_message
    
    if args:
      if 'vm.tiktok.com' not in args:
        return await utils.answer(message, 'Не вижу ссылку')
      await utils.answer(message, '🔄 Загрузка')
      video = await get_tiktok_video(args)
      
      try:
        await message.delete()
        await app.send_file(message.chat.id, file=G)
      except:
        try:
          await utils.answer(message, '⬇️ Скачивание')
          H = get(G).content
          E = io.BytesIO(H)
          E.name = 'video.mp4'
          E.seek(0)
          await message.delete()
          await app.send_message(message.chat.id, file=E)
        except:
          return await utils.answer(message, '❌ Я не могу скачать это видео')
    else:
      if reply:
        if not reply.text:
          return await utils.answer(message, 'В реплае нет текста')
      else:
        return await utils.answer(message, 'Нет аргумента и реплая')


      
async def get_tiktok_video(link):
  async def fvideo(video_id, _):
    full_link = "https://api-va.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{video_id}%5D"
    full_link = get(full_link)
    details = full_link.json().get('aweme_details')
    
    if not details:
      return 0, 0, full_link
    return details, True, full_link
  
  headheaders = head(full_link).headers
  headheaders = full_link.get('Location')
  try:
    query = parse_qs(urlsplit(headheaders).query)
    item_id = query.get('share_item_id')[0]
    G, C, D = await fvideo(item_id, 1)
    if not C:
      raise
  except:
    a = ''.join(re.findall('[0-9]', urlsplit(headheaders).path.split('/')[-1]))
    G, C, D = await fvideo(a, 2)
    if not C:
      return False, D
    
    return G[0]['video']['bit_rate'][0]['play_addr']['url_list'][-1], D
