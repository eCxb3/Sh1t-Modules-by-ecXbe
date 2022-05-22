from asyncio import sleep
from pyrogram import Client, types, filters
from .. import loader, utils, fsm

@loader.module("MuteB", "ecXbe")
class MutebMod(loader.Module):
    """Типо блокирует пользователя"""
    
    async def muteb_cmd(self, app: Client, message: types.Message, args: str):
        """Включить/выключить"""
        chats = self.db.get("MuteB", "chats", [])

        self.db.set("MuteB", "chats", list({*chats} ^ {message.chat.id}))
        return await message.delete()
    
    @loader.on(~filters.me)
    async def watcher(self, app: Client, message: types.Message):
        """Принт"""
        if message.chat.id in self.db.get("MuteB", "chats", []):
            return await utils.answer(message, "Пользователь добавил вас в чёрный список. Походу вы ему чем-то насолили")
    
    async def mutebc_cmd(self, app: Client, message: types.Message, args: str):
        
        chats = self.db.get("MuteBot", "botc", {})
        if not chats.get(str(chat.id)):
            chats[str(chat.id)] = 0
            self.db.set("MuteBot", "botc", chats)
            return await utils.answer(
                message, "Bot started, creator sad inside")

        del chats[str(chat.id)]
        self.db.set("MuteBot", "botc", chats)
        return await utils.answer(
                message, "Bot finished, creator sad inside")
   
    @loader.on(~filters.me)
    async def muteb_message_handler(self, app: Client, message: types.Message):
        base = {"I've already said it all.", "He's listening to top tracks now", "My creator ponders the meaning of life", "AHAHAHAHAHAHAHAHA", "He's insane.", "Why exactly this fucker created me", "He may have turned off the sound.", "He's waiting for a message"}
        if message.chat.id in self.db.get("MuteBot", []):
            if message.from_user.id == 2005298859:
                return await message.reply("Ooh ooh my creator, don't overdo it.")
            else:
                if self.db.get("MuteB", "botc", message.chat.id) == 0:
                    return await message.reply("My creator is a dumb idiot who only sits in depression because of personal communication, study problems. While you're fucking about @ecXbe, remember that he's sitting there right now, suffering and wondering why the fuck he even came into existence if everyone is fucking about him and everything is going through his ass. On the night of May 12-13, 2022, he tried to slit his wrists, but only got away with a bruise and then pretended it never happened.")
                    botc = self.db.get("MuteBot", "botc")
                    self.db.set("MuteBot", "botc", list({*botc} ^ {message.chat.id: 1}))
                else:
                    for i in base:
                        return await message.reply(i)
