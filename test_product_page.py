from .pages.product_page import ProductPage
from time import sleep
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_should_be_add_to_basket()

#@pytest.mark.skip
@pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6,
                                 pytest.param(7, marks=pytest.mark.xfail),
                                 8, 9])
def test_guest_can_see_product_name_in_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_should_be_in_basket()


def test_guest_can_see_cost_product_in_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_cost_should_be_in_basket()