import allure


class TestOrder:

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в хедере')
    def test_rent_a_scooter_click_on_button_order_in_header(self, order):
        order.go_to_rental_form_with_button_in_header()
        order.set_first_part_rental_form('Анна', 'Самедова', 'Москва', '89999990000')
        order.set_second_part_rental_form('10.06.2023', 'Хочу самокат')
        order.accept_consent_to_rent_a_scooter()
        order_number = order.check_popup_with_order_number()
        number_on_status_page = order.check_order_number_on_status_page()
        assert order_number == number_on_status_page.get_attribute('value')

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в конце страницы')
    def test_rent_a_scooter_click_on_button_order_in_finish_page(self, order):
        order.go_to_rental_form_with_button_in_finish_page()
        order.set_first_part_rental_form('Вадим', 'Беглов', 'Красноярск', '89999990000')
        order.set_second_part_rental_form('10.06.2023', 'Хочу самокат')
        order.accept_consent_to_rent_a_scooter()
        order_number = order.check_popup_with_order_number()
        number_on_status_page = order.check_order_number_on_status_page()
        assert order_number == number_on_status_page.get_attribute('value')
