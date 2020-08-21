# Libs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Modules
from utils.constants import Constants


class AuthPage:

    # Locators
    CREATE_ACC_EMAIL_INPUT = (By.CSS_SELECTOR, Constants.CREATE_ACC_EMAIL_INPUT)
    CREATE_ACC_BTN = (By.CSS_SELECTOR, Constants.CREATE_ACC_BTN)

    TITLE_RADIO_BTN = (By.CSS_SELECTOR, Constants.TITLE_RADIO_BTN)
    PERSONAL_FIRST_NAME = (By.CSS_SELECTOR, Constants.PERSONAL_FIRST_NAME)
    PERSONAL_LAST_NAME = (By.CSS_SELECTOR, Constants.PERSONAL_LAST_NAME)
    PERSONAL_PASSWORD = (By.CSS_SELECTOR, Constants.PERSONAL_PASSWORD)
    PERSONAL_BIRTH_DAY = (By.CSS_SELECTOR, Constants.PERSONAL_BIRTH_DAY)
    PERSONAL_BIRTH_MONTH = (By.CSS_SELECTOR, Constants.PERSONAL_BIRTH_MONTH)
    PERSONAL_BIRTH_YEAR = (By.CSS_SELECTOR, Constants.PERSONAL_BIRTH_YEAR)

    ADDRESS_FIRST_NAME = (By.CSS_SELECTOR, Constants.ADDRESS_FIRST_NAME)
    ADDRESS_LAST_NAME = (By.CSS_SELECTOR, Constants.ADDRESS_LAST_NAME)
    ADDRESS_COMPANY = (By.CSS_SELECTOR, Constants.ADDRESS_COMPANY)
    ADDRESS_LINE = (By.CSS_SELECTOR, Constants.ADDRESS_LINE)
    ADDRESS_CITY = (By.CSS_SELECTOR, Constants.ADDRESS_CITY)
    ADDRESS_STATE = (By.CSS_SELECTOR, Constants.ADDRESS_STATE)
    ADDRESS_ZIPCODE = (By.CSS_SELECTOR, Constants.ADDRESS_ZIPCODE)
    ADDRESS_COUNTRY = (By.CSS_SELECTOR, Constants.ADDRESS_COUNTRY)
    ADDRESS_MOBILE_PHONE = (By.CSS_SELECTOR, Constants.ADDRESS_MOBILE_PHONE)
    ADDRESS_ALIAS = (By.CSS_SELECTOR, Constants.ADDRESS_ALIAS)

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Common functions
    def load(self):
        self.browser.get(Constants.BASE_URL + "/index.php?controller=authentication&back=my-account")

    def get_browser_title(self):
        return self.browser.title

    def fill_email_to_create_acc(self, email):
        self.browser.find_element(*self.CREATE_ACC_EMAIL_INPUT).send_keys(email)

    def get_create_acc_btn(self):
        return self.browser.find_element(*self.CREATE_ACC_BTN)

    def fill_personal_information_form(self, personal_info_dict):
        self.browser.find_element(*self.TITLE_RADIO_BTN).click()
        self.browser.find_element(*self.PERSONAL_FIRST_NAME).send_keys(personal_info_dict["first_name"])
        self.browser.find_element(*self.PERSONAL_LAST_NAME).send_keys(personal_info_dict["last_name"])
        self.browser.find_element(*self.PERSONAL_PASSWORD).send_keys(personal_info_dict["password"])
        self.browser.find_element(*self.PERSONAL_BIRTH_DAY).click()
        self.browser.find_element(*self.PERSONAL_BIRTH_MONTH).click()
        self.browser.find_element(*self.PERSONAL_BIRTH_YEAR).click()
