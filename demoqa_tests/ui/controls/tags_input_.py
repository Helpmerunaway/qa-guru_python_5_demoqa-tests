from selene import have
from selene.core.entity import Element
from typing import Optional
from selene.support.shared import browser


class TagsInput:

	def __init__(self, element: Element):
		self.element = element

	@staticmethod
	def by_name(value):
		return TagsInput(browser.element(
			f"#{value},[name={value}],[name*={value},[id*={value}],.{value},[testID={value}"
		))

	# функция возврата элемента обернутая в проперти для удобства использования
	# @property
	# def element(self):
	# 	return browser.element(self.selector)

	# ассерт метод пишется в случае необходимости
	def should_have_texts(self, *values):
		self.element.should(have.text(''.join(values)))

	def add(self, from_: str, /, *, autocomplete: Optional[str] = None):
		self.element.type(from_)
		browser.all(
			'.subjects-auto-complete__option'
		).element_by(have.text(autocomplete or from_)).click()
		# fluent pageobject позволяет вызывать метод цепочкой
		return self

	def autocomplete(self, *values):
		for value in values:
			self.element.type(value).press_tab()

# примеры ввода
"""
TagsInput(browser.element('#subjectsInput'))

TagsInput.by_name('subjects')
"""