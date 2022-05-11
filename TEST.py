from asyncio import sleep

from aiogram.types import (
    InlineQuery,
    CallbackQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from pyrogram import Client, types
from .. import loader, utils, inline

@loader.module(name="TEST", author="ecXbe")
class ExampleMod(loader.Module):
  
    """dsfa"""

    async def info_cmd(self, app: Client, message: types.Message):
        """Вызывает инлайн-команду info. Использование: info"""
        bot_results = await app.get_inline_bot_results(
            (await self.bot_manager.bot.me).username, "info")

        await app.send_inline_bot_result(
            message.chat.id, bot_results.query_id,
            bot_results.results[0].id
        )
        return await message.delete()
