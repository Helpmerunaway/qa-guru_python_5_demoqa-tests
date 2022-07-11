from selene import have
from selene.core.entity import Element
from typing import Optional
from selene.support.shared import browser


class TagsInput:

	def __init__(self, element):
		self.element: Element = element

	def add(self, from_: str, /, *, autocomplete: Optional[str] = None):
		self.element.type(from_)
		browser.all(
			'.subjects-auto-complete__option'
		).element_by(have.text(autocomplete or from_)).click()
		return self

	def autocomplete(self, from_: str):
		self.element().send_keys(from_)
		self.element.press_tab()