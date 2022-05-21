from asyncio import sleep
from pyrogram import Client, types
from .. import loader, utils, fsm

@loader.module(name="tq", author="ecXbe")
class TqMod(loader.Module):
  a = 0
  t = "qwertyuiop[]asdfghjkl;'\zxcvbnm,./ йцукенгшщзхъфывапролджэ\ячсмитьбю."
  
  @loader.on_bot(lambda self, app, message: message.text[0] in t)
  async def watcher(self, app: Client, message: types.Message):
    base = {"I've already said it all.", "He's listening to top tracks now", "My creator ponders the meaning of life", "AHAHAHAHAHAHAHAHA", "He's insane.", "Why exactly this fucker created me", "He may have turned off the sound.", "He's waiting for a message"}
    
    #if message.from_user.id == '2005298859':
     # self.app.send_message(message.chat.id, "Ooh ooh my creator, don't overdo it.")
    
    if message.chat.id == '726525996':
      app.send_message(message.chat.id, "Let's give it a try.")
      if a == 0:
        message.reply("My creator is a dumb idiot who only sits around depressed because of his personal communication, study problems. While you're bitching about @ecXbe, remember that he's sitting there right now, suffering and wondering why the fuck he even came into existence if everyone is bitching about him and everything is going through his ass. On May 12, 2022, he tried to slit his wrists but only left himself with a bruise and then pretended like nothing happened.")
        i += 1
      else:
        for i in base:
          message.reply(i)
