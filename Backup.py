from pyrogram import Client, types, filters
from .. import loader

@loader.module(name="Backup", author="ecXbe")
class BackupMod(loader.Module):

  async def backup_cmd(self, app: Client, message: types.Message, args: str):
    chats = self.db.get("Backup", "chats", {})
    if not chats.get(str(message.chat.id)):
      if not args:
        return await message.edit("<b>[Backup]</b> Нет чата для резервного копирования")
      chats[str(message.chat.id)] = args
      self.db.set("Backup", "chats", chats)
      return await message.edit("<b>[Backup]</b> Резервное копирование этого чата включено")

    del chats[str(message.chat.id)]
    self.db.set("Backup", "chats", chats)
    return await message.edit("<b>[Backup]</b> Резервное копирование этого чата выключено")

  @loader.on(lambda _, __, mess: mess.media == "video" or mess.media == "photo")
  async watcher(self, app: Client, message: types.Message):
    chats = self.db.get("Backup", "chats", {})
    if message.chat.id in chats:
      backup_chat = chats.get(str(message.chat.id))
      await message.copy(backup_chat)
