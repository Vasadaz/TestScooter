"""Локаторы для главной страницы"""

from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы главной страницы: точки входа, логотипы, FAQ, cookie."""

    # --- Кнопки "Заказать" (две точки входа) ---
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[starts-with(@class, 'Home_FinishButton')]/button[text()='Заказать']",
    )

    # --- Логотипы ---
    LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    # --- Cookie ---
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @staticmethod
    def faq_question(question_text):
        """Кнопка вопроса FAQ по её тексту."""
        return (
            By.XPATH,
            f"//div[@data-accordion-component='AccordionItemButton']"
            f"[normalize-space(text())='{question_text}']",
        )

    @staticmethod
    def faq_answer(question_text):
        """Абзац ответа именно у раскрытой (без hidden) панели."""
        return (
            By.XPATH,
            f"//div[@data-accordion-component='AccordionItemButton']"
            f"[normalize-space(text())='{question_text}']"
            f"/ancestor::div[@class='accordion__item']"
            f"//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]/p",
        )

