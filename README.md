# book_wishlist
A scraper and static page generator for my books wishlist.
The scrapping is done from goodreads.com, based on a txt file with a list of books.

## Generate json
Use `generate_json.py` to generate the json file based on the "list_of_books.txt" file.
Each line of that file will be used as a search query in goodreads, with the first search result being used for each of them.

## Generate page
Use `generate_page.py` to generate an html page with a grid of the books that are contained in the books_info.json file, generated in the previous step.
You can then deploy this html page wherever you would like.