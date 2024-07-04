#!/bin/bash

cd ~/book_wishlist
source .venv/bin/activate
python generate_json.py
python generate_page.py

deactivate