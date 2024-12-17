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

    # btn_headers_domain = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Домены")]')
    btn_about = WebElement(xpath='//div[@class="header-block"]//a[@href="about"]')          # О нас
    btn_news = WebElement(xpath='//div[@class="header-block"]//a[@href="news"]')            # Новости
    btn_shopping = WebElement(xpath='//div[@class="header-block"]//a[@href="shipping"]')    # Доставка и оплата
    btn_contacts = WebElement(xpath='//div[@class="header-block"]//a[@href="contacts"]')    # Контакты
    btn_help = WebElement(xpath='//div[@class="header-block"]//a[@href="help"]')            # Помощь
    btn_catalog_produkcii = WebElement(xpath='//nav//a[@href="catalog/"]')                  # Каталог продукции
    btn_servisiprodukcii = WebElement(xpath='//nav//a[@href="services"]')                   # Сервис и услуги
    btn_pokopijnoeobsl = WebElement(xpath='//nav//a[@href="pokopijnoe-obsluzhivanie"]')     # Покопийное обсл-ие Kyocera