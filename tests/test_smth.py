import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки колличества плиток в блоке "Подберите свое решение"')

def test_site(web_browser):
    page = MainPage(web_browser)

    check.is_true(page.hdh.is_visible())