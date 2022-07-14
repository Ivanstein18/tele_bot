from email import message_from_bytes
from settings import TOKEN
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json, string


bot = Bot(token= TOKEN)
dp = Dispatcher(bot)

async def startup(_):
    print('В работе!')

@dp.message_handler(commands= ['start', "help"])
async def start_command(message):
    try:
        await bot.send_message(message.from_user.id, 'Стартанул!')
        await message.delete()
    except:
        await message.reply('Напишите боту в личку')

@dp.message_handler(commands= ['информация'])
async def inf_command(message):
    await bot.send_message(message.from_user.id, 'Меня зовут Вася')

@dp.message_handler()
async def send(message):
    if {i.strip().lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()



executor.start_polling(dp, skip_updates= True, on_startup= startup)
