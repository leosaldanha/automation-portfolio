"""
tests/test_homepage.py contains all tests related to AutomationPractice's home page.

TestCase-001 - Click on Slider's next button
TestCase-002 - Switch to "Best Sellers" tab
TestCase-003 - Add product to cart and proceed to checkout
"""

# Lib
from selenium.webdriver.common.action_chains import ActionChains

# Modules
from pages.home_page import HomePage
from utils.constants import Constants


# TestCase-001 - Click on Slider's next button
def test_slider_interaction(browser):
    home_page = HomePage(browser)

    # GIVEN that I am at the Home Page
    home_page.load()
    assert home_page.title() == Constants.HOMEPAGE_TITLE

    # WHEN I click on Slider's next button
    slider_next_btn = home_page.get_slider_next_btn()
    slider_next_btn.click()

    # THEN it must display the next information
    slider_title = home_page.get_slider_title()
    slider_description = home_page.get_slider_description()

    assert slider_title == Constants.BANNER_INFO_LIST["title"]
    assert slider_description == Constants.BANNER_INFO_LIST["description"]


# TestCase-002 - Switch to "Best Sellers" tab
def test_best_sellers_tab(browser):
    home_page = HomePage(browser)

    # GIVEN that I am at the Home Page
    home_page.load()
    assert home_page.title() == Constants.HOMEPAGE_TITLE

    # WHEN I click the 'Best Sellers' tab
    home_page.scroll_down(540)
    best_sellers_tab = home_page.get_best_sellers_tab()
    best_sellers_tab.click()

    # THEN it must display the best seller products
    products_list = home_page.get_products_list()
    for i in products_list:
        assert i.get_attribute("title") in Constants.BEST_SELLER_TITLES_LIST


# TestCase-003 - Add product to cart and proceed to checkout
def test_add_to_cart_and_proceed_to_checkout(browser):
    PRODUCT_PRICE = "$16.51"
    home_page = HomePage(browser)

    # GIVEN I am at the Home Page
    home_page.load()
    assert home_page.title() == Constants.HOMEPAGE_TITLE

    # WHEN I add a product to my cart
    home_page.scroll_down(540)
    product_containers = home_page.get_product_containers()

    ActionChains(browser).move_to_element(product_containers[0]).perform()
    add_to_cart_btn = home_page.get_add_to_cart_btn(product_containers[0])
    add_to_cart_btn.click()

    # AND I proceed to checkout
    proceed_to_checkout_btn = home_page.get_proceed_to_checkout_btn()
    proceed_to_checkout_btn.click()

    # THEN the price of the product must be as expected
    unitary_price = home_page.get_product_unitary_price()

    assert PRODUCT_PRICE in unitary_price


