from pyrogram import Client, types, filters
from .. import loader

@loader.module(name="Backup", author="ecXbe")
class BackupMod(loader.Module):
  
  """Резерное копирование чата"""
  
  async def backup_cmd(self, app: Client, message: types.Message, args: str):
    
    """Включает/Выключает резервное копирование чата. Использование .backup <id чата, куда будут копироваться сообщения>"""
    
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

  @loader.on(filters.photo & filters.video)
  async def watcher(self, app: Client, message: types.Message):
    print("Backup")
    chats = self.db.get("Backup", "chats", {})
    backup_chat = chats.get(str(message.chat.id))
    await message.copy(int(backup_chat))
    print("Backup end")