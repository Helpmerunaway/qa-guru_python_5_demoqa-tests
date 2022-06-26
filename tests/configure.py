from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
	browser.config.base_url = 'https://demoqa.com'
	browser.config.browser_name = 'chrome'
	browser.config.hold_browser_open = True
	browser.config.timeout = 3
	browser.config.window_width = 1920
	browser.config.window_height = 1080