import json
from jinja2 import Environment, FileSystemLoader

# Load JSON data from file
with open('./references/books_info.json', 'r') as file:
    books = json.load(file)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('./references/template.html')

# Render the template with data
output = template.render(books=books)

# Save the rendered HTML to a file
with open('books_wishlist.html', 'w') as file:
    file.write(output)
