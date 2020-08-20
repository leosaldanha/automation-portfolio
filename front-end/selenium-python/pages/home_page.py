"""
pages/home_page.py contains a class that define methods and variables to encapsulate the element gathering process.
"""

# Libs
from selenium.webdriver.common.by import By

# Modules
from utils.constants import Constants


class HomePage:

    # Locators
    HOME_PAGE_TABS = (By.ID, Constants.HOME_PAGE_TABS)
    BEST_SELLERS_TAB = (By.CLASS_NAME, Constants.BEST_SELLERS_BLOCK)
    PRODUCTS_BLOCK = (By.ID, Constants.BEST_SELLERS_TAB)
    PRODUCT_CONTAINER = (By.CLASS_NAME, Constants.PRODUCT_CONTAINER)
    PRODUCTS_NAMES = (By.CLASS_NAME, Constants.BEST_SELLER_PRODUCT_NAME)

    SLIDER = (By.ID, Constants.SLIDER)
    SLIDER_NEXT_BTN = (By.CLASS_NAME, Constants.SLIDER_NEXT_BTN)
    SLIDER_TEXT = (By.CLASS_NAME, Constants.SLIDER_TEXT)
    SLIDER_TITLE = (By.TAG_NAME, "h2")
    SLIDER_DESC = (By.TAG_NAME, "p")

    CART_CONFIRMATION_MODAL = (By.ID, Constants.CART_CONFIRMATION_MODAL)
    PROCEED_TO_CHECKOUT_BTN = (By.CLASS_NAME, Constants.PROCEED_TO_CHECKOUT_BTN)
    CART_SUMMARY = (By.ID, Constants.CART_SUMMARY)
    PRODUCT_UNITARY_PRICE = (By.CLASS_NAME, Constants.PRODUCT_UNITARY_PRICE)

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Load website
    def load(self):
        self.browser.get(Constants.BASE_URL + "/")

    def scroll_down(self, pixels):
        self.browser.execute_script("window.scrollTo(0, %s)" % (str(pixels))) 

    def get_best_sellers_tab(self):
        home_page_tabs = self.browser.find_element(*self.HOME_PAGE_TABS)
        return home_page_tabs.find_element(*self.BEST_SELLERS_TAB)

    def get_products_list(self):
        products_block = self.browser.find_element(*self.PRODUCTS_BLOCK)
        return products_block.find_elements(*self.PRODUCTS_NAMES)

    def get_slider_next_btn(self):
        slider = self.browser.find_element(*self.SLIDER)
        return slider.find_element(*self.SLIDER_NEXT_BTN)

    def get_slider_title(self):
        slider = self.browser.find_element(*self.SLIDER)
        return slider.find_element(*self.SLIDER_TEXT).find_element(*self.SLIDER_TITLE).get_attribute("innerHTML")

    def get_slider_description(self):
        slider = self.browser.find_element(*self.SLIDER)
        return slider.find_element(*self.SLIDER_TEXT).find_element(*self.SLIDER_DESC).get_attribute("innerHTML")

    def get_product_containers(self):
        return self.browser.find_elements(*self.PRODUCT_CONTAINER)

    def get_add_to_cart_btn(self, container):
        return container.find_element(By.CLASS_NAME, Constants.ADD_TO_CART_BTN)

    def get_proceed_to_checkout_btn(self):
        modal = self.browser.find_element(*self.CART_CONFIRMATION_MODAL)
        return modal.find_element(*self.PROCEED_TO_CHECKOUT_BTN)

    def get_product_unitary_price(self):
        cart_summary = self.browser.find_element(*self.CART_SUMMARY)
        return cart_summary.find_element(*self.PRODUCT_UNITARY_PRICE).get_attribute("innerHTML")

    def title(self):
        return self.browser.title
