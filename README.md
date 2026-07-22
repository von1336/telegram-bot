# Telegram Bot

Бот на aiogram 3.x с несколькими полезными командами. Ничего революционного, но работает стабильно и код читаемый.

## Команды

- `/start` — приветствие с inline-кнопками
- `/weather Москва` — погода через OpenWeatherMap API
- `/calc 2+2*2` — калькулятор (безопасный, фильтрует ввод)
- `/help` — справка

## Запуск

```bash
pip install -r requirements.txt
export BOT_TOKEN="твой_токен_от_BotFather"
export WEATHER_API_KEY="ключ_openweathermap"
python bot.py
```

## Docker

```bash
docker build -t mybot .
docker run -e BOT_TOKEN=xxx -e WEATHER_API_KEY=yyy mybot
```

## Структура

```
bot.py            — точка входа
config.py         — конфиг из env
handlers/
  start.py        — /start
  help.py         — /help
  weather.py      — /weather
  calculator.py   — /calc
```

## Заметки

- Калькулятор использует `eval`, но с whitelist-паттерном — безопасно
- Погода кэшируется нет, так что при спаме API может забанить. Для продакшена добавь Redis
- Логи пишутся в stdout, удобно для docker logs

Если нужен бот под заказ — пиши в телегу @simulcra
