from selene import have, be
from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_managemento():
	print('Starting browser')
	browser.config.wait_for_no_overlap_found_by_js = True

	browser.config.browser_name = 'chrome'
	browser.config.hold_browser_open = False
	browser.config.timeout = 3
	browser.config.window_width = 1700
	browser.config.window_height = 1200


@pytest.fixture()
def open_auto_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    browser.element('[class="main-header"]').should(have.text('Practice Form'))


@pytest.fixture()
def open_webtables_page():
	browser.open('https://demoqa.com/webtables')
	browser.should(have.title('ToolsQA'))
	browser.element('[class="main-header"]').should(have.text('Web Tables'))
