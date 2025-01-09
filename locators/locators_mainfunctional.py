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

    btn_katalog_production = WebElement(xpath='//nav//a[@href="catalog/"]') # Каталог продукции
    btn_printers = WebElement(xpath='//ul[@class]//li[@class="first"]//a[@href="catalog/printers/"]') # кнопка принтеры
    btn_in_basket = WebElement(xpath='(//*[@name="ms2_action"])[1]') # самый первый принтер в корзину
    btn_basket = WebElement(xpath='//div[@class="header-block-system-icons"]//a[@href="cart"]') # корзина
    btn_clear_basket = WebElement(xpath='''//*[contains(text(),'Очистить корзину')]''') # очистить корзину
    count_tovar = WebElement(xpath='//*[@name="count"]') # input товаров
    btn_plus = WebElement(xpath='(//*[@role="form"]//button)[2]') # плюс
    input_email = WebElement(xpath='//div[@class="col-12 col-md-6 pr-5"]//input[@name="email"]') # поле ввода почты
    input_receiver = WebElement(xpath='//div[@class="form-group input-parent required"]//input[@name="receiver"]') #получатель
    input_phone = WebElement(xpath='//div[@class="form-group input-parent"]//input[@name="phone"]') # телефон
    input_moreinformation = WebElement(xpath='//textarea[@name="comment"]') # доп информация
    checkbox_samovyvoz = WebElement(xpath='(//*[@id="deliveries"]//label)[1]') # чекбокс самовывоз
    checkbox_dostavka = WebElement(xpath='(//*[@id="deliveries"]//label)[2]') # чекбокс доставка
    input_postindex = WebElement(xpath='//div[@class="relative required"]//input[@placeholder="Почтовый индекс"]') # почтовый индекс
    input_region = WebElement(xpath='//input[@id="region"]') # область
    input_city = WebElement(xpath='//input[@name="city"]') # город
    input_street = WebElement(xpath='//input[@name="street"]') # улица
    input_building = WebElement(xpath='//input[@name="building"]') # дом
    input_room = WebElement(xpath='//input[@name="room"]') # комната
    btn_clear_data = WebElement(xpath='//div[@class="col-sm-4 mb-3 "]//button[@name="ms2_action"]') # кнопка очистить форму
    btn_submit = WebElement(xpath='//div[@class="pl-3 text-right mb-5"]//button[@value="order/submit"]') # кнопка подтверждения заказа


