from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .locators import RegistrationLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        x = self.browser.current_url
        assert "login" in x, "no login in url"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        self.browser.find_element(*RegistrationLocators.EMAIL).send_keys(email)
        self.browser.find_element(*RegistrationLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*RegistrationLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()
        assert self.is_element_present(*RegistrationLocators.ACCOUNT), "User is not logged in"