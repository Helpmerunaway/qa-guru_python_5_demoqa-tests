from selene.support.shared import browser
from selene.core.entity import Element


class Cell:
	def __init__(self, element: Element):
		self.element = element

	def start_editing(self):
		self.element.double_click()
		return self

	@property
	def input(self):
		return self.element.element('.input')

	def set(self, value):
		self.input.set_value(value)
		return self

	def save(self):
		self.input.press_enter()
		return self


class TableControl:

	def __init__(self, element: Element = None):
		self.element = element if element is not None \
			else browser.element('.table')

	def cell(self, row_index: int, column_index: int):
		return Cell(self.check_cells_of_row(row_index)[column_index])

	def check_cells_of_row(self, index):
		return self.rows[index].all('td')

	@property
	def rows(self):
		return self.element.all('tr')