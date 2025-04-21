import os
import json
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for q in questions:
        keyboard.add(types.KeyboardButton(q["question"]))
    await message.answer("Выберите вопрос:", reply_markup=keyboard)

@dp.message_handler()
async def answer_question(message: types.Message):
    for q in questions:
        if message.text == q["question"]:
            await message.answer(q["answer"])
            return
    await message.answer("Вопрос не найден. Пожалуйста, выберите из списка.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
