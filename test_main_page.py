from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_page()

@pytest.mark.parametrize('different_links', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])         
def test_add_to_basket(browser, different_links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{different_links}"
    page = MainPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_title()
    