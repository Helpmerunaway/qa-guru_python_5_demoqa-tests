from selene import have
from demoqa_tests.data.data import User, Subjects, Hobbies
from demoqa_tests.ui.application_manager import app


def test_register_student_dev_patel(open_auto_practice_form):
	student = User()
	app.registration_form.set_first_name(student.first_name) \
		.set_last_name(student.last_name).set_email(student.email)\
		.set_male_gender()\
		.set_mobile_number(student.mobile_number)\
		.set_date_of_birth(student.birthday_day, student.birthday_month, student.birthday_year)\
		.add_subject(student.subjects).\
		add_hobbies(student.hobbies).\
		browse_picture(student.picture)\
		.set_address(student.address)\
		.select_state(option=student.state)\
		.select_city(option=student.city)\
		.submit()

	app.results_modal.table.check_cells_of_row(1).should(have.exact_texts(
		'Student Name', f'{student.first_name} {student.last_name}'))
	app.results_modal.table.check_cells_of_row(2).should(have.exact_texts(
		'Student Email', f'{student.email}'))
	app.results_modal.table.check_cells_of_row(3).should(have.exact_texts(
		'Gender', f'{student.gender}'))
	app.results_modal.table.check_cells_of_row(4).should(have.exact_texts(
		'Mobile', f'{student.mobile_number}'))
	app.results_modal.table.check_cells_of_row(5).should(have.exact_texts(
		'Date of Birth', f'{student.birthday_day} {student.birthday_month_name},{student.birthday_year}'))
	app.results_modal.table.check_cells_of_row(6).should(have.exact_texts(
		'Subjects',
		f'{Subjects.computer_science}, {Subjects.social_studies}, '
		f'{Subjects.chemistry}, {Subjects.maths}, {Subjects.physics}'))
	app.results_modal.table.check_cells_of_row(6).should(have.exact_texts(
		'Subjects', f'{student.subjects}'))
	app.results_modal.table.check_cells_of_row(7).should(have.exact_texts(
		'Hobbies', f'{Hobbies.sports}, {Hobbies.reading}, {Hobbies.music}'))
	app.results_modal.table.check_cells_of_row(7).should(have.exact_texts(
		'Hobbies', f'{student.hobbies}'))
	app.results_modal.table.check_cells_of_row(8).should(have.exact_texts(
		'Picture', student.picture))
	app.results_modal.table.check_cells_of_row(9).should(have.exact_texts(
		'Address', student.address))
	app.results_modal.table.check_cells_of_row(10).should(have.exact_texts(
		'State and City', f'{student.state} {student.city}'))

	app.results_modal.close_modal_and_check_result()
