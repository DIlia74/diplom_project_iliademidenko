import allure
import pytest_check as check
from locators.locators_header import MainPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_auto_ru(web_browser):

    page = MainPage(web_browser)

    elements = [(page.btn_about,'О нас','https://www.kpc.by/about'),
                (page.btn_news,'Новости','https://www.kpc.by/news'),
                (page.btn_shopping,'Доставка и оплата','https://www.kpc.by/shipping'),
                (page.btn_contacts,'Контакты','https://www.kpc.by/contacts'),
                (page.btn_help,'Помощь','https://www.kpc.by/help'),
                (page.btn_catalog_produkcii,'КАТАЛОГ ПРОДУКЦИИ','https://www.kpc.by/catalog/'),
                (page.btn_servisiprodukcii,'СЕРВИС И УСЛУГИ','https://www.kpc.by/services'),
                (page.btn_pokopijnoeobsl,'ПОКОПИЙНОЕ ОБСЛУЖИВАНИЕ KYOCERA','https://www.kpc.by/pokopijnoe-obsluzhivanie')
                ]
    for element, text_element, url_elements in elements:

        with allure.step('Тест проверки правильного URL при переходе'):
            element.click()
            check.equal(page.get_current_url(), url_elements)

        with allure.step('Тест проверки отображения на экране'):
            check.is_true(element.is_visible())

        with allure.step('Тест проверки кликабельности'):
            check.is_true(element.is_clickable())

        with allure.step('Тест проверки на орфографию'):
            check.equal(element.get_text(), text_element)

        with allure.step('Тест проверки на правильный адрес кнопки'):
             check.equal(element.get_attribute('href'), url_elements)

