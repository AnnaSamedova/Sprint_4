import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from page_objects.navigation_page import NavigationPageScooter
from page_objects.order_page import OrderPageScooter
from page_objects.questions_page import QuestionsPageScooter

url = 'https://qa-scooter.praktikum-services.ru/'


@pytest.fixture()
def browser():
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--window-size=900,600')
    browser = webdriver.Firefox(options=firefox_options)
    yield browser
    browser.quit()


@pytest.fixture()
def questions(browser):
    return QuestionsPageScooter(browser, url)


@pytest.fixture()
def order(browser):
    return OrderPageScooter(browser, url)


@pytest.fixture()
def navigation(browser):
    return NavigationPageScooter(browser, url)
