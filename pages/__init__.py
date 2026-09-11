"""Пакет Page Object.

Каждая страница сайта представлена отдельным классом-наследником BasePage.
Классы инкапсулируют поведение (действия пользователя), локаторы вынесены
в пакет `locators`.
"""
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage

__all__ = ["BasePage", "MainPage", "OrderPage"]
