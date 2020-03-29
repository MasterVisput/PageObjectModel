from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_url()


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_see_to_login_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_form()

def test_guest_see_to_register_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_register_form()

def test_guest_can_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.product_should_be_not_in_basket()





