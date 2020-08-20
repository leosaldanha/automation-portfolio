"""
tests/conftest.py contains fixtures and settings defined right before the tests are executed.
"""

import json
import pytest
import selenium.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def setup_chrome(type):
    options = selenium.webdriver.ChromeOptions()

    # common settings
    options.add_argument("--lang=pt-BR")

    if type == 'standard':
        options.add_argument("--start-maximized")
    elif type == 'headless':
        options.add_argument('headless')
    else:
        raise Exception()

    return options


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('setup.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome(options=setup_chrome('standard'))
    elif config['browser'] == 'Headless Chrome':
        b = selenium.webdriver.Chrome(options=setup_chrome('headless'))
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
