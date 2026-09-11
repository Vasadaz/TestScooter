"""Страница оформления заказа"""

import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators import OrderPageLocators as Loc

class OrderPage(BasePage):
    """Страница заказа: две формы (данные клиента + аренда) и модального окна подтверждения."""

    # ---------- Форма 1 ----------
    @allure.step("Заполнить форму с данными пользователя")
    def fill_user_form(self, name, surname, address, metro_index, phone):
        """Заполнить форму с данными пользователя"""
        self.input_text(Loc.NAME_FIELD, name)
        self.input_text(Loc.SURNAME_FIELD, surname)
        self.input_text(Loc.ADDRESS_FIELD, address)
        self._select_metro(metro_index)
        self.input_text(Loc.PHONE_FIELD, phone)

    @allure.step("Выбрать станцию метро (индекс {metro_index})")
    def _select_metro(self, metro_index):
        """Выбрать станцию метро"""
        self.click(Loc.METRO_FIELD)
        options = self.wait.until(lambda d: d.find_elements(*Loc.METRO_OPTION))
        options[metro_index].click()

    @allure.step("Нажать 'Далее'")
    def click_next(self):
        """Нажать кнопку 'Далее'"""
        self.click(Loc.NEXT_BUTTON)

    # ---------- Форма 2 ----------
    @allure.step("Заполнить форму аренды")
    def fill_order_form(self, date, period_index, color, comment):
        """Заполнить форму аренды"""
        self._set_date(date)
        self._select_period(period_index)
        self._select_color(color)
        self.input_text(Loc.COMMENT_FIELD, comment)

    @allure.step("Указать дату доставки: {date}")
    def _set_date(self, date):
        self.input_text(Loc.DATE_FIELD, date)
        self.find_element(Loc.DATE_FIELD).send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды (индекс {period_index})")
    def _select_period(self, period_index):
        self.click(Loc.PERIOD_DROPDOWN)
        options = self.wait.until(lambda d: d.find_elements(*Loc.PERIOD_OPTION))
        options[period_index].click()

    @allure.step("Выбрать цвет: {color}")
    def _select_color(self, color):
        locator = Loc.COLOR_BLACK if color == "black" else Loc.COLOR_GREY
        self.click(locator)

    @allure.step("Нажать 'Заказать' в форме")
    def click_submit_order(self):
        """Нажать кнопку 'Заказать' в форме"""
        self.click(Loc.ORDER_SUBMIT_BUTTON)

    @allure.step("Подтвердить заказ (кнопка 'Да')")
    def confirm_order(self):
        """Подтвердить заказ (кнопка 'Да')"""
        self.click(Loc.CONFIRM_YES_BUTTON)

    @allure.step("Проверить появление модального окна об успешном заказе")
    def is_success_modal_visible(self):
        """Проверить появление модального окна об успешном заказе"""
        return self.wait_visible(Loc.SUCCESS_MODAL).is_displayed()

    # ---------- Полный флоу ----------
    @allure.step("Оформить заказ целиком по набору данных")
    def create_order(self, data):
        """Оформить заказ"""
        self.fill_user_form(
            data["name"], data["surname"], data["address"],
            data["metro"], data["phone"],
        )
        self.click_next()
        self.fill_order_form(
            data["date"], data["period"], data["color"], data["comment"],
        )
        self.click_submit_order()
        self.confirm_order()
