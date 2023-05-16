import requests
import sqlite3
from bs4 import BeautifulSoup as BS


def yummyanime_veb_pars():
    anime_content_url = []
    for item in range(1, 80):
        url = requests.get(f'https://yummyanime.tv/series/page/{item}/')
        result = url.content
        soup = BS(result, 'lxml')
        anime_content = soup.find_all(class_='section__content section__items')
        for anime in anime_content:
            anime_work = anime.find_all(class_='movie-item')
            for anime_title in anime_work:
                anime_title_result = anime_title.find_all(class_='movie-item__link')
                for anime_result in anime_title_result:
                    anime_url = anime_result.get('href')
                    anime_content_url.append(f'https://yummyanime.tv{anime_url}')
    return anime_content_url


def yummyanime_content_pars(content_list):
    number = 0
    lst = []
    for con in content_list:
        number += 1
        print(number)
        q = requests.get(con)
        result = q.content
        soup = BS(result, 'lxml')
        anime_title = soup.find(class_='inner-page__title')
        anime_translate = soup.find(class_='inner-page__list')
        anime_series = soup.find(class_='movie-item__label')
        try:
            if anime_translate is None:
                raise ValueError()
            if anime_series is None:
                raise ValueError
            anime_series = anime_series.text.split(' ')
            anime_translate = anime_translate.text.split(':')
            lst.append(["YUMMYANIME.TV", anime_title.text.upper(), int(anime_series[0]), anime_translate[-1].strip(), con])

        except ValueError:
            continue

    return lst


if __name__ == '__main__':
    data = yummyanime_content_pars(yummyanime_veb_pars())
    db = sqlite3.connect('../anim.db')
    c = db.cursor()
    for content in data:
        c.execute("INSERT INTO content(website, title, series, voice, href) VALUES (?, ?, ?, ?, ?)",
                  (content[0], content[1], int(content[2]), content[3], content[4]))
    db.commit()
    db.close()