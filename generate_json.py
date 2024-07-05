"""
Script to generate a json file with various book information scraped from the internet,
based on a text file with list of books.
"""

import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import re


def get_book_info(query):
    query_parsed = urllib.parse.quote_plus(query)
    url = f'https://www.goodreads.com/search?q={query_parsed}'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0'}
    r = requests.get(url, headers=headers)

    # initialize variables
    title = query
    author = ''
    author_url = ''
    book_url = ''
    cover_url = ''
    rating = ''
    error = True

    # Parsing the HTML
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        s1 = soup.find('a', class_='bookTitle')
        s2 = soup.find('a', class_='authorName')
        s3 = soup.find('img', class_='bookCover')
        s4 = soup.find('span', class_='greyText smallText uitext')

        try:
            title = s1.text.strip()
            book_url = s1.get('href')
            book_url = 'https://www.goodreads.com' + book_url

            author = s2.text.strip()
            author_url = s2.get('href')

            cover_url = s3.get('src')
            cover_url = re.sub(r'\._[0-9A-Z]{4}_', '', cover_url).replace('_','')

            rating = s4.text.strip().split('\n')[0]

            error = False

        except:
            pass

    return {'title': title,
            'author': author,
            'author_url': author_url,
            'cover_url': cover_url,
            'book_url': book_url,
            'rating': rating,
            'error': error}


# MAIN SCRIPT:
# Read list of books
with open("./references/list_of_books.txt") as f:
    list_of_books = f.read()

list_of_books = list_of_books.split('\n')
list_of_books = [book for book in list_of_books if book]

# Gather information from listed books
books_info = []
for book in list_of_books:
    books_info.append(get_book_info(book))

# Save information into json file
with open("./references/books_info.json", "w") as f:
    json.dump(books_info, f, indent=2)
