"""
utils/constants.py contains all the constants that are used on the project.
"""


class Constants:
    BASE_URL = 'http://automationpractice.com'

    # Page titles
    HOMEPAGE_TITLE = "My Store"

    # Home page locators
    # ID
    HOME_PAGE_TABS = "home-page-tabs"
    CART_CONFIRMATION_MODAL = "layer_cart"
    CART_SUMMARY = "cart_summary"

    # Class
    ADD_TO_CART_BTN = "ajax_add_to_cart_button"
    PRODUCT_CONTAINER = "product-container"
    PROCEED_TO_CHECKOUT_BTN = "button-medium"
    PRODUCT_UNITARY_PRICE = "price"

    # CSS Selectors
    SIGN_IN_BTN = "a.login"

    # Login page locators
    # CSS Selectors
    CREATE_ACC_EMAIL_INPUT = "input[name='email_create']"
    CREATE_ACC_BTN = "button#SubmitCreate"

    # User credentials
    ACC_EMAIL = "testaccount1@provider.com"
    ACC_PASSWORD = "123456"

    # Account creation forms
    TITLE_RADIO_BTN = "label[for='id_gender1']"
    PERSONAL_FIRST_NAME = "input[name='customer_firstname']"
    PERSONAL_LAST_NAME = "input[name='customer_lastname']"
    PERSONAL_PASSWORD = "input#passwd"
    PERSONAL_BIRTH_DAY = "select#days > option[value='4']"
    PERSONAL_BIRTH_MONTH = "select#months > option[value='5']"
    PERSONAL_BIRTH_YEAR = "select#years > option[value='1900']"

    ADDRESS_FIRST_NAME = "input#firstname"
    ADDRESS_LAST_NAME = "input#lastname"
    ADDRESS_COMPANY = "input#company"
    ADDRESS_LINE = "input#address1"
    ADDRESS_CITY = "input#city"
    ADDRESS_STATE = "select#id_state > option[value='16']"
    ADDRESS_ZIPCODE = "input#postcode"
    ADDRESS_COUNTRY = "select[name='id_country'] > option[value='21']"
    ADDRESS_MOBILE_PHONE = "input#phone_mobile"
    ADDRESS_ALIAS = "input#alias"



    USER_PERSONAL_INFO = {
        "first_name": "Luke",
        "last_name": "Skywalker",
        "password": "maytheforcebewithyou"
    }

    USER_ADDRESS = {
        "first_name": "Luke",
        "last_name": "Skywalker",
        "company": "JEDI Inc.",
        "address": "R-16, Arkanis sector, Outer Rim Territories",
        "city": "Tatooine (planet)",
        "state": 1,
        "zip_code": "11111",
        "country": 21,
        "phone": "+11 11 11111 1111",
        "assignment": "Mommy"
    }