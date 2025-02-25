from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def product_should_be_not_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'Product in basket, but should be not'

    def guest_should_see_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY), 'Basket is not empty, but should be'
