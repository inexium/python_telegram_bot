FROM docker.io/python:3.13-alpine3.22

ENV PATH="/root/.local/bin:${PATH}"

RUN apk update
RUN apk add --no-cache pipx

WORKDIR /opt/telegram_bot
COPY . /opt/telegram_bot

RUN pipx install poetry
RUN poetry sync

CMD ["poetry", "run", "python", "telegram_bot/telegram_bot.py"]



