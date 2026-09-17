"""Главная страница"""

import allure
from selenium.common.exceptions import TimeoutException

from pages import BasePage
from locators import MainPageLocators as Loc, MainPageLocators


class MainPage(BasePage):
    """Главная страница Самоката: точки входа в заказ, FAQ, логотипы."""

    @staticmethod
    def get_locator_faq_question(question_text):
        """Кнопка вопроса FAQ по её тексту."""
        by, value = MainPageLocators.FAQ_QUESTION
        return by, value.format(question_text)

    @staticmethod
    def get_locator_faq_answer(question_text):
        """Абзац ответа именно у раскрытой (без hidden) панели."""
        by, value = MainPageLocators.FAQ_ANSWER
        return by, value.format(question_text)

    @allure.step("Принять cookie")
    def accept_cookies(self):
        """Принять cookie"""
        try:
            self.find_clickable(Loc.COOKIE_BUTTON).click()
        except TimeoutException:
            pass

    @allure.step("Нажать кнопку 'Заказать' вверху страницы")
    def click_order_button_top(self):
        """Нажать кнопку 'Заказать' вверху страницы"""
        self.click(Loc.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' внизу страницы")
    def click_order_button_bottom(self):
        """Нажать кнопку 'Заказать' внизу страницы"""
        self.click(Loc.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть по вопросу FAQ №{index}")
    def click_faq_question(self, index):
        """Кликнуть по вопросу FAQ"""
        locator = self.get_locator_faq_question(index)
        self.scroll_to_element(locator)
        self.click(locator)

    @allure.step("Раскрыть вопрос и получить текст ответа: {question_text}")
    def get_faq_answer_text(self, question_text):
        """Раскрыть вопрос и получить текст ответа"""
        # Скроллим и кликаем по вопросу
        question_locator = self.get_locator_faq_question(question_text)
        self.scroll_to_element(question_locator)
        self.click(question_locator)

        # Явно ждём видимости раскрытой панели (без @hidden)
        answer_locator = self.get_locator_faq_answer(question_text)
        return self.wait_visible(answer_locator).text

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_scooter_logo(self):
        """Кликнуть по логотипу 'Самокат'"""
        self.click(Loc.LOGO_SCOOTER)

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        """Кликнуть по логотипу 'Яндекс'"""
        self.click(Loc.LOGO_YANDEX)


