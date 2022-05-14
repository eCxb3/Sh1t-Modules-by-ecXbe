from asyncio import sleep

from aiogram.types import (
    Message,
    CallbackQuery,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from pyrogram import Client, types
from .. import loader, utils, __version__

@loader.module(name="GhoulForAll", author="ecXbe")
class GhoulforallMod(loader.Module):
    async def example_inline_handler(self, app: Client, inline_query: InlineQuery, args: str):  # _inline_handler на конце функции чтобы обозначить что это инлайн-команда
                                                                                                # args - аргументы после команды. необязательный аргумент
        """Пример инлайн-команды. Использование: @bot example [аргументы]"""
        await inline_query.answer(
            [
                InlineQueryResultArticle(
                    id=utils.random_id(),
                    title="Ghoul"
                    description="Запустить гуля"
                    ),
                    input_message_content=InputTextMessageContent(
                        "Нажми на кнопочку, ну давай, ну попробуй"),
                    reply_markup=InlineKeyboardMarkup().add(
                        InlineKeyboardButton("Гулёнок", callback_data="ghoul_button_callback"))
                )
            ]
        )

    @loader.on_bot(lambda self, app, call: call.data == "ghoul_button_callback")  # Сработает только если каллбек дата равняется "example_button_callback"
    async def example_callback_handler(self, app: Client, call: CallbackQuery):  # _callback_handler на конце функции чтобы обозначить что это каллбек-хендлер
        """Пример каллбека"""
        await self.bot.edit_message_text(inline_message_id=call.inline_message_id, text='Я гуль')
        await sleep(2)
        a = 1000
        while a > 0:
          c = a - 7
          await self.bot.edit_message_text(inline_message_id=call.inline_message_id, text=str(a) + " - 7 = " + str(c))
          a = c
          await sleep(0.1)
        await self.bot.edit_message_text(inline_message_id=call.inline_message_id, text='l l let me die')
    

