import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.kpc.by/'

        super().__init__(web_driver, url)

    btn_footer_about = WebElement(xpath='//div[@class="f-col-3 menu"]//a[@href="about"]')           # О нас футер
    btn_footer_news = WebElement(xpath='//div[@class="f-col-3 menu"]//a[@href="news"]')             # Новости
    btn_footer_shopping = WebElement(xpath='//div[@class="f-col-3 menu"]//a[@href="shipping"]')     # Доставка и оплата
    btn_footer_contacts = WebElement(xpath='//div[@class="f-col-3 menu"]//a[@href="contacts"]')     # Контакты
    btn_footer_help = WebElement(xpath='//div[@class="f-col-3 menu"]//a[@href="help"]')             # Помощь
    btn_catalog_produkcii = WebElement(xpath='//div[@class="f-col-2 menu"]//a[@href="catalog/"]')   # Каталог продукции
    btn_services = WebElement(xpath='//div[@class="f-col-2 menu"]//a[@href="services"]')            # Сервис и услуги
    btn_maintenance = WebElement(xpath='//div[@class="f-col-2 menu"]//a[@href="pokopijnoe-obsluzhivanie"]')     # Покопийное обслуживание
