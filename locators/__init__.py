"""Пакет локаторов.

Локаторы отделены от поведения страниц (чистый POM): при изменении вёрстки
правки вносятся только здесь, не затрагивая логику в пакете `pages`.
"""
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

__all__ = ["MainPageLocators", "OrderPageLocators"]
