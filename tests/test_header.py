import allure
import pytest_check as check
from locators.locators_main_page.locators_header import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_auto_ru(web_browser):

    page = MainPage(web_browser)

    elements = [(page.btn_cars,'Легковые','https://auto.ru/cars/all/'),
                (page.btn_commercial,'Коммерческие','https://auto.ru/lcv/all/'),
                (page.btn_electro,'Электро','https://auto.ru/electro/'),
                (page.btn_chinese,'Китайские','https://auto.ru/catalog/cars/chinese/'),
                (page.btn_moto,'Мото','https://auto.ru/motorcycle/all/'),
                (page.btn_history,'Отчёты','https://auto.ru/history/'),
                (page.btn_cars_otchet,'Выкуп','https://auto.ru/buyout/'),
                (page.btn_insurance,'Кредиты','https://auto.ru/promo/finance/'),
                (page.btn_ocenka_auto,'Оценка авто','https://auto.ru/evaluation/cars/'),
                (page.btn_strahovka,'Страховки','https://auto.ru/promo/osago-tbank/'),
                (page.btn_dealers,'Гараж','https://auto.ru/garage/'),
                (page.btn_journals,'Журнал','https://auto.ru/mag/'),
                (page.btn_for_biznes,'Для бизнеса','https://business.auto.ru/')
                        ]
    for element, text_element, url_elements in elements:
        with allure.step('Тест проверки правильного URL при переходе'):
            element.click()
            check.equal(page.get_current_url(), url_elements)

        with allure.step('Тест проверки отображения на экране'):
            check.is_true(element.is_visible())

        with allure.step('Тест проверки кликабельности'):
            check.is_true(element.is_clickable())

        # with allure.step('Тест проверки на орфографию'):
        #     check.equal(element.get_text(), text_element)
        #
        #  with allure.step('Тест проверки на правильный адрес кнопки'):
        #      check.equal(element.get_attribute('href'), url_elements)