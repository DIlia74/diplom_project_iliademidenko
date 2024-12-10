import allure
from locators.locators_main_page.locators_search import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_auto_ru(web_browser):

    page = MainPage(web_browser)


