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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketTransition():
    TRANSITION_TO_BASKET = (By.CSS_SELECTOR, "span .btn")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#id_form-0-quantity")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p")

class RegistrationLocators():    
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn")
    ACCOUNT = (By.CSS_SELECTOR, ".nav > li:nth-child(1) a")