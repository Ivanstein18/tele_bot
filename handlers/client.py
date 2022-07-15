from aiogram import Dispatcher, types
from create_bot import dp, bot


# @dp.message_handler(commands= ['start', "help"])
async def start_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Стартанул!')
        await message.delete()
    except:
        await message.reply('Напишите боту в личку')

# @dp.message_handler(commands= ['информация'])
async def inf_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Меня зовут Вася')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands= ['start', 'help'])
    dp.register_message_handler(inf_command, commands= ['информация']) 