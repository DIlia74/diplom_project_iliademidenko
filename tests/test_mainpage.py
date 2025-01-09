import time

import allure
import pytest_check as check
from selenium.webdriver.common.devtools.v85.dom import get_attributes

from locators.locators_mainpageetc import MainPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки лого')
def test_logo_kpc_by(web_browser):
    """Тест на наличие лого и его функционал"""

    page = MainPage(web_browser)

    with allure.step(f'Проверка "{page.kpclogo}" на отображение'):
        check.is_true(page.kpclogo.is_visible())
    with allure.step(f'Проверка "{page.kpclogo}" на функционал'):
        page.kpclogo.click()
        check.is_true(page.kpclogo.is_clickable())


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки <li>Каталог продукции</li>')
def test_li_catalog_kpc_by(web_browser):
    """Этот тест проверяет функционал кнопки "Каталог продукции" и его подразделов"""

    page = MainPage(web_browser)

    with allure.step(f'Проверка "{page.btn_katalog_production}" на отображение'):
        check.is_true(page.btn_katalog_produkcii.is_visible())

    elements = [(page.btn_printers,'Принтеры','https://www.kpc.by/catalog/printers/'),
                (page.btn_kopiryimfu,'Копиры и МФУ','https://www.kpc.by/catalog/copiers/'),
                (page.btn_optional_equipment,'Опциональное оснащение','https://www.kpc.by/catalog/options/'),
                (page.btn_consumables,'Расходные материалы','https://www.kpc.by/catalog/orm/'),
                (page.btn_spare_parts,'Запчасти','https://www.kpc.by/catalog/spare-parts/'),
                (page.btn_related_products,'Сопутствующие товары','https://www.kpc.by/catalog/other/'),
                (page.btn_archive_of_devices,'Архив аппаратов','https://www.kpc.by/catalog/arhiv/')
                ]
    for element, text_element, url_elements in elements:
        page.btn_katalog_production.move_to()

        with allure.step('Тест проверки правильного URL при переходе'):
            element.click()
            check.equal(page.get_current_url(), url_elements)

        with allure.step('Тест проверки на правильный адрес кнопки'):
             check.equal(element.get_attribute('href'), url_elements)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки оставшихся кнопок бади')
def test_body_kpc_by(web_browser):
    """Тест на проверку кнопок в боди"""

    page = MainPage(web_browser)

    elements = [(page.btn_service_and_uslugi,'СЕРВИС И УСЛУГИ','https://www.kpc.by/services'),
                (page.btn_diagnostic_oborudovania,'Диагностика оборудования','https://www.kpc.by/services'),
                (page.btn_repair_and_obsl,'Ремонт и регламентное обслуживание','https://www.kpc.by/services'),
                (page.btn_obsl_korpor_clients,'Комплексное обслуживание корпоративных клиентов','https://www.kpc.by/services'),
                (page.btn_guarantee_repair_oborud,'Гарантийный ремонт оборудования','https://www.kpc.by/services'),
                (page.btn_fillup_cartridges_chg_rashod,'Заправка картриджей. Замена расходников','https://www.kpc.by/services'),
                (page.btn_katalog_produkcii,'КАТАЛОГ ПРОДУКЦИИ','https://www.kpc.by/catalog/'),
                (page.btn_archive_apparatov,' Архив аппаратов','https://www.kpc.by/catalog/'),
                (page.btn_pokopijnoe_obsl,'ПОКОПИЙНОЕ ОБСЛУЖИВАНИЕ','https://www.kpc.by/pokopijnoe-obsluzhivanie')
                ]
    for element, text_element, url_elements in elements:

        with allure.step('Тест проверки правильного URL при переходе'):
            element.click()
            check.equal(page.get_current_url(), url_elements)
            page.go_back()


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки карусели')
def test_carousel_kpc_by(web_browser):
    """Тесты на проверку карусели"""

    page = MainPage(web_browser)

    with allure.step('Тест проверки на кликабельность'):
        for i in range(5):
            page.right_btn.click()
        check.is_true(page.right_btn.is_clickable())
        check.is_true(page.right_btn.is_visible())
        check.equal(page.firstph.get_attribute('href'),'https://www.kpc.by/catalog/copiers/bw-mfp-a4/ma4500x')

    with allure.step('Тест проверка остановки авторотации при наведении курсора'):
        page.firstph.move_to()
        time.sleep(7)
        check.is_true(page.firstph.is_visible(),'При наведении курсора авторотация не просиходит')


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки перехода по фото')
def test_carousel_kpc_by1(web_browser):
    """Негативный тест карусели на переход по картинке"""

    page = MainPage(web_browser)

    firstph = page.firstph # перменная с локатором первой картинки
    thirdph = page.thirdph # перменная с локатором 3 картинки

    with allure.step('Тест перехода в раздел по картинке и правильного адреса'):
        for i in range(3):
            page.left_btn.click()
        page.thirdph.click()
        time.sleep(3)

    with allure.step('Проверка первая картинка не равна третьей'):
        check.not_equal(firstph, thirdph)

    with allure.step('Проверка: третья картинка равна третьей картинке'):
        check.equal(firstph, thirdph) # две проверки первая перменная не равно третей переменной и вторая проаерка: что третья картинка равно третей картинки
        # check.equal(page.get_current_url(),'https://www.kpc.by/catalog/copiers/%D1%86%D0%B2%D0%B5%D1%82%D0%BD%D1%8B%D0%B5-%D0%BC%D1%84%D1%83-a4/ma3500cix')


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки перехода по фото')
def test_carousel_kpc_by2(web_browser):
    """Позитивный тест карусели на переход по картинке"""

    page = MainPage(web_browser)

    with allure.step('Тест перехода в раздел по картинке и правильного адреса'):
        page.firstph.click()
        time.sleep(3)
        check.equal(page.get_current_url(),'https://www.kpc.by/')   # возвращает на дефолт страницу, стр принтера откр-ся

    with allure.step(f'Проверка "{page.firstph}" на отображение'):
        check.is_true(page.firstph.is_visible())

    with allure.step(f'Проверка "{page.firstph}" на кликабельность'):
        check.is_true(page.firstph.is_clickable())








