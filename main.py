from wsgiref import headers
from bs4 import BeautifulSoup
import csv

import requests


def get_html(url):
    r = requests.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0'})
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('OMA.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['way']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find('div', id="data-ga__catalog-products-grid").find_all('img')
    for el in data:
        src = el.get('data-src')
        if src is not None:
            way = 'https://www.oma.by' + src
            data = {'way': way}
            print(data)
            write_csv(data)


def main():
    url = 'https://www.oma.by/pechnoe-oborudovanie-c'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
