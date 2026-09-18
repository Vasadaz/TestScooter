"""
Тесты для страницы оформления заказа
"""

import allure
import pytest

from pages import MainPage, OrderPage
from data import Urls

@allure.epic("Самокат")
@allure.feature("Заказ самоката")
class TestOrder:
    """Позитивный сценарий заказа с двумя точками входа и двумя наборами данных."""

    # Параметризация точек входа: метод входа + удобное имя
    ENTRY_POINTS = [
        ("top", "Кнопка 'Заказать' вверху страницы"),
        ("bottom", "Кнопка 'Заказать' внизу страницы"),
    ]

    @allure.title("Позитивный заказ: вход через '{entry_title}', набор данных #{data_index}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("data_index", [0, 1], ids=["data_set_1", "data_set_2"])
    @pytest.mark.parametrize(
        "entry_method,entry_title",
        ENTRY_POINTS,
        ids=["entry_top", "entry_bottom"],
    )
    def test_create_order_positive(self, driver, entry_method, entry_title, data_index, order_data_sets):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_data = order_data_sets[data_index]

        with allure.step("Открыть главную страницу и принять cookie"):
            main_page.open(Urls.MAIN_PAGE)
            main_page.accept_cookies()

        with allure.step(f"Войти в сценарий: {entry_title}"):
            if entry_method == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()

        with allure.step("Оформить заказ по набору данных"):
            order_page.create_order(order_data)

        with allure.step("Проверить всплывающее окно об успешном создании заказа"):
            assert order_page.is_success_modal_visible(), (
                "Модальное окно об успешном заказе не появилось"
            )

@allure.epic("Самокат")
@allure.feature("Навигация по логотипам")
class TestLogoNavigation:
    """Проверка переходов по логотипам Самоката и Яндекса."""

    @allure.title("Клик по логотипу 'Самокат' ведёт на главную страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть страницу заказа"):
            main_page.open(Urls.ORDER_PAGE)
            main_page.accept_cookies()

        with allure.step("Кликнуть по логотипу 'Самокат'"):
            main_page.click_scooter_logo()

        with allure.step("Проверить переход на главную страницу"):
            assert main_page.get_current_url() in Urls.MAIN_PAGE, (
                f"Ожидался URL {Urls.MAIN_PAGE}, получен {main_page.get_current_url()}"
            )

    @allure.title("Клик по логотипу 'Яндекс' открывает Дзен в новой вкладке")
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open(Urls.MAIN_PAGE)
            main_page.accept_cookies()

        with allure.step("Кликнуть по логотипу 'Яндекс'"):
            main_page.click_yandex_logo()

        with allure.step("Переключиться на новую вкладку и дождаться загрузки Дзена"):
            main_page.switch_to_new_window()
            main_page.wait_url_contains(Urls.DZEN_PAGE)

        with allure.step("Проверить, что открылся Дзен"):
            assert Urls.DZEN_PAGE in main_page.get_current_url(), (
                f"Ожидался Дзен, получен {main_page.get_current_url()}"
            )
