from settings import TOKEN
from aiogram import Bot
from aiogram.dispatcher import Dispatcher


bot = Bot(token= TOKEN)
dp = Dispatcher(bot)