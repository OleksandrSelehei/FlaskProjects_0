import requests
import sqlite3
from bs4 import BeautifulSoup as BS


def amedia_onlain_veb_pars():
    number_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number = 0
    lst = []
    for item in range(1, 106):
        number += 1
        print(number)
        url = requests.get(f'https://amedia.online/anime/page/{item}/')
        result = url.content
        soup = BS(result, 'lxml')
        anime_content = soup.find_all(class_='cats-full-wr clearfix')
        for content in anime_content:
            anime_content = content.find_all(class_='c1-item')
            for anime in anime_content:
                flag = 1
                anime_meta = anime.find(class_='c1-img')
                anime_url = anime_meta.get('href')
                anime_series = anime_meta.find(class_='seriya')
                if anime_series is None:
                    continue
                else:
                    anime_series = anime_series.text.strip('/')[0]
                    for i in anime_series:
                        if not (i in number_symbol):
                            flag = 0
                if flag == 0:
                    continue
                anime_title = anime.find(class_='c1-title').text
                lst.append(['AMEDIA_ONLINE', anime_title.upper(), int(anime_series), '-', anime_url])
    return lst


if __name__ == '__main__':
    data = amedia_onlain_veb_pars()
    db = sqlite3.connect('../anim.db')
    c = db.cursor()
    for content in data:
        c.execute("INSERT INTO content(website, title, series, voice, href) VALUES (?, ?, ?, ?, ?)",
                  (content[0], content[1], int(content[2]), content[3], content[4]))
    db.commit()
    db.close()