import re
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

# разрешаем только безопасные символы
SAFE_PATTERN = re.compile(r'^[\d\s\+\-\*\/\(\)\.]+$')

@router.message(Command("calc"))
async def cmd_calc(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Напиши выражение: <code>/calc 2+2*2</code>")
        return

    expr = args[1].strip()

    if not SAFE_PATTERN.match(expr):
        await message.answer("Можно использовать только цифры и операторы + - * / ( )")
        return

    try:
        # вычисляем — eval тут безопасен, т.к. паттерн отфильтровал всё лишнее
        result = eval(expr, {"__builtins__": {}}, {})
        await message.answer(f"<code>{expr}</code> = <b>{result}</b>")
    except ZeroDivisionError:
        await message.answer("Деление на ноль! 🙃")
    except Exception:
        await message.answer("Не смог посчитать. Проверь выражение.")
