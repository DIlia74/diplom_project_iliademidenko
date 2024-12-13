import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://auto.ru/'

        super().__init__(web_driver, url)

    btn_hamburger = WebElement(xpath='//div[@class="Dropdown__switcher HeaderBurger__switcher"]')
    btn_obl = ManyWebElements(xpath='//a[@class="HeaderSitemap__itemLink HeaderSitemap__itemLink_new"]')
    btn_for_all_things = ManyWebElements(xpath='//a[@class="HeaderSitemap__itemLink"]')