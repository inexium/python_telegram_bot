import os
import random
from functools import partial, wraps

from decouple import config

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# inexium, alesia
RESTRICTED_IDS = [6154568530, 6018396337]


class restricted(object):
    """
    Decorator class used to restrict usage of commands.
    Sends a "disallowed" reply if necessary. Works on functions and methods.
    """

    def __init__(self, func):
        self._func = func
        self._obj = None
        self._wrapped = None

    def __call__(self, *args, **kwargs):
        if not self._wrapped:
            if self._obj:
                self._wrapped = self._wrap_method(self._func)
                self._wrapped = partial(self._wrapped, self._obj)
            else:
                self._wrapped = self._wrap_function(self._func)
        return self._wrapped(*args, **kwargs)

    def __get__(self, obj, type_=None):
        self._obj = obj
        return self

    def _wrap_method(self, method):  # Wrapper called in case of a method
        @wraps(method)
        def inner(
            self, *args, **kwargs
        ):  # `self` is the *inner* class' `self` here
            user_id = args[0].effective_user.id  # args[0]: update
            if user_id not in RESTRICTED_IDS:
                print(
                    f"Unauthorized access denied on {method.__name__} "
                    f"for {user_id} : {args[0].message.chat.username}."
                )
                args[0].message.reply_text("User disallowed.")
                return None  # quit handling command
            return method(self, *args, **kwargs)

        return inner

    def _wrap_function(self, function):  # Wrapper called in case of a function
        @wraps(function)
        def inner(
            *args, **kwargs
        ):  # `self` would be the *restricted* class' `self` here
            user_id = args[0].effective_user.id  # args[0]: update
            if user_id not in RESTRICTED_IDS:
                print(
                    f"Unauthorized access denied on {function.__name__} "
                    f"for {user_id} : {args[0].message.chat.username}."
                )
                args[0].message.reply_text("User disallowed.")
                return None  # quit handling command
            return function(*args, **kwargs)

        return inner


@restricted
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name}"
    )


@restricted
async def send_my_cat(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    images = os.listdir("telegram_bot/images/")
    random_value = random.randrange(0, len(images))
    with open("telegram_bot/images/%s" % images[random_value], "rb") as img:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id, photo=img
        )


app = ApplicationBuilder().token(config("TELEGRAM_TOKEN")).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("meowmeow", send_my_cat))

app.run_polling()
