#    Sh1t-UB (telegram userbot by sh1tn3t)
#    Copyright (C) 2021-2022 Sh1tN3t

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import configparser

import psutil
import platform

from aiogram.types import (
    InlineQuery,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

from pyrogram import Client, types
from .. import loader, utils, __version__
from typing import Union, List

@loader.module(name="TEST", author="ecXbe")
class TestMod(loader.Module):
  def __init__(
        self,
        app: Client,
        chat_id: Union[str, int],
        purge: bool = False
    ) -> None:
        """Инициализация класса
        Параметры:
            app (``pyrogram.Client``):
                Клиент
            chat_id (``str`` | ``int``):
                Чат, в который нужно отправить сообщение
            purge (``bool``, *optional*):
                Удалять сообщения после завершения диалога
        """
        self.app = app
        self.chat_id = chat_id
        
  async def test_cmd(self, app: Client, message: types.Message):  
    history = self.app.get_history(self.chat.id, limit=1)
    print(history[0])
