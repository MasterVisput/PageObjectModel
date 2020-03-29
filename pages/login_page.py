from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_field = self.browser.find_element_by_css_selector('[name="registration-email"]')
        password_field_1 = self.browser.find_element_by_css_selector('[name="registration-password1"]')
        password_field_2 = self.browser.find_element_by_css_selector('[name="registration-password2"]')
        email_field.send_keys(email)
        password_field_1.send_keys(password)
        password_field_2.send_keys(password)
        button_reg = self.browser.find_element_by_css_selector('[name="registration_submit"]')
        button_reg.click()
        self.browser.implicitly_wait(5)

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'This page not is login form'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'