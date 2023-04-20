from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message
import data.data_base as db
import data.user_info as ui
import parsing.parser as ps
from keyboards.main_menu import get_main_menu, get_next_ideas_menu

router = Router()
@router.message(Text(text = "Инвестиционные идеи"))
async def invest_ideas(message: Message):
    if len(db.invest_ideas_info) == 0:
        await ps.invest_idea_upd()
    usr_id = str(message.from_user.id)
    ideas_need = ui.users_ideas_progress.get(usr_id, -1) + 1
    ui.users_ideas_progress[usr_id] = ideas_need
    if len(db.invest_ideas_info) <= ideas_need:
        await message.answer("Все инвестиционные идеи на сегодня просмотрены🤑🤑🤑. Перехожу в основное меню",
                        reply_markup=get_main_menu())
    else:
      await message.answer(
          transform_ideas(ideas_need),
          parse_mode = "html",
          reply_markup = get_next_ideas_menu()
      )
@router.message(Text(text = "Следующая идея"))
async def invest_ideas(message: Message):
    if len(db.invest_ideas_info) == 0:
        await ps.invest_idea_upd()
    usr_id = str(message.from_user.id)
    ideas_need = ui.users_ideas_progress.get(usr_id, -1) + 1
    ui.users_ideas_progress[usr_id] = ideas_need
    if len(db.invest_ideas_info) <= ideas_need:
        await message.answer("Все инвестиционные идеи на сегодня просмотрены🤑🤑🤑. Перехожу в основное меню", 
                       reply_markup=get_main_menu())
    else:
      await message.answer(
          transform_ideas(ideas_need),
          parse_mode = "html",
          reply_markup = get_next_ideas_menu()
      )

def transform_ideas(ideas_need):
    need = None
    number = ideas_need + 1
    for news in db.invest_ideas_info.items():
        need = news
        if ideas_need == 0:
            break
        ideas_need -= 1
    answer = f"{number}) {need[0]}"
    for i in range(len(need[1])):
        answer = answer + "\n" + need[1][i]
    return answer
    