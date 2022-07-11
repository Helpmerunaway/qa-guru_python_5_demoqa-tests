

class TableControl:
	def __init__(self, element):
		self.element = element

	def cells_of_row(self, index):
		return self.element.all('tbody tr')[index].all('td')