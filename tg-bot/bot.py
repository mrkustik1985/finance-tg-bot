import asyncio
import datetime
from aiogram import Bot, Dispatcher, types, Router
from aiogram.dispatcher.filters import Text
from config import token
import time
from handlers import main_menu, news_upd, invest_ideas


bot = Bot(token=token)
dp = Dispatcher()
    

async def main():
    dp.include_router(news_upd.router)
    dp.include_router(main_menu.router)
    dp.include_router(invest_ideas.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())