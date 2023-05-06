from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message
from keyboards.main_menu import get_main_menu

router = Router()

@router.message(commands = ['start'])
async def start(message: Message):
    await message.answer("Добро пожаловать, это бот возвращающий последние экономические новости!\n"
                         "Для изучения функционала бота напишите /help\n",
                         reply_markup=get_main_menu())

@router.message(commands = ['help'])
async def help(message: Message):
    await message.answer("Основные возможности бота:\n"
                         "1) Новости мира экономики и финансов\n"
                         "2) Информация с сайта ЦБ РФ с экономическими показателями и текущими курсами валют\n"
                         "3) Просмотр актуальных котировок акций СПБ и Московской Бирж, сырья и криптовалюты\n"
                         "4) Инвест - идеи от авторов (обновления нерегулярные и редкие)\n"
                        "Для более подробной информации о возможностях работы с акциями пишите '/help_stock'")

@router.message(commands=['help_stock'])
async def get_help_stock(message: Message):
    await message.answer(
        "🗯Команды '/msc_find' и '/spb_find' ищут среди названий компаний и тикеров совпадения и отправляют "
        "обратно сообщение с информацией по паттерну по умолчанию(текущая котировка акции с биржы и дельта)."
    )



@router.message(Text(text = "Вернуться в меню"))
async def answer_return_menu_from_news(message: Message):
    await message.answer("ok, teta", reply_markup=get_main_menu())