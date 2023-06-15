from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import allure


class QuestionsPageScooter(BasePage):

    exit_accordion_panel = (By.CLASS_NAME, 'accordion__heading')
    open_accordion_panel = (By.XPATH, './/div[@aria-disabled="true"]')

    question_price_and_payment = (By.XPATH, './/div[@id="accordion__heading-0"]')
    answer_price_and_payment = (By.XPATH, './/div[@id="accordion__panel-0"]/p')

    question_multiple_scooter = (By.XPATH, './/div[@id = "accordion__heading-1"]')
    answer_multiple_scooter = (By.XPATH, './/div[@id="accordion__panel-1"]/p')

    question_rental_time = (By.XPATH, './/div[@id = "accordion__heading-2"]')
    answer_rental_time = (By.XPATH, './/div[@id="accordion__panel-2"]/p')

    question_rental_date = (By.XPATH, './/div[@id = "accordion__heading-3"]')
    answer_rental_date = (By.XPATH, './/div[@id="accordion__panel-3"]/p')

    question_extend_order = (By.XPATH, './/div[@id = "accordion__heading-4"]')
    answer_extend_order = (By.XPATH, './/div[@id="accordion__panel-4"]/p')

    question_scooter_charging = (By.XPATH, './/div[@id = "accordion__heading-5"]')
    answer_scooter_charging = (By.XPATH, './/div[@id="accordion__panel-5"]/p')

    question_cancel_order = (By.XPATH, './/div[@id = "accordion__heading-6"]')
    answer_cancel_order = (By.XPATH, './/div[@id="accordion__panel-6"]/p')

    question_scooter_delivery = (By.XPATH, './/div[@id = "accordion__heading-7"]')
    answer_scooter_delivery = (By.XPATH, './/div[@id="accordion__panel-7"]/p')

    @allure.step('Скролл к разделу "Вопросы о важном"')
    def scroll_to_section_questions(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    @allure.step('Клик на все вопросы в аккордеон панели (цикл) раздела "Вопросы о важном"')
    def click_on_all_elements_accordion_panel_section_questions(self):
        accordion_panels = self.find_elements_located(QuestionsPageScooter.exit_accordion_panel)
        for accordion in accordion_panels:
            accordion.click()
        return QuestionsPageScooter.open_accordion_panel

    @allure.step('Клик на вопрос в аккордеон панели раздела "Вопросы о важном"')
    def click_on_element_in_accordion_panel_section_questions(self, locator_question):
        self.find_element_located(locator_question).click()

    @allure.step('Просмотр ответа на вопрос в аккордеон панели раздела "Вопросы о важном"')
    def check_answer_on_question_in_accordion_panel(self, locator_answer):
        answer_accordion_panel = self.find_element_located(locator_answer).text
        return answer_accordion_panel

    @allure.step('Переход к аккордеон панели в разделе "Вопросы о важном"')
    def go_to_accordion_panel_in_section_questions(self):
        self.go_to_site()
        self.cookie_accept()
        self.scroll_to_section_questions()
