import aiohttp
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import WEATHER_API_KEY

router = Router()

@router.message(Command("weather"))
async def cmd_weather(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Укажи город: <code>/weather Москва</code>")
        return

    city = args[1].strip()
    if not WEATHER_API_KEY:
        await message.answer("Погода временно недоступна (не настроен API-ключ)")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric", "lang": "ru"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status != 200:
                await message.answer(f"Не нашёл город «{city}». Проверь написание.")
                return
            data = await resp.json()

    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    await message.answer(
        f"🌤 <b>{data['name']}</b>\n\n"
        f"Температура: {temp:.0f}°C (ощущается как {feels:.0f}°C)\n"
        f"За окном: {desc}\n"
        f"Влажность: {humidity}%\n"
        f"Ветер: {wind} м/с"
    )
