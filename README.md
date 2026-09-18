# Автотесты для сайта «Самокат»

UI-автотесты для учебного сервиса аренды самокатов [qa-scooter.praktikum-services.ru](https://qa-scooter.praktikum-services.ru/).
Проект написан на **Python** с использованием **Selenium WebDriver**, **Pytest**, **Allure** и **Faker**.

## Содержание

- [Стек](#стек)
- [Структура проекта](#структура-проекта)
- [Требования](#требования)
- [Установка](#установка)
- [Запуск тестов](#запуск-тестов)
- [Allure-отчёт](#allure-отчёт)
- [Покрытие тестами](#покрытие-тестами)
- [Архитектура (Page Object Model)](#архитектура-page-object-model)

## Стек

| Компонент | Назначение |
|---|---|
| Python 3.10+ | Язык разработки |
| Selenium WebDriver | Управление браузером |
| Pytest | Тестовый фреймворк, параметризация, фикстуры |
| Allure | Отчёты и шаги |
| Faker | Генерация тестовых данных |
| webdriver-manager | Автоматическая установка драйверов |

**Тестовый браузер:** Mozilla Firefox (geckodriver).

## Структура проекта

```
project/
├── conftest.py               # Фикстуры: драйвер, данные заказа
├── pytest.ini                # Конфигурация pytest, addopts для Allure
├── requirements.txt          # Зависимости
├── README.md
│
├── data/
│   ├── urls.py               # URL-адреса страниц
│   └── faq.py                # Вопросы и ответы «Вопросы о важном»
│
├── locators/
│   ├── main_page_locators.py # Локаторы главной страницы
│   └── order_page_locators.py# Локаторы формы заказа
│
├── pages/
│   ├── base_page.py          # Базовые методы (клик, ввод, ожидания)
│   ├── main_page.py          # Page Object главной страницы
│   └── order_page.py         # Page Object страницы заказа
│
└── tests/
    ├── test_faq.py           # Тесты выпадающего списка
    └── test_order.py         # Тесты оформления заказа
```

## Требования

- Python 3.10 или новее
- Браузер **Mozilla Firefox**
- `geckodriver` (устанавливается автоматически через `webdriver-manager`)
- Java 8+ — только для локального просмотра Allure-отчёта

## Установка

1. Клонируйте репозиторий:

```bash
git clone <url-репозитория>
cd <папка-проекта>
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Запуск всех тестов:

```bash
pytest
```

Запуск конкретного модуля:

```bash
pytest tests/test_faq.py
pytest tests/test_order.py
```

Запуск одного теста:

```bash
pytest tests/test_order.py::TestOrder::test_create_order_positive
```

Запуск в режиме подробного вывода:

```bash
pytest -v
```

Запуск только тестов с определённой меткой:

```bash
pytest -m regression
```

## Allure-отчёт

1. Запустите тесты — результаты сохранятся в `allure-results` (указано в `../pytest.ini`):

```bash
pytest --alluredir=allure-results --clean-alluredir
```

2. Сгенерируйте HTML-отчёт:

```bash
allure generate allure-results -o allure-report --clean
```

3. Откройте отчёт:

```bash
allure open allure-report
```

Или сразу сгенерировать и открыть во временном сервере:

```bash
allure serve allure-results
```

> Каталоги `allure-results` и `allure-report` не коммитятся в репозиторий (см. `../.gitignore`).

## Покрытие тестами

### 1. Выпадающий список «Вопросы о важном»

Проверяется, что при клике на стрелку вопроса раскрывается соответствующий текст ответа.

- Отдельный тест на **каждый** вопрос реализован через параметризацию `@pytest.mark.parametrize`.
- Источник данных — `data/faq.py`.

### 2. Заказ самоката (позитивный сценарий)

Проверяется полный флоу:

1. Точка входа — кнопка «Заказать» вверху страницы или внизу (обе проверяются).
2. Заполнение формы заказа (имя, фамилия, адрес, станция метро, телефон, дата, срок аренды, цвет, комментарий).
3. Появление всплывающего окна об успешном создании заказа.
4. Переход на главную страницу «Самоката» при клике на логотип «Самокат».
5. Открытие главной страницы Дзена в новой вкладке при клике на логотип Яндекса.

Тесты с двумя наборами данных генерируются Faker и передаются через фикстуру `order_data_sets` со `scope="session"` — это позволяет не дублировать сценарий для каждой точки входа.

## Архитектура (Page Object Model)

Проект построен по паттерну **Page Object Model**:

- **Locators** — только селекторы, без логики. Разбиты по страницам.
- **Pages** — классы страниц с методами, описывающими действия пользователя. Наследуются от `BasePage`.
- **BasePage** — общие операции: `click`, `input_text`, `find_element`, `wait_visible`, единые явные ожидания.
- **Tests** — только сценарии и ассерты, без локаторов и Selenium API.

Пример использования:

```python
def test_create_order_positive(self, driver, entry_method, entry_title, order_data):
    main_page = MainPage(driver)
    main_page.accept_cookies()

    order_page = main_page.click_order_button(entry_method)
    order_page.fill_order_form(order_data)
    assert order_page.is_success_modal_visible()
```

