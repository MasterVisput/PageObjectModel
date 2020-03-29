from .base_page import BasePage
from selenium import webdriver
from .locators import ProductPageLocators
from selenium.webdriver import Remote as RemoteWebDriver

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def product_should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING)


    def product_name_should_be_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name in product_name_in_basket, 'Product name not in basket'


    def product_cost_should_be_in_basket(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_cost_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_cost in product_cost_in_basket, 'Price in basket wrong'







