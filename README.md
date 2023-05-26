# Django Parser

Django Parser is a web scraping tool built with Django framework that extracts product information from an e-commerce website and stores it in a database. It uses Selenium and BeautifulSoup libraries for web scraping and Django ORM for database operations.

## Installation

```shell
git clone https://github.com/Ilyakson/RozetkaParser.git
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python parse_links.py
python parse_product_info.py
```