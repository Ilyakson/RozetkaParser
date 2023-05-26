import os
import time

import django
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoParser.settings")
django.setup()

from app.models import Keyword, Link


def parse_links():
    """Функція для парсингу посилань на товари та збереження їх у базу даних."""
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)

    keywords = Keyword.objects.exclude(status="complete")

    for keyword in keywords:
        search_query = keyword.name

        driver.get("https://rozetka.com.ua/")

        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='search']"))
        )
        search_input.send_keys(search_query)

        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'search-form__submit')]"))
        )
        search_button.click()

        time.sleep(3)

        seller_filter = driver.find_element(By.CSS_SELECTOR, "div[data-filter-name='seller'] a.checkbox-filter__link[data-id='Rozetka']")
        seller_filter.click()

        time.sleep(3)

        while True:
            elements = driver.find_elements(By.CLASS_NAME, "goods-tile__heading")

            for element in elements:
                link_url = element.get_attribute("href")
                link_name = element.text.strip()

                link = Link(name=link_name, link=link_url, status="Not Parsed")
                link.save()
            try:
                next_page_button = driver.find_element(
                    By.XPATH, "/html/body/app-root/div/div/rz-search/rz-catalog/div/div["
                              "2]/section/rz-catalog-paginator/app-paginator/div/a[2]")
            except:
                break
            if "disabled" in next_page_button.get_attribute("class"):
                break

            next_page_button.click()

            time.sleep(3)
        keyword.status = "complete"
        keyword.save()
    driver.quit()


parse_links()
