from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketLocator


class ProductPage(BasePage):
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        add = self.browser.find_element(*BasketLocator.ADD_TO_BASKET)
        add.click()
        assert self.is_not_element_present(*BasketLocator.CHECK_TITLE_AFTER_ADDING), "Success message is presented"
   
    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*BasketLocator.CHECK_TITLE_AFTER_ADDING), "Success message is presented"

    def test_message_disappeared_after_adding_product_to_basket(self):
        add = self.browser.find_element(*BasketLocator.ADD_TO_BASKET)
        add.click()
        assert self.is_disappeared(*BasketLocator.CHECK_TITLE_AFTER_ADDING), "Success message is presented"
