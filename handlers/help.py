from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def cmd_help(message: Message):
    text = (
        "<b>Доступные команды:</b>\n\n"
        "/start — запустить бота\n"
        "/weather &lt;город&gt; — узнать погоду\n"
        "/calc &lt;выражение&gt; — посчитать\n"
        "/help — эта справка\n\n"
        "<b>Примеры:</b>\n"
        "<code>/weather Москва</code>\n"
        "<code>/calc 2+2*2</code>"
    )
    await message.answer(text)
