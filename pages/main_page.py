from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import BasketLocator
from .login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def add_to_basket(self):
        add = self.browser.find_element(*BasketLocator.ADD_TO_BASKET)
        add.click() 


    def check_title(self):
        check = self.browser.find_element(*BasketLocator.CHECK_TITLE)
        check1 = check.text
        check_after = self.browser.find_element(*BasketLocator.CHECK_TITLE_AFTER_ADDING)
        check_after2 = check_after.text
        assert check1 == check_after2, "Wrong title"