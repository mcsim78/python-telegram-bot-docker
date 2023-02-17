# Telegram bot template
This is a template for telegram bot that used library aiogram.
This project was created for me to quickly create a telegram bot. I hope it will be useful to you. If you have any suggestions, please write to me, I will be glad to hear them.
You can use it as a basis for your project. This template ready for run as a docker container. There are a few simple examples of handlers.
Write your logic in the `bot_lib/` directory.
Handlers place in the `handlers/` directory and connect them in the `bot.py` file.

## How to run in docker
1. Clone the repository.
2. Run `docker-compose up -d` and wait for the build to finish.


## Structure

* `bot.py`: point of entry into the bot
* `bot_lib/`: place here the logic of the bot, additional functions
* `bot_lib/bot_create.py`: creating Dispatcher, CallbackData, Storage and other instances
* `bot_lib/settings.py`: the bot settings
* `handlers/`: handlers for bot commands
* `handlers/message_handlers.py`: handlers for user messages
* `handlers/callback_handlers.py`: handlers for callback requests
* `handlers/error_handlers.py`: handlers for errors
* `handlers/state_forms.py`: forms for states
* `keyboards/`: keyboards for bot
* `keyboards/common_keyboards.py`: additional functions for creating keyboards
* `Dockerfile`: file for building docker image
* `docker-compose.yml`: used to run the bot
* `requirements.txt`: list of package dependencies
