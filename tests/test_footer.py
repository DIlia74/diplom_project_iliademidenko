import allure
import pytest_check as check
from locators.locators_footer import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_auto_ru(web_browser):

    page = MainPage(web_browser)

    elements = [(page.btn_moscow, 'Москва','https://auto.ru/moskva/'),
                (page.btn_saint_petersburg,'Санкт-Петербург','https://auto.ru/sankt-peterburg/'),
                (page.btn_vladimir,'Владимир','https://auto.ru/vladimir/'),
                (page.btn_volgograd,'Волгоград','https://auto.ru/volgograd/'),
                (page.btn_voronezh,'Воронеж','https://auto.ru/voronezh/'),
                (page.btn_ekaterinburg,'Екатеринбург','https://auto.ru/ekaterinburg/')
                ]

    for element, text_element, url_elements in elements:
        with allure.step('Тест проверки правильного URL при переходе'):
            element.click()
            check.equal(page.get_current_url(), url_elements)

        with allure.step('Тест проверки отображения на экране'):
            check.is_true(element.is_visible())

        with allure.step('Тест проверки кликабельности'):
            check.is_true(element.is_clickable())