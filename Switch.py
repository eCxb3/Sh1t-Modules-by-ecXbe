from pyrogram import Client, types
from .. import loader, utils


@loader.module("Switcher", "ecXbe")
class SwitcherMod(loader.Module):
  
  """Меняет раскладку сообщения при случайном написании сообщения на другой раскладке"""
  
  async def switch_cmd(self, app: Client, message: types.Message, args: str):
    RuKeys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    EnKeys = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
    
    reply = message.reply_to_message
    if reply:
      utils.answer(message, reply)
    else:
      if args:
        utils.answer(message. args)
      else:
        return utils.answer(message, 'Нет реплая и аргумента,   использование -switch <replay/text>')
