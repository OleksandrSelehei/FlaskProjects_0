import requests
import sqlite3
from bs4 import BeautifulSoup as BS


def anime_vost_veb_pars():
    number_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number = 0
    lst = []
    for item in range(1, 296):
        number += 1
        print(number)
        url = requests.get(f'https://animevost.org/page/{item}/')
        result = url.content
        soup = BS(result, 'lxml')
        anime_content = soup.find_all(class_='shortstoryHead')
        for anime_title in anime_content:
            flag = 1
            anime_url = anime_title.select('.shortstoryHead > h2 > a')
            anime_title = anime_title.text.split('/')
            arr_title = anime_title[0].split('\n')
            anime_title = anime_title[-1].split('[')
            anime_title = anime_title[1].split(' ')
            anime_title = anime_title[0].split('-')
            for i in anime_title[-1]:
                if not (i in number_symbol):
                    flag = 0
            if flag == 1:
                if len(anime_title[-1]) > 0:
                    lst.append(
                        ["ANIMEVOST", arr_title[-1].strip().upper(), int(anime_title[-1]), "AnimeVost", anime_url[0].get('href')])
    return lst


if __name__ == '__main__':
    data = anime_vost_veb_pars()
    db = sqlite3.connect('../anim.db')
    c = db.cursor()
    for content in data:
        c.execute("INSERT INTO content(website, title, series, voice, href) VALUES (?, ?, ?, ?, ?)",
                  (content[0], content[1], int(content[2]), content[3], content[4]))
    db.commit()
    db.close()

