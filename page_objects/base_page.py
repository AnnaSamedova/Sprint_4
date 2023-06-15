import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    cookie = (By.XPATH, './/button[@id="rcc-confirm-button"]')

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Переход на сайт')
    def go_to_site(self):
        return self.driver.get(self.url)

    @allure.step('Поиск элемента на странице с ожиданием')
    def find_element_located(self, locator, time=120):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Поиск элементов на странице с ожиданием')
    def find_elements_located(self, locator, time=120):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Принять куки')
    def cookie_accept(self):
        self.find_element_located(BasePage.cookie).click()

    @allure.step('Нажать на элемент')
    def click_on_any_element(self, locator):
        self.find_element_located(locator).click()
