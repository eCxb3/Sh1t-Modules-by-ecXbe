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

    async def ghoul_inline_handler(self, app: Client, inline_query: InlineQuery, args: str):

        """Гуль"""
        print(inline)
        await inline_query.answer(
            [
                InlineQueryResultArticle(
                    id=inline.result_id(),
                    title="Ghoul",
                    description="Запустить гуля" + (
                        f" Аргументы: {args}" if args
                        else ""
                    ),
                    input_message_content=InputTextMessageContent(
                        "НЕ НАЖИМАТЬ, ВАМ ПИЗДЕЦ БУДЕТ"),
                    reply_markup=InlineKeyboardMarkup().add(
                        InlineKeyboardButton("Запустить гуля", callback_data="ghoul_button_callback"))
                )
            ]
        )

    @loader.on_bot(lambda self, app, call: call.data == "ghoul_button_callback")
    async def ghoul_callback_handler(self, app: Client, call: CallbackQuery):

        """Кто нажмёт, тому пизда"""
        print(call)
        await app.send_message(call.chat_instance, 'Я гуль')
        await sleep(2)
        a = 1000
        while a > 0:
            c = a - 7
            await app.send_message(local, str(a) + " - 7 = " + str(c))
            a = c
            await sleep(0.1)
        await app.send_message(local, 'l l let me die')