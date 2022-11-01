from bs4 import BeautifulSoup
import requests
import datetime


url = 'https://habr.com/ru'
key_words = ['Профессия', 'рекрутера', 'программирование', 'учиться', 'дизайн', 'фото', 'web', 'python', 'код']
links = []
cool_links = {}

response = requests.get(url)
response.encoding = 'utf-8'
href_searching = BeautifulSoup(response.text, 'html.parser').find_all('a', class_="tm-article-snippet__title-link")
links += [f"{url}{href['href'][3:]}" for href in href_searching]

for link in links:
    response = requests.get(link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    texts = soup.find_all('p')
    for text in texts:
        for key_word in key_words:
            if key_word in text.text.split():
                if link not in cool_links:
                    cool_links[link] = [datetime.datetime.fromisoformat(soup.find('time')['datetime']), soup.title.text]

for k, v in cool_links.items():
    print(f'{v[0]} => {v[1]} ==> {k}')