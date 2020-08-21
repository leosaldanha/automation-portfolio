"""
tests/test_homepage.py contains all tests related to AutomationPractice's home page.

TestCase-001 - Click on Slider's next button
TestCase-002 - Switch to "Best Sellers" tab
TestCase-003 - Add product to cart and proceed to checkout
"""

# Lib
# Timers were added on the code only to make it easier for whoever is watching the code execution
import time

# Modules
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from utils.constants import Constants

# TestCase-001 - Create Account
def test_account_creation(browser):
    home_page = HomePage(browser)
    auth_page = AuthPage(browser)

    home_page.load()
    assert home_page.get_browser_title() == Constants.HOMEPAGE_TITLE

    sign_in_btn = home_page.get_sign_in_btn()
    sign_in_btn.click()

    auth_page.fill_email_to_create_acc(Constants.ACC_EMAIL)

    create_acc_btn = auth_page.get_create_acc_btn()
    create_acc_btn.click()

    auth_page.fill_personal_information_form(Constants.USER_PERSONAL_INFO)

    time.sleep(5)




# TestCase-004 - Add to cart and proceed to checkout
def test_add_to_cart_and_proceed_to_checkout(browser):
    PRODUCT_PRICE = "$16.51"

    home_page = HomePage(browser)

    # GIVEN I am at the Home Page
    home_page.load()
    assert home_page.get_browser_title() == Constants.HOMEPAGE_TITLE

    # WHEN I add a product to my cart
    home_page.scroll_down(540)

    add_to_cart_btn = home_page.get_add_to_cart_btn()
    add_to_cart_btn.click()

    # AND I proceed to checkout
    proceed_to_checkout_btn = home_page.get_proceed_to_checkout_btn()
    proceed_to_checkout_btn.click()

    # THEN the price of the product must be as expected
    unitary_price = home_page.get_product_unitary_price()

    time.sleep(2)

    assert PRODUCT_PRICE in unitary_price


