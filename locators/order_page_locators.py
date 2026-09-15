"""Локаторы для страницы оформления заказа"""

from selenium.webdriver.common.by import By

class OrderPageLocators:
    """Локаторы страницы заказа: форма клиента, форма аренды, модального окна."""

    # --- Форма 1: данные пользователя ---
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.CLASS_NAME, "select-search__row")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # --- Форма 2: про аренду ---
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    PERIOD_OPTION = (By.CLASS_NAME, "Dropdown-option")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_SUBMIT_BUTTON = (
        By.XPATH,
        "//div[starts-with(@class, 'Order_Buttons')]/button[text()='Заказать']",
    )

    # --- Модальные окна подтверждения оформления заказа ---
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[starts-with(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
