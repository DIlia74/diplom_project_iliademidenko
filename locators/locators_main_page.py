import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.kpc.by/'

        super().__init__(web_driver, url)

    # btn_headers_domain = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Домены")]')