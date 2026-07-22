from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌤 Погода", callback_data="weather")],
        [InlineKeyboardButton(text="🧮 Калькулятор", callback_data="calc")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")],
    ])
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я простой бот с парой полезных функций. Выбери что нужно:",
        reply_markup=kb
    )
