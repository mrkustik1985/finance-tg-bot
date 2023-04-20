from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message
from keyboards.main_menu import get_main_menu

router = Router()

@router.message(commands = ['start'])
async def start(message: Message):
    await message.answer("Добро пожаловать, это бот возвращающий последние экономические новости!", reply_markup=get_main_menu())

@router.message(Text(text = "Вернуться в меню"))
async def answer_return_menu_from_news(message: Message):
    await message.answer("ok, teta", reply_markup=get_main_menu())