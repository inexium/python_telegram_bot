# Python Telegram Bot
Just for fun<br>

## Commands
/hello<br>
Just returns "Hello >>username<<"<br>

/meowmeow<br>
Returns a random picture of my cat<br>

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
Using poetry

## Images
Create a folder at root of project called "images"