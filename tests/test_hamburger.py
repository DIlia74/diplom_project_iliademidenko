import allure
import pytest_check as check
from locators.locators_hamburger import MainPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_auto_ru(web_browser):

    page = MainPage(web_browser)

    page.btn_hamburger.click()
