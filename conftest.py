"""
Настройка фикстур
"""
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from data import generate_order_data


@pytest.fixture()
def driver():
    """Фикстура WebDriver для Mozilla Firefox с автоустановкой geckodriver."""
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def order_data_sets():
    """Генерирует два уникальных набора данных на каждую тестовую сессию."""
    return [generate_order_data(), generate_order_data()]