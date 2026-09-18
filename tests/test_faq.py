"""Проверка текста в FAQ"""

import allure
import pytest

from pages import MainPage
from data import Urls, FAQ_ITEMS

@allure.epic("Самокат")
@allure.feature("FAQ — Вопросы о важном")
class TestFaq:
    """Отдельный тест на каждый вопрос: клик по тексту вопроса → проверка текста ответа."""

    @allure.title("Вопрос FAQ: '{faq_item[question]}' раскрывает корректный ответ")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "faq_item",
        FAQ_ITEMS,
        ids=[item["id"] for item in FAQ_ITEMS],
    )
    def test_faq_answer_is_correct(self, driver, faq_item):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу и принять cookie"):
            main_page.open(Urls.MAIN_PAGE)
            main_page.accept_cookies()

        with allure.step(f"Раскрыть вопрос и проверить ответ: {faq_item['question']}"):
            actual_answer = main_page.get_faq_answer_text(faq_item["question"])
            assert actual_answer == faq_item["answer"], (
                f"Ответ на вопрос '{faq_item['question']}' не совпал.\n"
                f"Ожидалось: {faq_item['answer']}\n"
                f"Получено:  {actual_answer}"
            )


