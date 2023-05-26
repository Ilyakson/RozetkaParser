import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoParser.settings")
django.setup()

from app.models import Link, Info


def parse_product_page():
    """Функція для парсингу сторінки товару та збереження даних у базі даних."""
    product_links = Link.objects.exclude(status="complete")
    current_link = 0
    for link in product_links:
        response = requests.get(link.link + "characteristics/")

        if response.status_code != 200:
            print(f"Помилка при отриманні сторінки товару: {response.status_code}")
            return
        diagonal_value = None
        sim_value = None
        storage_value = None
        front_camera_value = None
        main_camera_value = None

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("h1", class_="product__title").text

        try:
            price_element = soup.find("p", class_="product-carriage__price").text
        except AttributeError:
            price_element = "No have price"

        try:
            reviews_count = soup.find("span", class_="tabs__link-text ng-star-inserted").text
        except AttributeError:
            reviews_count = 0

        try:
            diagonal_element = soup.find("span", string="Діагональ екрана")
            diagonal_value = diagonal_element.find_next("a").text.strip()
        except AttributeError:
            pass

        try:
            sim_element = soup.find("span", string="Кількість SIM-карток")
            sim_value = sim_element.find_next("a").text.strip()
        except AttributeError:
            pass

        try:
            storage_element = soup.find("span", string="Вбудована пам'ять")
            storage_value = storage_element.find_next("a").text.strip()
        except AttributeError:
            pass

        try:
            front_camera_element = soup.find("span", string="Фронтальна камера")
            front_camera_value = front_camera_element.find_next("a").text.strip()
        except AttributeError:
            pass

        try:
            main_camera_element = soup.find("span", string="Основна камера")
            main_camera_value = main_camera_element.find_next("a").text.strip()
        except AttributeError:
            pass

        info = Info(
            product_name=title,
            price=price_element,
            link=link.link,
            reviews=reviews_count,
            screen_diagonal=diagonal_value,
            sim_card_count=sim_value,
            built_in_memory=storage_value,
            front_camera=front_camera_value,
            main_camera=main_camera_value,
        )
        info.save()
        link.status = "complete"
        link.save()
        current_link += 1
        if current_link == 100:
            current_link = 0
            break


parse_product_page()
