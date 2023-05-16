import requests
from bs4 import BeautifulSoup as BS


def ongoing_yammy_pars_veb():
    anime_content_url = []
    for item in range(1, 6):
        url = requests.get(f'https://yummyanime.tv/ongoing/page/{item}/')
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


def ongoing_yummyanime_content_pars(content_list):
    lst = []
    for con in content_list:
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


def ongoing_anime_vost_pars():
    number_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lst = []
    for item in range(1, 12):
        url = requests.get(f'https://animevost.org/ongoing/page/{item}/')
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
                        ["ANIMEVOST", arr_title[-1].strip().upper(), int(anime_title[-1]), "AnimeVost",
                         anime_url[0].get('href')])
    return lst


def ongoing_jut_su_pars():
    lst = []
    for item in range(1, 5):
        url = requests.get(f'https://jut-su.net/ongoing/page/{item}/')
        result = url.content
        soup = BS(result, 'lxml')
        anime_content = soup.find_all(class_='short-title')
        for anime_meta in anime_content:
            lst.append("https://jut-su.net" + anime_meta.get('href'))
    return lst


def ongoing_jut_su_pars_content(content_list):
    number_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    meta_data_ongoing = 'short-meta short-meta-status ongoing'
    meta_data_released = 'short-meta short-meta-status released'
    lst = []
    for con in content_list:
        flag = 1
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
                    lst.append(["JUT-SU.NET", anime_title.text.strip().split('\n')[0].upper(),
                                int(anime_series.text.split(' ')[0]), anime_translate[-1].text.split(':')[-1].strip(),
                                con])
    return lst


def ongoing_anidub_pars():
    lst = []
    for item in range(1):
        url = requests.get(f'https://anidub.vip/anime/anime_ongoing/page/{item}/')
        result = url.content
        soup = BS(result, 'lxml')
        anime_content = soup.find_all(class_='sect-content sect-items')
        for content in anime_content:
            content = content.find_all(class_='th-item')
            for anime in content:
                anime_url = anime.find(class_='th-itemb').find(class_='th-in').get('href')
                lst.append(anime_url)
    return lst


def ongoing_anidub_pars_original_content(content_list):
    number_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lst = []
    for con in content_list:
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


def ongoing_amedia_onlain_pars():
    number_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    lst = []
    for item in range(1, 15):
        url = requests.get(f'https://amedia.online/ongoingi/page/{item}/')
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
    print(ongoing_amedia_onlain_pars())