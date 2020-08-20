"""
utils/constants.py contains all the constants that are used on the project.
"""


class Constants:
    # URLs
    BASE_URL = 'http://automationpractice.com'

    # Page titles
    HOMEPAGE_TITLE = "My Store"

    # Messages
    CONFIRMATION_MESSAGE = "Product successfully added to your shopping cart"

    # To be used by locators
    # ID
    HOME_PAGE_TABS = "home-page-tabs"
    BEST_SELLERS_BLOCK = "blockbestsellers"
    SLIDER = "homepage-slider"
    CART_CONFIRMATION_MODAL = "layer_cart"
    CART_SUMMARY = "cart_summary"

    # Class
    BEST_SELLERS_TAB = "blockbestsellers"
    BEST_SELLER_PRODUCT_NAME = "product-name"
    SLIDER_NEXT_BTN = "bx-next"
    SLIDER_TEXT = "homeslider-description"
    ADD_TO_CART_BTN = "ajax_add_to_cart_button"
    PRODUCT_CONTAINER = "product-container"
    PROCEED_TO_CHECKOUT_BTN = "button-medium"
    PRODUCT_UNITARY_PRICE = "price"

    BEST_SELLER_TITLES_LIST = [
        "Printed Chiffon Dress",
        "Faded Short Sleeve T-shirts",
        "Blouse",
        "Printed Summer Dress",
        "Printed Dress"
    ]

    BANNER_INFO_LIST = {
        "title": "EXCEPTEUR<br>OCCAECAT",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin tristique in tortor et" +
                       " dignissim. Quisque non tempor leo. Maecenas egestas sem elit"
    }
