from pyrogram import Client, types, filters
from .. import loader, utils


@loader.module("MuteB", "sh1tn3t")
class MutebMod(loader.Module):
    """Типо блокирует пользователя"""

    async def muteb_cmd(self, app: Client, message: types.Message, args: str):
        """Включить/выключить"""
        chats = self.db.get("MuteB", "chats", [])
        echo_status = message.chat.id in chats

        self.db.set("MuteB", "chats", list({*chats} ^ {message.chat.id}))
        return await message.delete()

    @loader.on(~filters.me)
    async def watcher(self, app: Client, message: types.Message):
        """Принт"""
        if message.chat.id in self.db.get("MuteB", "chats", []):
            return await utils.answer(message, "Пользователь добавил вас в чёрный список. Походу вы ему чем-то насолили")
