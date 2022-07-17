from selene import have, be
from selene.support.shared import browser

from demoqa_tests.ui.controls.table import TableControl


class ModalDialog():

	def __init__(self):
		self.element = browser.element('.modal-dialog')
		self.table = TableControl(self.element.element('.table'))

	def should_have_row_with_exact_texts(self, value):
		self.table.check_cells_of_row(1).should(have.exact_texts('Student Name', value))
		return self

	def close_modal_and_check_result(self):
		browser.element('#closeLargeModal').click()
		browser.element('[id="closeLargeModal"]').should(be._not_.present)
		return self

