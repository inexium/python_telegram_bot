# Python Telegram Bot

![python version](https://img.shields.io/badge/python-3.13-blue?logo=python&logoColor=white)
![code style](https://img.shields.io/badge/code%20style-ruff-blue)

## Commands

```
/hello
```
Just returns "Hello >>username<<"

```
/meowmeow
```
Returns a random picture of my cat

## Docker

```sh
docker build -t bot_image .

docker run --detach \
--name telegram_bot \
-e TELEGRAM_TOKEN=HERE_PUT_TOKEN \
-v /YOUR_PATH_HERE/:/opt/telegram_bot/images/ \
bot_image
```

## Package manager

Actually using **uv** as a package manager

## Images

Images are located at : PROJECT_FOLDER/images/
