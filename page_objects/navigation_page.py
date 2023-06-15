from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
import allure


class NavigationPageScooter(BasePage):

    logo_scooter = (By.XPATH, './/img[@alt = "Scooter"]')
    logo_yandex = (By.XPATH, './/img[@alt = "Yandex"]')
    button_order_in_header = (By.XPATH, './/button[@class = "Button_Button__ra12g"]')
    element_home_page = (By.XPATH, './/div[contains(@class, "Home_Header__iJKdX")]')
    logo_dzen = (By.XPATH, './/a[(@aria-label = "Логотип Дзен") and contains(@href, "https://dzen.ru/")]')

    @allure.step('Нажать на логотип "Самокат"')
    def click_on_logo_scooter(self):
        self.find_element_located(NavigationPageScooter.logo_scooter).click()

    @allure.step('Найти элемент на главной странице сайта "Яндекс"')
    def find_element_home_page(self):
        return self.find_element_located(NavigationPageScooter.element_home_page)

    @allure.step('Нажать на логотип "Яндекс"')
    def click_on_logo_yandex(self):
        yandex_logo = self.find_element_located(NavigationPageScooter.logo_yandex)
        yandex_logo.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(NavigationPageScooter.logo_dzen))
        url_yandex = self.driver.current_url
        return url_yandex

    @allure.step('Перейти на форму аренды самоката')
    def go_to_rental_form(self):
        self.find_element_located(NavigationPageScooter.button_order_in_header).click()

    @allure.step('Перейти на сайт "Яндекс.Самокат" и принять куки')
    def go_to_on_page_scooter(self):
        self.go_to_site()
        self.cookie_accept()

    @allure.step('Проверить навигацию, нажав на логотип "Самокат"')
    def go_to_on_home_page_scooter(self):
        self.go_to_rental_form()
        self.click_on_logo_scooter()
