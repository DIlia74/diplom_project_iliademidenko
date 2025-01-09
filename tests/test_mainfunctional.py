import allure
import pytest_check as check
from locators.locators_mainfunctional import MainPage
from conftest import web_browser
import time


def navigate_to_basket(page):
    page.btn_katalog_production.move_to()
    page.btn_printers.click()
    page.btn_in_basket.click()
    page.btn_basket.click()
    time.sleep(3)

def fill_basket_form(page):
    email = 'test@gmail.com'
    receiver = 'Test Тест'
    phone = '-0000000000000'
    more_info = 'TesttesttestTesttesttestTesttesttestTesttesttestTesttesttestTesttesttest'
    postindex = '0000000000000'
    region = 'test тест'
    city = 'тест test'
    street = 'Push-kina123'
    building = 'k0lotu$Hk1na'
    room = 'test'

    page.input_email.send_keys(email)
    page.input_receiver.send_keys(receiver)
    page.input_phone.send_keys(phone)
    page.input_moreinformation.send_keys(more_info)
    page.checkbox_dostavka.click()
    page.input_postindex.send_keys(postindex)
    page.input_region.send_keys(region)
    page.input_city.send_keys(city)
    page.input_street.send_keys(street)
    page.input_building.send_keys(building)
    page.input_room.send_keys(room)


@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест для проверки добавления товара и просмотра в корзине')
def test_kpc_mainfunctional_addproduct(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест проверка добавления товара в корзину'):
        page.btn_katalog_production.move_to()
        page.btn_printers.click()
        page.btn_in_basket.click()
        page.btn_basket.click()
        check.equal(page.get_current_url(),'https://www.kpc.by/cart')


@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест для проверки удаления товара и просмотра в корзине')
def test_kpc_mainfunctional_deleteproduct(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест проверка удаление товара из корзины'):
        page.btn_katalog_production.move_to()
        page.btn_printers.click()
        page.btn_in_basket.click()
        page.btn_basket.click()
        page.btn_clear_basket.click()


@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест для проверки написания текста в корзине')
def test_kpc_mainfunctional_sendkeys(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест на написание текста в корзине'):
        page.btn_katalog_production.move_to()
        page.btn_printers.click()
        page.btn_in_basket.click()
        page.btn_basket.click()
        page.count_tovar.send_keys('абв')
        check.is_true(page.count_tovar.is_visible())
        check.is_true(page.count_tovar.is_clickable())


@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест для проверки ввода разных цифр в поле корзины')
def test_kpc_mainfunctional_sendkeys1(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест на ввод цифр в поле корзины'):
        page.btn_katalog_production.move_to()
        page.btn_printers.click()
        page.btn_in_basket.click()
        page.btn_basket.click()
        page.count_tovar.send_keys('-9999')
        page.btn_plus.click()
        time.sleep(3)

@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест заполнение почты')
def test_kpc_mainfunctional_sendkeys2(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест заполнения почты'):
        page.btn_katalog_production.move_to()
        page.btn_printers.click()
        page.btn_in_basket.click()
        page.btn_basket.click()
        page.input_email.send_keys('test@gmail.com')
        check.is_true(page.input_email.is_valid_email('test@gmail.com'))
        page.btn_submit.click()

    with allure.step('Проверка на отображение'):
        check.is_true(page.input_email.is_visible())

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.input_email.is_clickable())

@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест заполнение данных получателя и номера телефона')
def test_kpc_mainfunctional_sendkeys3(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест заполнения инпута "Получатель"'):
        navigate_to_basket(page)
        page.input_receiver.send_keys('Test Тест')

    with allure.step('Тест заполнения инпута "Телефон"'):
        page.input_phone.send_keys('-0000000000000')
        page.btn_submit.click()


    with allure.step('Проверка на отображение'):
        check.is_true(page.input_email.is_visible())

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.input_email.is_clickable())

    with allure.step('Проверка на отображение'):
        check.is_true(page.input_phone.is_visible())

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.input_phone.is_clickable())


@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест заполнение данных для доставки')
def test_kpc_mainfunctional_sendkeys4(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест заполнения данных для доставки'):
        navigate_to_basket(page)
        page.checkbox_dostavka.click()
        page.input_postindex.send_keys('0000000000000')
        page.input_region.send_keys('test тест')
        page.input_city.send_keys('тест test')
        page.input_street.send_keys('Push-kina123')
        page.input_building.send_keys('k0lotu$Hk1na')
        page.input_room.send_keys('test')
        page.btn_submit.click()


@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест заполнение данных для доставки(в целом)')
def test_kpc_mainfunctional_common(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест заполнение общей формы для заказа'):
        navigate_to_basket(page)
        page.input_email.send_keys('test@gmail.com')
        page.input_receiver.send_keys('Test Тест')
        page.input_phone.send_keys('-0000000000000')
        page.input_moreinformation.send_keys('TesttesttestTesttesttestTesttesttestTesttesttestTesttesttestTesttesttest')
        page.checkbox_dostavka.click()
        page.input_postindex.send_keys('0000000000000')
        page.input_region.send_keys('test тест')
        page.input_city.send_keys('тест test')
        page.input_street.send_keys('Push-kina123')
        page.input_building.send_keys('k0lotu$Hk1na')
        page.input_room.send_keys('test')
        page.btn_submit.click()


@allure.story('Тест для проверки основного функционала')
@allure.feature('Тест заполнение данных для доставки(в целом) и нажатие кнопки очистить форму')
def test_kpc_mainfunctional_cleardata(web_browser):

    page = MainPage(web_browser)

    with allure.step('Тест проверки функционала кнопки "Очистить форму"'):
        navigate_to_basket(page)
        fill_basket_form(page)
        page.btn_clear_data.click()
        time.sleep(5)






