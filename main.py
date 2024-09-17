
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

logging.basicConfig(level=logging.INFO)

bot = Bot(token='7066132436:AAHc1oFOIwYN9V9PKK_tSx9wqt4t7gVM6CU') 
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    webAppInfo = types.WebAppInfo(url="https://n3ke2710.github.io")
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Отправить данные', web_app=webAppInfo))
    
    await message.answer(text='Привет!', reply_markup=builder.as_markup())

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())


  