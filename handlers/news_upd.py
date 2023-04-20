from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message
import data.data_base as db
import data.user_info as ui
import parsing.parser as ps
from keyboards.main_menu import get_next_news_menu, get_main_menu


router = Router()
@router.message(Text(text = "Новости экономики и финансов"))
async def answer_news(message: Message):
    if len(db.economic_news_info) == 0:
        await ps.rbk_economics_news()
    usr_id = str(message.from_user.id)
    news_need = ui.users_news_progress.get(usr_id, -1) + 1
    ui.users_news_progress[usr_id] = news_need
    if news_need == len(db.economic_news_info):
        message.answer("Все новости на сегодня просмотрены ✅✅✅\nНачинаю с начала.")
        ui.users_news_progress[usr_id] = 0
        news_need = 0
    need = None
    for news in db.economic_news_info.items():
        need = news[1]
        if news_need == 0:
            break
        news_need -= 1
    await message.answer(
        f"{need}",
        parse_mode="html",
        reply_markup=get_next_news_menu()
    )

@router.message(Text(text = "Курс $ и €"))
async def get_currency(message: Message):
    if len(db.bax_rates_info) == 0 or '🆘' in db.bax_rates_info[0]:
        db.bax_rates_info.clear()
        db.euro_rates_info.clear()
        await ps.get_exchange_rate()
    mes =  "Вчера:          1💵 = " + db.bax_rates_info[0] + "       1💶 = " + db.euro_rates_info[0] + "\n"
    mes += "Позавчера: 1💵 = " + db.bax_rates_info[1] + "       1💶 = " + db.euro_rates_info[1]
    await message.answer(mes)

@router.message(Text(text = "Следующая новость"))
async def answer_news(message: Message):
    if len(db.economic_news_info) == 0:
        await ps.rbk_economics_news()
    usr_id = str(message.from_user.id)
    news_need = ui.users_news_progress.get(usr_id, -1) + 1
    ui.users_news_progress[usr_id] = news_need
    if news_need == len(db.economic_news_info):
        message.answer("Все новости на сегодня просмотрены ✅✅✅\nНачинаю с начала.")
        ui.users_news_progress[usr_id] = 0
        news_need = 0
    need = None
    for news in db.economic_news_info.items():
        need = news[1]
        if news_need == 0:
            break
        news_need -= 1
    await message.answer(
        f"{need}",
        parse_mode="html",
        reply_markup=get_next_news_menu()
    )