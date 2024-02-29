import asyncio
import logging
import sys

from aiogram.filters.command import Command
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message

from config import TOKEN

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()



@dp.message(Command(commands=['start']))
async def command_start_handler(message: Message):
    await message.answer(f"Привіт, яку тваринку хочеш взяти собі додому?")



async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
