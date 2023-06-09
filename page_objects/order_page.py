from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import allure


class OrderPageScooter(BasePage):

    button_order_in_header = (By.XPATH, './/div[contains(@class, "Header_Nav__AGCXC")]/button[contains(text(), "Заказать")]')
    button_order_two = (By.XPATH, './/div[contains(@class, "Home_FinishButton__1_cWm")]/button[contains(text(), "Заказать")]')
    field_name = (By.XPATH, './/input[contains(@placeholder, "* Имя")]')
    field_surname = (By.XPATH, './/input[contains(@placeholder, "* Фамилия")]')
    field_address = (By.XPATH, './/input[contains(@placeholder, "* Адрес")]')
    select_metro_station = (By.XPATH, './/div[contains(@class, "select-search__value")]/input[contains(@placeholder, "* Станция метро")]')
    list_metro_station = (By.XPATH, './/div[contains(@class, "select-search__select")]/ul[contains(@class, "select-search__options")]')
    element_list_metro_station = (By.XPATH, './/li[@data-value="1"]/button[@value="1"]')
    field_phone = (By.XPATH, './/input[contains(@placeholder, "* Телефон")]')
    button_next = (By.XPATH, './/button[contains(@class, "Button_Button__ra12g") and contains(text(), "Далее")]')
    field_calendar = (By.XPATH, './/input[contains(@placeholder, "* Когда привезти самокат")]')
    field_rental_period = (By.XPATH, './/div[contains(@class, "Dropdown-control")]/div[contains(text(), "* Срок аренды")]')
    option_dropdown_menu = (By.XPATH, './/div[contains(@class, "Dropdown-menu")]/div[1]')
    checkbox_scooter_color_grey = (By.XPATH, './/input[contains(@id, "grey")]')
    checkbox_scooter_color_black = (By.XPATH, './/input[contains(@id, "black")]')
    field_comment = (By.XPATH, './/input[contains(@placeholder, "Комментарий для курьера")]')
    button_order_scooter = (By.XPATH, './/div[contains(@class, "Order_Buttons__1xGrp")]/button[contains(text(), "Заказать")]')
    popup_agreement = (By.XPATH, './/div[contains(@class, "Order_Buttons__1xGrp")]/button[contains(text(), "Да")]')
    popup_order_is_processed_text = (By.XPATH, './/div[contains(@class, "Order_Text__2broi")]')
    button_check_status_order = (By.XPATH, './/div[contains(@class, "Order_NextButton__1_rCA")]/button[contains(text(), "Посмотреть статус")]')
    field_with_number_order = (By.XPATH, './/input[contains(@class, "Input_Input") and contains(@class, "Input_Filled")]')

    @allure.step('Нажать на кнопку заказа самоката')
    def click_on_button_order(self, locator):
        self.find_element_located(locator).click()

    @allure.step('Заполнить поле в форме заказа самоката')
    def set_field_in_the_rental_form(self, locator, value):
        field = self.find_element_located(locator)
        field.send_keys(value)
        field.send_keys(Keys.ENTER)

    @allure.step('Выбрать в списке станций метро - станцию метро')
    def set_select_metro_station_in_the_rental_form(self):
        self.find_element_located(OrderPageScooter.select_metro_station).click()
        self.find_element_located(OrderPageScooter.list_metro_station)
        self.find_element_located(OrderPageScooter.element_list_metro_station).click()

    @allure.step('Нажать на кнопку "Далее"')
    def click_on_button_next(self):
        self.find_element_located(OrderPageScooter.button_next).click()

    @allure.step('Выбрать срок аренды самоката в выпадающем списке поля')
    def set_dropdown_menu_in_rental_form(self):
        self.find_element_located(OrderPageScooter.field_rental_period).click()
        self.find_element_located(OrderPageScooter.option_dropdown_menu).click()

    @allure.step('Выбрать чекбокс цвета самоката')
    def set_checkbox_scooter_color_in_rental_form(self):
        self.find_element_located(OrderPageScooter.checkbox_scooter_color_grey).click()

    @allure.step('Нажать на кнопку оформления заказа')
    def click_on_button_order_scooter(self):
        self.find_element_located(OrderPageScooter.button_order_scooter).click()

    @allure.step('В попапе "Хотите оформить заказ" нажать кнопку согласия')
    def click_on_button_in_popup_agreement_yes(self):
        self.find_element_located(OrderPageScooter.popup_agreement).click()

    @allure.step('Получить номер заказа из всплывающего окна успешного оформления заказа')
    def check_popup_with_order_number(self):
        text_order = self.find_element_located(OrderPageScooter.popup_order_is_processed_text).text
        number_order = ''
        for number in text_order:
            if number.isdigit():
                number_order += number
        return number_order

    @allure.step('Получить номер заказа на странице с информацией и статусами заказа')
    def check_order_number_on_status_page(self):
        self.find_element_located(OrderPageScooter.button_check_status_order).click()
        number_on_status_page = self.find_element_located(OrderPageScooter.field_with_number_order)
        return number_on_status_page

    @allure.step('Перейти к форме аренды самоката по кнопке "Заказать" в хедере')
    def go_to_rental_form_with_button_in_header(self):
        self.go_to_site()
        self.cookie_accept()
        self.click_on_button_order(OrderPageScooter.button_order_in_header)

    @allure.step('Перейти к форме аренды самоката по кнопке "Заказать" в конце страницы')
    def go_to_rental_form_with_button_in_finish_page(self):
        self.go_to_site()
        self.cookie_accept()
        self.click_on_button_order(OrderPageScooter.button_order_two)

    @allure.step('Заполнить все поля первой части анкеты - имя, фамилия, адрес, метро, номер телефона')
    def set_first_part_rental_form(self, name, surname, address, phone):
        self.set_field_in_the_rental_form(OrderPageScooter.field_name, name)
        self.set_field_in_the_rental_form(OrderPageScooter.field_surname, surname)
        self.set_field_in_the_rental_form(OrderPageScooter.field_address, address)
        self.set_select_metro_station_in_the_rental_form()
        self.set_field_in_the_rental_form(OrderPageScooter.field_phone, phone)
        self.click_on_button_next()

    @allure.step('Заполнить все поля второй части анкеты - дата, срок, цвет, комментарий')
    def set_second_part_rental_form(self, date, comment):
        self.set_field_in_the_rental_form(OrderPageScooter.field_calendar, date)
        self.set_dropdown_menu_in_rental_form()
        self.set_checkbox_scooter_color_in_rental_form()
        self.set_field_in_the_rental_form(OrderPageScooter.field_comment, comment)

    @allure.step('Продолжить и согласиться оформить заказ')
    def accept_consent_to_rent_a_scooter(self):
        self.click_on_button_order_scooter()
        self.click_on_button_in_popup_agreement_yes()
