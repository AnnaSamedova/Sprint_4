import time

import allure
from page_objects.questions_page import QuestionsPageScooter


class TestQuestions:

    @allure.title('Проверка активности аккордеон панели')
    def test_click_on_all_elements_in_accordion_panel_section_questions(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        assert questions.click_on_all_elements_accordion_panel_section_questions()

    @allure.title('Проверка вопроса о стоимости и способах оплаты самоката')
    def test_click_on_question_price_and_payment(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        questions.click_on_element_in_accordion_panel_section_questions(QuestionsPageScooter.question_price_and_payment)
        answer = questions.check_answer_on_question_in_accordion_panel(QuestionsPageScooter.answer_price_and_payment)
        assert answer == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title('Проверка вопроса о возможности заказа нескольких самокатов')
    def test_click_on_question_multiple_scooter(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        questions.click_on_element_in_accordion_panel_section_questions(QuestionsPageScooter.question_multiple_scooter)
        answer = questions.check_answer_on_question_in_accordion_panel(QuestionsPageScooter.answer_multiple_scooter)
        assert answer == ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с "
                          "друзьями, можете просто сделать несколько заказов — один за другим.")

    @allure.title('Проверка вопроса о времени аренды самоката')
    def test_click_on_question_scooter_rental_time(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        questions.click_on_element_in_accordion_panel_section_questions(QuestionsPageScooter.question_rental_time)
        answer = questions.check_answer_on_question_in_accordion_panel(QuestionsPageScooter.answer_rental_time)
        assert answer == ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение "
                          "дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ "
                          "курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится"
                          " 9 мая в 20:30.")

    @allure.title('Проверка вопроса о дате аренды самоката')
    def test_click_on_question_scooter_rental_date(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        questions.click_on_element_in_accordion_panel_section_questions(QuestionsPageScooter.question_rental_date)
        answer = questions.check_answer_on_question_in_accordion_panel(QuestionsPageScooter.answer_rental_date)
        assert answer == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title('Проверка вопроса о возможности продления и возврата самоката')
    def test_click_on_question_extend_order(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        questions.click_on_element_in_accordion_panel_section_questions(QuestionsPageScooter.question_extend_order)
        answer = questions.check_answer_on_question_in_accordion_panel(QuestionsPageScooter.answer_extend_order)
        assert answer == ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку "
                          "по красивому номеру 1010.")

    @allure.title('Проверка вопроса о зарядке самоката')
    def test_click_on_question_scooter_charging(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        questions.click_on_element_in_accordion_panel_section_questions(QuestionsPageScooter.question_scooter_charging)
        answer = questions.check_answer_on_question_in_accordion_panel(QuestionsPageScooter.answer_scooter_charging)
        assert answer == ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — "
                          "даже если будете кататься без передышек и во сне. Зарядка не понадобится.")

    @allure.title('Проверка вопроса об отмене заказа')
    def test_click_on_question_cancel_order(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        questions.click_on_element_in_accordion_panel_section_questions(QuestionsPageScooter.question_cancel_order)
        answer = questions.check_answer_on_question_in_accordion_panel(QuestionsPageScooter.answer_cancel_order)
        assert answer == ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже "
                          "не попросим. Все же свои.")

    @allure.title('Проверка вопроса о доставке самоката')
    def test_click_on_question_scooter_delivery(self, questions):
        questions.go_to_accordion_panel_in_section_questions()
        questions.click_on_element_in_accordion_panel_section_questions(QuestionsPageScooter.question_scooter_delivery)
        answer = questions.check_answer_on_question_in_accordion_panel(QuestionsPageScooter.answer_scooter_delivery)
        assert answer == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
