from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Курс $ и €')
    kb.button(text='Новости экономики и финансов')
    kb.button(text='Инвестиционные идеи')
    kb.adjust(2, 2, 2, 1)
    return kb.as_markup(resize_keyboard=True)


def get_next_news_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Следующая новость")
    kb.button(text="Вернуться в меню")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_next_ideas_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Следующая идея")
    kb.button(text="Вернуться в меню")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)