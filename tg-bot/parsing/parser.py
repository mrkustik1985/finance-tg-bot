import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import data.data_base as db


async def get_exchange_rate():
    cbr_resp = requests.get(db.cbr_url)
    bs_cbr = BeautifulSoup(cbr_resp.text, "lxml")
    ###избавиться от вылета из-за исключений
    indexes = bs_cbr.find_all('div', 'main-indicator_value')
    indexes_keys = ['Цель по инфляции', 'Инфляция за', 'Ключевая ставка', 'Ставка RUONIA']
    indexes_value_dates = bs_cbr.find_all('div', 'main-indicator_text')
    if len(indexes_value_dates) == 0:
        db.indexes_info = [indexes_keys[i] + " 🆘. Мы скоро решим эту проблему." for i in range(len(indexes_keys))]
        db.bax_rates_info.append("🆘")
        db.bax_rates_info.append("🆘")
        db.euro_rates_info.append("🆘")
        db.euro_rates_info.append("🆘")
    else:
        indexes_keys[1] += " " + indexes_value_dates[1].find('a').text.strip()
        indexes_keys[2] += " " + indexes_value_dates[2].find('a').text.strip()
        indexes_keys[3] += " " + indexes_value_dates[3].text.strip()
        db.indexes_info = [indexes_keys[i] + ": " + indexes[i].text.strip() for i in range(len(indexes_keys))]
        rates_info = bs_cbr.find_all('div', 'col-md-2 col-xs-9 _right mono-num')
        db.bax_rates_info.append(rates_info[2].text.strip())  # Вчера
        db.bax_rates_info.append(rates_info[3].text.strip())  # Позавчера
        db.euro_rates_info.append(rates_info[0].text.strip())  # Вчера
        db.euro_rates_info.append(rates_info[1].text.strip())  # Позавчера

async def rbk_economics_news():
    r = requests.get(db.economic_news_url)
    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("div", class_ = "item__wrap l-col-center")
    for article in articles_cards:
        title = article.find("span", class_ = "item__title rm-cm-item-text js-rm-central-column-item-text")
        db.economic_news_info[title] = article.a['href']

async def invest_idea_upd():
    r = requests.get(db.invest_url)
    soup = BeautifulSoup(r.text, "lxml")
    get_all_ideas = soup.find_all("div", class_ = "idea-item___3a4SC")
    for idea in get_all_ideas:
        idea_info = [x.text.strip() for x in idea.find_all('p', 'typo___oYDNK')]
        db.invest_ideas_info[idea_info[0]] = ["аналитик : " + idea_info[1], 
                                              "срок начала " + idea_info[2], 
                                              "срок достижения цели " + idea_info[3],
                                              "потенциальная доходность " + idea_info[5],]
    # print(db.invest_ideas_info)

async def update_msc_stocks():
    r = requests.get(db.stocks_msc_url)
    soup = BeautifulSoup(r.text, "lxml")
    get_stocks_msk = soup.find_all("tr")
    for i in get_stocks_msk[1:]:
        i = i.find_all("td")
        db.stocks_msc_info[("название: " + i[2].text.strip(), "тикер: " + i[3].text.strip())]= [
                                        "время обновления: " + i[1].text.strip(),
                                        "последняя цена: " + i[7].text.strip(), 
                                        "изменение: " + i[8].text.strip(),
                                        "объем торгов(млн.руб): " + i[9].text.strip()
                                        ]
    db.stocks_msk_time_upd = time.mktime(datetime.strptime(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S").timetuple())