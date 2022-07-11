from selene.support.shared import browser


class DatePicker:

	def __init__(self, element):
		self.element = element

	def choose_date(self, day: int, month: int, year: int):
		self.element.click()
		browser.element('[class*="month-select"]').click().element(f'[value="{month - 1}"]').click()
		browser.element('[class*="year-select"]').click().element(f'[value="{year}"]').click()
		browser.element(f'[class*="datepicker__day--0{day}"]').click()
