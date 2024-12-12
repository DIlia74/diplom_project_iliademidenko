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
    btn_moscow = WebElement(xpath='//a[@href="https://auto.ru/moskva/"]')
    btn_saint_petersburg = WebElement(xpath='//a[@href="https://auto.ru/sankt-peterburg/"]')
    btn_vladimir = WebElement(xpath='//a[@href="https://auto.ru/vladimir/"]')
    btn_volgograd = WebElement(xpath='//a[@href="https://auto.ru/volgograd/"]')
    btn_voronezh = WebElement(xpath='//a[@href="https://auto.ru/voronezh/"]')
    btn_ekaterinburg = WebElement(xpath='//a[@href="https://auto.ru/ekaterinburg/"]')
