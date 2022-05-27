from asyncio import sleep
from pyrogram import Client, types, filters
from .. import loader, utils, fsm

@loader.module("MuteB", "ecXbe")
class MutebMod(loader.Module):
    """Типо блокирует пользователя"""
    
    async def muteb_cmd(self, app: Client, message: types.Message, args: str):
        """Включить/выключить"""
        chats = self.db.get("MuteB", "chats", [])
        g_chat = message.chat.id in chats
        
        self.db.set("MuteB", "chats", list({*chats} ^ {message.chat.id}))
        return await utils.answer(message, (
        "Грустные медузы..., она похожа на ..." if g_chat
        else "Весёлые медузы зазаза, она похожа на арбузы зузузу"
        ))
    
    @loader.on(~filters.me)
    async def watcher(self, app: Client, message: types.Message):
        """Принт"""
        if message.chat.id in self.db.get("MuteB", "chats", []):
            video = await app.get_messages(-1001636732080, 5695)
            return await app.send_video(message.chat.id, str(video.video.file_id))
