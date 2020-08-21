"""
pages/home_page.py contains a class that define methods and variables to encapsulate the element gathering process.
"""

# Libs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Modules
from utils.constants import Constants


class HomePage:

    # Locators
    HOME_PAGE_TABS = (By.ID, Constants.HOME_PAGE_TABS)

    SIGN_IN_BTN = (By.CSS_SELECTOR, Constants.SIGN_IN_BTN)

    PRODUCT_CONTAINER = (By.CLASS_NAME, Constants.PRODUCT_CONTAINER)

    CART_CONFIRMATION_MODAL = (By.ID, Constants.CART_CONFIRMATION_MODAL)
    PROCEED_TO_CHECKOUT_BTN = (By.CLASS_NAME, Constants.PROCEED_TO_CHECKOUT_BTN)
    CART_SUMMARY = (By.ID, Constants.CART_SUMMARY)
    PRODUCT_UNITARY_PRICE = (By.CLASS_NAME, Constants.PRODUCT_UNITARY_PRICE)

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Common functions
    def load(self):
        self.browser.get(Constants.BASE_URL + "/")

    def scroll_down(self, pixels):
        self.browser.execute_script("window.scrollTo(0, %s)" % (str(pixels)))

    def get_browser_title(self):
        return self.browser.title

    # Element locator functions

    def get_sign_in_btn(self):
        return self.browser.find_element(*self.SIGN_IN_BTN)

    def get_add_to_cart_btn(self):
        containers = self.browser.find_elements(*self.PRODUCT_CONTAINER)
        ActionChains(self.browser).move_to_element(containers[0]).perform()
        return containers[0].find_element(By.CLASS_NAME, Constants.ADD_TO_CART_BTN)

    def get_proceed_to_checkout_btn(self):
        modal = self.browser.find_element(*self.CART_CONFIRMATION_MODAL)
        return modal.find_element(*self.PROCEED_TO_CHECKOUT_BTN)

    def get_product_unitary_price(self):
        cart_summary = self.browser.find_element(*self.CART_SUMMARY)
        return cart_summary.find_element(*self.PRODUCT_UNITARY_PRICE).get_attribute("innerHTML")
