from demoqa_tests.data.data import User
from demoqa_tests.ui.pages.student_registration_page import StudentRegistrationForm

# STEPS OBJECTS
class StudentRegistrationSteps:
	def __init__(self):
		self.form = StudentRegistrationForm()

	# высокоуровневые шаги
	def fill_form(self, user: User):
		# self.set_first_name(first_name).set_last_name(last_name).add_subjects(*subjects)
		self.form.set_first_name(user.first_name)
		self.form.set_last_name(user.last_name)
		self.form.add_subjects(*user.subjects)
		self.form.submit()