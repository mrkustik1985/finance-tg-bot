from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message
import data.data_base as db
import data.user_info as ui
import parsing.parser as ps
from datetime import datetime
import time
from config import TIME_TO_UPDATE_STOCKS
from keyboards.main_menu import get_main_menu

router = Router()
@router.message(commands = "msc_find")
async def msc_find_upd(message: Message):
    tm = check_is_need_upd()
    if tm != -1:
        await ps.update_msc_stocks()
        db.stocks_msc_time_upd = get_time(datetime.now())
    need_comp = message.text.split()[1].strip()
    answer = f"Вот что удалось найти по запросу {need_comp}:\n\n"
    cnt = 1
    fl = 0
    for i, j in db.stocks_msc_info.keys():
        if need_comp.lower() in i.lower() or need_comp.lower() in j.lower():
            fl = 1
            t = db.stocks_msc_info[(i, j)]
            answer = answer + "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵\n"
            answer = answer + f"{cnt}) {i}\n{j}\n"
            for x in t:
                if 'цена' in x:
                   answer = answer + "💸" + x + '\n'
                elif '-' in x:
                  answer = answer + "🗿" + x + '\n'
                elif '+' in x:   
                  answer = answer + "🚬" + x + '\n'
                else:
                  answer = answer + x + '\n'
            cnt += 1
            answer += '\n'
    if fl == 0:
       answer = answer + "🔴Увы, вы допустили ошибку в названии, повторите запрос"
    await message.answer(
        answer,
        parse_mode = "html",
        reply_markup = get_main_menu()
    )

def check_is_need_upd():
    time_now = get_time(datetime.now())
    if time_now - db.stocks_msc_time_upd < TIME_TO_UPDATE_STOCKS:
        return -1
    return time_now

def get_time(time_need):
  return time.mktime(datetime.strptime(datetime.strftime(time_need, "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S").timetuple())