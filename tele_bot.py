from settings import TOKEN
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token= TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message):
    if message.text == 'привет':
        await message.answer('пока')



executor.start_polling(dp, skip_updates= True)
