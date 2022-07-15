import json, string
from aiogram import Dispatcher, types
from create_bot import dp


# @dp.message_handler()
async def send(message: types.Message):
    if {i.strip().lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(send)