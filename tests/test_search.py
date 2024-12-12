import time

import allure
import pytest_check as check
from locators.locators_search import MainPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_headers(web_browser):

    page = MainPage(web_browser)

    with allure.step('Проверка поиска по слову'):
        page.btn_search.send_keys('Haval')

        with allure.step('Нажимаем на поиск'):
            page.btn_search.click()

        with allure.step('Нажать на подсказку'):
            page.btn_podskazka_query.click()

    with allure.step('Проверяем что перенесло на новую вебстр'):
        check.is_true(page.get_current_url(), 'https://auto.ru/cars/haval/all/?query=Haval&from=searchline')
