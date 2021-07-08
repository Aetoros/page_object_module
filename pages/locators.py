from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class BasketLocator():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button.btn")
    CHECK_TITLE = (By.CSS_SELECTOR, ".col-sm-6 h1")
    CHECK_TITLE_AFTER_ADDING = (By.CSS_SELECTOR,".alert:nth-child(1) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
     
 