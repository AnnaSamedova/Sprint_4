import allure


class TestNavigation:

    @allure.title('Проверка перехода на главную страницу сайта "Яндекс.Самокат"')
    def test_check_navigation_click_on_logo_scooter(self, navigation):
        navigation.go_to_on_page_scooter()
        navigation.go_to_on_home_page_scooter()
        assert navigation.find_element_home_page()

    @allure.title('Проверка перехода на сайт страницу "Яндекс"')
    def test_check_navigation_click_on_logo_yandex(self, navigation):
        navigation.go_to_on_page_scooter()
        url_yandex = navigation.click_on_logo_yandex()
        assert url_yandex == "https://dzen.ru/?yredirect=true"
