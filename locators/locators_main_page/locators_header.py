import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://auto.ru/'

        super().__init__(web_driver, url)

    # btn_headers_domain = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Домены")]')
    btn_cars = WebElement(xpath = '//li[@data-id="cars"]')
    btn_commercial = WebElement(xpath = '//li[@data-id="trucks"]')
    btn_electro = WebElement(xpath = '//li[@data-id="electro"]')
    btn_chinese = WebElement(xpath = '//li[@data-id="chinese"]')
    btn_moto = WebElement(xpath = '//li[@data-id="moto"]')
    btn_history = WebElement(xpath = '//li[@data-id="history"]')
    btn_cars_otchet = WebElement(xpath = '//li[@data-id="c2b-promo"]')
    btn_insurance = WebElement(xpath = '//li[@data-id="credits"]')
    btn_ocenka_auto = WebElement(xpath = '//li[@data-id="cars-evaluation"]')
    btn_strahovka = WebElement(xpath = '//li[@data-id="insurance"]')
    btn_dealers = WebElement(xpath = '//li[@data-id="garage-new"]')
    btn_journals = WebElement(xpath = '//li[@data-id="mag"]')
    btn_for_biznes = WebElement(xpath = '//li[@data-id="dealers"]')