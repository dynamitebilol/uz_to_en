import logging
from google_translate_py import Translator
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2092667828:AAFGK0TpnE8LHoZ0s47AN-XAHT-46M4svIM'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm Translator!\nMade by @dynamitebilol.")


@dp.message_handler()
async def translated(message: types.Message):
    try:
        respond = (Translator().translate(message.text, "uz", "en"))
        await message.answer(respond)
    except:
        await message.answer("Bu bot faqat boshqa tillardan o'zbek tiliga tarjima qiladi.Shuning uchun o'zbek tilidan boshqa tilda yozing")



executor.start_polling(dp, skip_updates=True)