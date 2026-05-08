FROM astral/uv:python3.13-alpine3.23

WORKDIR /opt/telegram_bot
COPY . /opt/telegram_bot

CMD ["uv", "run", "python", "telegram_bot/telegram_bot.py"]



