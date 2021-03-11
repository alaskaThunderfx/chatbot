import requests
import string
import os
from bs4 import BeautifulSoup

formatting = str.maketrans(' ', '_', string.punctuation)
page_n = int(input())
span_type = input()
count = 1
path = os.getcwd()
while count <= page_n:
    for n in range(1, page_n + 1):
        if count == 1:
            r = requests.get('https://www.nature.com/nature/articles')
            soup = BeautifulSoup(r.content, 'html.parser')
        else:
            r = requests.get(
                f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={str(count)}')
            soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all('li', {'class': 'app-article-list-row__item'})
        article_type = soup.find_all('span', {'class': 'c-meta__type'})
        page = f'Page_{str(n)}'
        os.mkdir(page)
        os.chdir(path + '\\' + page)
        count += 1
        for i in articles:
            if i.find('span', {'class': 'c-meta__type'}).text == span_type:
                link = i.a.get('href')
                s = requests.get('https://www.nature.com' + '{}'.format(link))
                new_soup = BeautifulSoup(s.content, 'html.parser')
                content1 = new_soup.find_all('div', {'class': 'c-article-section__content'})
                content2 = new_soup.find_all('div', {'class': 'article__body cleared'})
                content3 = new_soup.find_all('div', {'id': 'section-9hkXy4uOIg'})
                content4 = new_soup.find_all('div', {'class': 'article-item__body'})
                if content1:
                    title = new_soup.find('title')
                    with open('{}.txt'.format(title.text.translate(formatting).strip()), 'wb') as file:
                        for a in content1:
                            file.write(a.text.encode('utf-8'))
                    print(os.getcwd())
                    print('1')
                elif content2:
                    title = new_soup.find('h3')
                    with open('{}.txt'.format(title.text.translate(formatting).strip()), 'wb') as file:
                        for b in content2:
                            file.write(b.text.encode('utf-8'))
                    print('2')
                elif content3:
                    title = new_soup.find('h1')
                    with open('{}.txt'.format(title.text.translate(formatting).strip()), 'wb') as file:
                        for c in content3:
                            file.write(c.text.encode('utf-8'))
                    print('3')
                elif content4:
                    title = new_soup.find('h1', {'class': 'article-item__title'})
                    with open('{}.txt'.format(title.text.translate(formatting).strip()), 'wb') as file:
                        for d in content4:
                            file.write(d.text.encode('utf-8'))
                    print('4')
        os.chdir(path)
    print('Saved all articles.')
