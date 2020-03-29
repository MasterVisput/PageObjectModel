from .pages.product_page import ProductPage
from time import sleep
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    #page.solve_quiz_and_get_code()
    page.product_should_be_add_to_basket()

@pytest.mark.skip
@pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6,
                                 pytest.param(7, marks=pytest.mark.xfail),
                                 8, 9])
def test_guest_can_see_product_name_in_basket_with_ficha(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_should_be_in_basket()

def test_guest_can_see_product_name_in_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    #page.solve_quiz_and_get_code()
    page.product_name_should_be_in_basket()


def test_guest_can_see_cost_product_in_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    #page.solve_quiz_and_get_code()
    page.product_cost_should_be_in_basket()


def test_guest_can_see_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    #page.solve_quiz_and_get_code()
    page.should_be_not_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    #page.solve_quiz_and_get_code()
    page.should_be_not_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    #page.solve_quiz_and_get_code()
    page.should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_form()

def test_guest_can_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.product_should_be_not_in_basket()