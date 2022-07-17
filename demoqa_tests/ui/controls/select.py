from selene import command, have
from selene.core.entity import Element
from selene.support.shared import browser


def select(element: Element, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


def by_choose(element: Element, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


def by_autocomplete(element: Element, /, *, option: str):
    element.type(option).press_enter()
