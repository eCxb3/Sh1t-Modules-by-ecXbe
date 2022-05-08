from pyrogram import Client, types
from .. import loader, utils


@loader.module("Switcher", "ecXbe")
class SwitcherMod(loader.Module):
  
  """Меняет раскладку сообщения при случайном написании сообщения на другой раскладке"""
  
  async def switch_cmd(self, app: Client, message: types.Message, args: str):
    Ru = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    En = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
    
    reply = message.reply_to_message
    if reply:
      if not reply.text:
        return await utils.answer(message, 'Нет текста в реплае')
      change = str.maketrans(RuKeys + EnKeys, EnKeys + RuKeys)
      text = str.translate(reply.text, change)
      if message.from_user.id != reply.from_user.id:
        return await utils.answer(message, text)
      else:
        await message.delete()
        return await utils.answer(reply, text)
    else:
      if args:
        change = str.maketrans(Ru + En, En + Ru)
        text = str.translate(args, change)
        return await utils.answer(message, text)
      else:
        return await utils.answer(message, """Нет реплая и аргумента, использование -switch <replay/text>""")
