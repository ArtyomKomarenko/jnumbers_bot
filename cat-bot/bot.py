import os
import time

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

chat_id = 285966818
bot = Bot(os.getenv("BOT_TOKEN"))


def send_random_cat():
    url = f'https://cataas.com/cat?t=${time.time()}'
    bot.send_photo(chat_id, url)


def main() -> None:
    send_random_cat()
    print('Cat has been sent')


if __name__ == "__main__":
    main()
