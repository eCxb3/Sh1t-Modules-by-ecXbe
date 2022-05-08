from pyrogram import Client, types
from .. import loader, utils
import random

@loader.module("HAHA", "ecXbe")
class NotesMod(loader.Module):
  
  """Ржач полнейший, использовать -haha <кол-во/random>"""
  
  async def haha_cmd(self, app: Client, message: types.Message, args: str):
    reply = message.reply_to_message
    message.delete()
    hah = ['п', 'х', 'а', 'в', 'ф', 'ы'] # 22
    if args:
      if args.isdigit():
        for _ in range(int(args)):
          lol = "".join([random.choice(hah) for _ in range(random.randint(6, 22))])
          while 'пп' in lol or 'хх' in lol or 'аа' in lol or 'вв' in lol or 'фф' in lol or 'ыы' in lol:
            lol = lol.replace('пп', 'п').replace('хх', 'х').replace('аа', 'а').replace('вв', 'в').replace('фф', 'ф').replace('ыы', 'ы')
          if reply:
            await reply.reply(lol)
          else:
            await app.send_message(message.chat.id, lol)
      else:
        if args == "random":
          for _ in range(random.randint(2, 10)):
            lol = "".join([random.choice(hah) for _ in range(random.randint(6, 22))])
            while 'пп' in lol or 'хх' in lol or 'аа' in lol or 'вв' in lol or 'фф' in lol or 'ыы' in lol:
              lol = lol.replace('пп', 'п').replace('хх', 'х').replace('аа', 'а').replace('вв', 'в').replace('фф', 'ф').replace('ыы', 'ы')
            if reply:
              await reply.reply(lol)
            else:
              await app.send_message(message.chat.id, lol)
        else:
          return await utils.answer(message, 'Значение должно быть цифрой или значением random')
    else:
      return await utils.answer(message, 'Нет аргумента')
