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
        return await utils.answer(message, "Весёлые медузы нарара, они похожи на арбузы нарара")
    
    @loader.on(~filters.me)
    async def watcher(self, app: Client, message: types.Message):
        """Принт"""
        if message.chat.id in self.db.get("MuteB", "chats", []):
            return await app.send_video(message.chat.id, "BAACAgIAAx0EYY6MsAACFj9ikH-2u901yj1K4sLyGkYo4QlLdAACchYAApzWiEgh-qigp-UKnR4E")
