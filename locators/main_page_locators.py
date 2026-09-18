"""Локаторы для главной страницы"""

from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы главной страницы: точки входа, логотипы, FAQ, cookie."""

    #  Кнопки "Заказать" (две точки входа) 
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[starts-with(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    #  Логотипы 
    LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    #  Cookie 
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # FAQ
    FAQ_QUESTION = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton'][normalize-space(text())='{}']")
    FAQ_ANSWER = (
            By.XPATH,
            "//div[@data-accordion-component='AccordionItemButton']"
            "[normalize-space(text())='{}']"
            "/ancestor::div[@class='accordion__item']"
            "//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]/p",
        )
