import os
from xml.etree.ElementPath import xpath_tokenizer

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.kpc.by/'

        super().__init__(web_driver, url)

    btn_katalog_production = WebElement(xpath='//nav//a[@href="catalog/"]') # Кнопка каталог продукции и её подразделы
    btn_printers = WebElement(xpath='//nav//div[@class="wrap"]//ul[@class]//a[@href="catalog/printers/"]') # Принтеры
    btn_kopiryimfu = WebElement(xpath='//nav//div[@class="wrap"]//ul[@class]//a[@href="catalog/copiers/"]') # Копиры и МФУ
    btn_optional_equipment = WebElement(xpath='//nav//div[@class="wrap"]//ul[@class]//a[@href="catalog/options/"]') # Опциональное оснащение
    btn_consumables = WebElement(xpath='//nav//div[@class="wrap"]//ul[@class]//a[@href="catalog/orm/"]') # Расходные материалы
    btn_spare_parts = WebElement(xpath='//nav//div[@class="wrap"]//ul[@class]//a[@href="catalog/spare-parts/"]') # Запчасти
    btn_related_products = WebElement(xpath='//nav//div[@class="wrap"]//ul[@class]//a[@href="catalog/other/"]') # Сопутствующие товары
    btn_archive_of_devices = WebElement(xpath='//nav//div[@class="wrap"]//ul[@class]//a[@href="catalog/arhiv/"]') # Архив аппаратов
    kpclogo = WebElement(xpath='//div[@class="logo"]')          # Логотип слевовверху

    btn_katalog_produkcii = WebElement(xpath="//*[contains(text(),'КАТАЛОГ ПРОДУКЦИИ')]")           # кнопка каталог продукции на главной стр
    btn_archive_apparatov = WebElement(xpath='//a[@title="Каталог продукции"]')             # кнопка архив аппаратов на гл стр
    btn_pokopijnoe_obsl = WebElement(xpath="//*[contains(text(),'ПОКОПИЙНОЕ ОБСЛУЖИВАНИЕ')]")           # кнопка покопийного обслуживания на главной стра

    ### class="home-services"
    btn_service_and_uslugi = WebElement(xpath='//div[@class="home-title title-services"]//div[@class="title h2"]')  # Кнопка сервис и услуги на главной стр
    btn_diagnostic_oborudovania = WebElement(xpath='''//div[@class="home-services"]//*[contains(text(),'Диагностика оборудования')]''') #Кнопка диагностика оборудования
    btn_repair_and_obsl = WebElement(xpath='''//div[@class="home-services"]//*[contains(text(),'Ремонт и регламентное обслуживание')]''') #Кнопка Ремонт и регламентное обслуживание
    btn_obsl_korpor_clients = WebElement(xpath='''//div[@class="home-services"]//*[contains(text(),'Комплексное обслуживание корпоративных клиентов')]''') #Кнопка Комплексное обслуживание корпоративных клиентов
    btn_guarantee_repair_oborud = WebElement(xpath='''//div[@class="home-services"]//*[contains(text(),'Гарантийный ремонт оборудования')]''') #Кнопка Гарантийный ремонт оборудования
    btn_fillup_cartridges_chg_rashod = WebElement(xpath='''//div[@class="home-services"]//*[contains(text(),'Заправка картриджей. Замена расходников')]''') #КнопкаЗаправка картриджей. Замена расходников

    ########## Карусель ###########

    left_btn = WebElement(xpath='//button[@aria-label="Previous"]') # левая кнопка
    right_btn = WebElement(xpath='//button[@aria-label="Next"]') # правая кнопка
    firstph = WebElement(xpath='//a[@href="catalog/copiers/bw-mfp-a4/ma4500x"]') # первое фото
    secondph = WebElement(xpath='//a[@href="catalog/printers/монохромные-принтеры-a4/pa5500x"]') # второе фото
    thirdph = WebElement(xpath='//img[@src="res/img/print_3.jpg"]') # третье фото
    fourthph = WebElement(xpath='//img[@src="res/img/print_4.jpg"]') # четвертое фото
    fifthph = WebElement(xpath='//img[@src="res/img/print_5.jpg"]') # пятое фото






