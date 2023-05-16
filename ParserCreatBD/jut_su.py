import requests
import sqlite3
from bs4 import BeautifulSoup as BS


def jut_su_pars_veb():
    lst = []
    for item in range(1, 63):
        print(item)
        url = requests.get(f'https://jut-su.net/tv-series/page/{item}/')
        result = url.content
        soup = BS(result, 'lxml')
        anime_content = soup.find_all(class_='short-title')
        for anime_meta in anime_content:
            lst.append("https://jut-su.net" + anime_meta.get('href'))
    return lst


def jut_su_pars_content(content_list):
    number_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number = 0
    meta_data_ongoing = 'short-meta short-meta-status ongoing'
    meta_data_released = 'short-meta short-meta-status released'
    lst = []
    for con in content_list:
        flag = 1
        number += 1
        print(number)
        q = requests.get(con)
        result = q.content
        soup = BS(result, 'lxml')
        anime_title = soup.find(class_='fheader-left fx-1')
        anime_translate = soup.find_all(class_='sd-line')
        anime_series = soup.find(class_=meta_data_ongoing)
        if anime_series is None:
            anime_series = soup.find(class_=meta_data_released)
        if anime_series is not None:
            for i in anime_series.text.split(' ')[0]:
                if not (i in number_symbol):
                    flag = 0
            if flag == 1:
                if len(anime_series.text.split(' ')[0]) > 0:
                    lst.append(["JUT-SU.NET", anime_title.text.strip().split('\n')[0].upper(), int(anime_series.text.split(' ')[0]), anime_translate[-1].text.split(':')[-1].strip(), con])
    return lst


if __name__ == '__main__':
    content_list = jut_su_pars_veb()
    print(content_list)
    if len(content_list) > 100:
        data = jut_su_pars_content(content_list)
        db = sqlite3.connect('../anim.db')
        c = db.cursor()
        for content in data:
            c.execute("INSERT INTO content(website, title, series, voice, href) VALUES (?, ?, ?, ?, ?)",
                      (content[0], content[1], int(content[2]), content[3], content[4]))
        db.commit()
        db.close()