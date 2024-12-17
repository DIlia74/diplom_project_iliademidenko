import time

import allure
import pytest_check as check
from locators.locators_search import MainPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_headers(web_browser):

    page = MainPage(web_browser)

    # with allure.step('Проверка поиска по слову'):
    #     page.btn_search.send_keys('Haval')
    #
    #     with allure.step('Нажимаем на поиск'):
    #         page.btn_search.click()
    #
    #     with allure.step('Нажать на подсказку'):
    #         page.btn_podskazka_query.click()
    #
    # with allure.step('Проверяем что перенесло на новую вебстр'):
    #     check.is_true(page.get_current_url(), 'https://auto.ru/cars/haval/all/?query=Haval&from=searchline')

    with allure.step('Проверка кнопки поиска'):
        page.btn_search.click()
        check.equal(page.get_current_url(),'https://www.kpc.by/search')

    with allure.step('Проверка функционала поле инпута'):
        page.input_search.send_keys('принтер')
        page.btn_forsearch.click()

    with allure.step('Проверка переноса по запросу "принтер"'):
        check.is_true(page.get_current_url(), 'https://www.kpc.by/search?search=%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%B5%D1%80&id=65')
