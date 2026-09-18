"""
Оптимизация базовых функций на страницы
"""

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    """Базовый класс со всеми общими обёртками над Selenium."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        """Открыть страницу по url"""
        self.driver.get(url)

    @allure.step("Найти видимый элемент: {locator}")
    def find_element(self, locator):
        """Найти видимый элемент"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти кликабельный элемент: {locator}")
    def find_clickable(self, locator):
        """Найти кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator):
        """Кликнуть по элементу"""
        element = self.find_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            # Что-то перекрыло элемент — кликаем через JS
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def input_text(self, locator, text):
        """Ввести текст в элемент"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text

    @allure.step("Проскроллить к элементу: {locator}")
    def scroll_to_element(self, locator):
        """Проскроллить к элементу"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    @allure.step("Дождаться появления элемента: {locator}")
    def wait_visible(self, locator):
        """Дождаться появления элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self):
        """Переключиться на новую вкладку"""
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    @allure.step("Дождаться, что URL содержит: {expected}")
    def wait_url_contains(self, expected, timeout=10):
        """Дождаться, что URL содержит"""
        WebDriverWait(self.driver, timeout).until(
            lambda d: expected in d.current_url
        )
        return self.driver.current_url

