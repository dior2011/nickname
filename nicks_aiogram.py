#bot.py
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from nicks_buttons import buttons
from nicks import nicknames

TOKEN = "6779295155:AAH8Iq5yGkUHVoG-r-DgkSgr9JI9eUOB35M"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = message.from_user.full_name
    print(message.text)
    await message.reply(f"Assalomu alaykum, {full_name}! Ismingizni yozing!")
    


@dp.message(F.text)
async def ism_answer(message: Message):
    global ism
    await message.answer(text=nicknames(message.text),reply_markup=buttons)
    ism = [message.text]
    
    await message.delete()
    
from aiogram.types import CallbackQuery
@dp.callback_query(F.data)
async def callback_handler(callback: CallbackQuery):
    await callback.message.answer(text=nicknames(ism[0]),reply_markup=buttons)
    await callback.message.delete()

async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    