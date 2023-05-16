import requests
import sqlite3
from bs4 import BeautifulSoup as BS


def anidub_pars_original_veb():
    lst = []
    for item in range(1, 151):
        url = requests.get(f'https://anidub.vip/anime/page/{item}/')
        result = url.content
        soup = BS(result, 'lxml')
        anime_content = soup.find_all(class_='sect-content sect-items')
        for content in anime_content:
            content = content.find_all(class_='th-item')
            for anime in content:
                anime_url = anime.find(class_='th-itemb').find(class_='th-in').get('href')
                lst.append(anime_url)
    return lst


def anidub_pars_original_content(content_list):
    number_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number = 0
    lst = []
    for con in content_list:
        number += 1
        print(number)
        flag = 1
        q = requests.get(con)
        result = q.content
        soup = BS(result, 'lxml')
        anime_meta = soup.find(class_='fright fx-1')
        if anime_meta is not None:
            anime_meta = anime_meta.select('h1')
            anime_title = anime_meta[0].text
            anime_title = anime_title.split('/')[0].strip().upper()
            anime_series = anime_meta[0].text
            if '[' in anime_series:
                anime_series = anime_series.split('/')[-1].split('[')[-1].split(' ')[0][-1]
            else:
                continue
            for i in anime_series:
                if not (i in number_symbol):
                    flag = 0
            if flag == 1:
                if len(anime_series) > 0:
                    lst.append(['ANIDUB.VIP', anime_title, int(anime_series), 'AniDUB', con])
        else:
            continue
    return lst


if __name__ == '__main__':
    data = anidub_pars_original_content(anidub_pars_original_veb())
    db = sqlite3.connect('../anim.db')
    c = db.cursor()
    for content in data:
        c.execute("INSERT INTO content(website, title, series, voice, href) VALUES (?, ?, ?, ?, ?)",
                  (content[0], content[1], int(content[2]), content[3], content[4]))
    db.commit()
    db.close()