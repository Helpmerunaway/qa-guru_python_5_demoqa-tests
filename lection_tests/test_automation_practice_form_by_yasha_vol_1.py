from selene.support.shared import browser
from selene import have, command

from demoqa_tests.utils import resource, upload_resource


def arrange_student_registration_form_opened():
	browser.open('/automation-practice-form')
	(
		browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10)
		.should(have.size_greater_than_or_equal(2)).perform(command.js.remove)
	)
	# remove ads


class Gender:
	male = 'Male'
	female = 'Female'
	other = 'Other'


class Hobbies:
	sports = 'Sports'
	reading = 'Reading'
	music = 'Music'


class Subjects:
	computer_science = 'Computer Science'
	english = 'English'


def test_register_student():
	"""
	This is test case to test practice form submition
	:return:
	"""
	arrange_student_registration_form_opened()

	class student:
		name = 'Rustam'
		surname = 'Tyapaev'
		email = 'test@gmail.com'
		mobileNumber = '1234567890'
		birthDay = '19'
		birthMonth = '11'
		birthMonthName = 'December'
		birthYear = '1988'
		currentAddress = 'ulica Pushkina dom Kolotyshkina'
		state = 'NCR'
		city = 'Delhi'


		# ACT
	browser.element('#firstName').type(student.name)
	browser.element('#lastName').type(student.surname)
	browser.element('#userEmail').type(student.email)

	gender_group = browser.element('#genterWrapper')
	gender_group.all('.custom-radio').element_by(have.exact_text(Gender.male)).click()


	mobileNumber = browser.element('#userNumber')
	mobileNumber.type(student.mobileNumber)

	browser.element('#dateOfBirthInput').click()
	# или
	browser.element('#dateOfBirthInput').perform(command.js.set_value('23 July 1988'))
	# или
	browser.element('#dateOfBirthInput').with_(set_value_by_js=True).set_value('23 July 1988').click()
	###
	browser.element(f'.react-datepicker__year-select').element(f'[value')
	browser.element(f'. react-datepicker__month-select [value="{student.birthMonth}]"]').click()
	browser.element(f' .react-datepicker__day--0{student.birthDay}').click()



	browser.element('#subjectsInput').type(Subjects.english).press_enter()
	browser.all('.subjects-auto-complete__option').element_by(have.text(Subjects.english))

	def autocomplete(selector: str, /, *,  from_: str, to: str = None):
		browser.element(selector).type(from_)
		browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
			to if to is None else from_
		))
		# if to is not None:
		# 	browser.all('.subjects-auto-complete__option').element_by(have.exact_text(to))
		# else:
		# 	browser.all('.subjects-auto-complete__option').element_by(have.exact_text(from_))
	autocomplete('#subjectsInput', from_='Com', to=Subjects.computer_science)
	autocomplete('#subjectsInput', from_=Subjects.english)

	browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(Hobbies.music)).click()
	# реализация хелпера аплоада файла, путь до картинки

	browser.element('#uploadPicture').send_keys(resource("screen.png"))

	browser.element('#uploadPicture').perform(upload_resource('screen.png'))

	browser.element('#currentAddress').type(student.currentAddress)

	# * - разделитель необходимый для добавления обязательного требования option
	# / - не нужно указывать например selector = '#state'
	def select_dropdown(selector, /, *, option: str):
		browser.element(selector).click()
		browser.all('[id^=[react-select][id*=option]')\
			.element_by(have.exact_text(option)).click()
	select_dropdown('#state', option=student.state)
	select_dropdown('#city', option=student.city)

	# или так, без функции
	browser.element('#state').element('input').type(student.state).press_tab()
	browser.element('#city').element('input').type(student.city).press_tab()

	# вместо парент элемент используем element('..')
	browser.element('#submit').element('..').perform(command.js.click)

# ASSERT 1 VARIANT проверяет только наличие текста
	browser.elements('table tr').element(1).should(have.text(student.name))
	browser.elements('table tr').element(1).should(have.text(student.surname))
	browser.elements('table tr').element(2).should(have.text(student.email))
	browser.elements('table tr').element(3).should(have.text(Gender.male))
	browser.elements('table tr').element(4).should(have.text(student.mobileNumber))
	browser.elements('table tr').element(5).should(have.text(student.birthYear))
	browser.elements('table tr').element(5).should(have.text(student.birthMonth))
	# browser.elements('table tr').element(5).should(have.text(student.birthDay))
	# browser.elements('table tr').element(6).should(have.text(Subjects.computer_science))
	# browser.elements('table tr').element(6).should(have.text(Subjects.english))


	# ASSERT 2 VARIANT проверяет наличие и последовательность расположения текста
	browser.all('table tr')[5].all('td')[1].should(have.exact_text(
		f'{student.birthDay} {student.birthMonth},{student.birthYear}'
	))
	# ASSERT 3 VARIANT проверяет всю строку, находим модалку, таблицу и ячейки
	def cells_of_row(index, should_have_texts: list[str]):
		browser.element('.modal-dialog').all('table tr')[index].all('td').should(
			have.exact_texts(*should_have_texts)
		)
	cells_of_row(index=5, should_have_texts=[
		'Date of Birth',
		f'{student.birthDay} {student.birthMonth}, {student.birthYear}'
	])
	cells_of_row(index=6, should_have_texts=[
		'Subjects',
		f'{Subjects.computer_science}, {Subjects.english}'
	])


	# browser.elements('table tr').element(7).should(have.text(Hobbies.music))
	# browser.elements('table tr').element(8).should(have.text(""))
	# browser.elements('table tr').element(9).should(have.text(student.currentAddress))
	# browser.elements('table tr').element(10).should(have.text(student.state))
	# browser.elements('table tr').element(10).should(have.text(student.city))

# selectors:
#foobar - css id foobar
# [id=foo] [name=bar] - css with parent
# //*[@id='foo' ]//*[@name='bar']