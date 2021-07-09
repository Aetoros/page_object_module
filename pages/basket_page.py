from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketLocator
from .locators import BasketTransition

class BasketPage(BasePage):
    def add_to_basket(self):
        add = self.browser.find_element(*BasketLocator.ADD_TO_BASKET)
        add.click() 


    def check_title(self):
        check = self.browser.find_element(*BasketLocator.CHECK_TITLE)
        check1 = check.text
        check_after = self.browser.find_element(*BasketLocator.CHECK_TITLE_AFTER_ADDING)
        check_after2 = check_after.text
        assert check1 == check_after2, "Wrong title"

    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        find_basket = self.browser.find_element(*BasketTransition.TRANSITION_TO_BASKET)
        find_basket.click()
        assert self.is_not_element_present(*BasketTransition.BASKET_EMPTY), "Basket is empty"
        assert self.is_element_present(*BasketTransition.BASKET_EMPTY_TEXT), "Empty basket text present"

    def guest_cant_see_product_in_basket_opened_from_product_page(self):
        find_basket = self.browser.find_element(*BasketTransition.TRANSITION_TO_BASKET)
        find_basket.click()
        assert self.is_not_element_present(*BasketTransition.BASKET_EMPTY), "Basket is empty"
        assert self.is_element_present(*BasketTransition.BASKET_EMPTY_TEXT), "Empty basket text present"