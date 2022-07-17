from enum import Enum

from selene.support.shared import browser
from selene import be, have, command
from demoqa_tests import utils
from demoqa_tests.data.data import User
from demoqa_tests.ui import application_manager
from demoqa_tests.ui.application_manager import app
from demoqa_tests.ui.components.modal_dialog import ModalDialog
from demoqa_tests.ui.controls.datepicker import DatePicker
from demoqa_tests.ui.controls.dropdown import DropDown
from demoqa_tests.ui.controls.tags_input_ import TagsInput
from demoqa_tests.ui.controls.table import TableControl
from demoqa_tests.ui.pages.student_registration_page import StudentRegistrationForm


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
    social_studies = 'Social Studies'
    chemistry = 'Chemistry'
    maths = 'Maths'
    physics = 'Physics'


class Student:
    name = 'Dev'
    surname = 'Patel'
    email = 'dev_patel@gmail.com'
    mobileNumber = '9999119999'
    birthDay = '23'
    birthMonthName = 'April'
    birthMonth = '03'
    birthYear = '1990'
    currentAddress = 'Milky Way, Solar System, Earth'
    state = 'Uttar Pradesh'
    city = 'Agra'
    picture = 'screen.png'




def test_register_student(open_auto_practice_form):
    harry_potter = User(
        first_name='Harry',
        last_name='Potter',
        subjects=['Computer Science', 'Social', 'Chemistry', 'Maths', 'Physics']
    )

    # высокоуровневый степ
    app.form.fill_form(harry_potter)
    # OR
    app.form.set_first_name('Harry').set_last_name('Potter')

    """
    NAME SURNAME AND EMAIL
    """
    browser.element('#firstName').type(Student.name)
    browser.element('#lastName').type(Student.surname)
    browser.element('#userEmail').type(Student.email)

    """
    GENDER
    """
    gender_group = browser.element('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text(
        Gender.male)).click()

    """
    MOBILE NUMBER
    """
    mobile_number = browser.element('#userNumber')
    mobile_number.type(Student.mobileNumber)

    # OR
    class Month(Enum):
        September = 8
        Aug = 7

    DatePicker(browser.element('#dateOfBirthInput')).open().select_month(Month.Aug).select_year(1999).select_date(30)
    app.form.set_birth_day(30, Month.Aug, 1999)
    """
    DATE OF BIRTH HW6 POINT 2.3
    """
    date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
    # date_of_birth.choose_date(23, 4, 1990)
    date_of_birth.enter_date('23 April 1990')

    # OR
    app.form.add_subjects('Computer Science', 'Social', 'Chemistry', 'Maths', 'Physics')
    app.form.should_have_subjects('Computer Science', 'Social', 'Chemistry', 'Maths', 'Physics')
    app.form.subjects.element.should(have.text(''.join(['Computer Science', 'Social', 'Chemistry', 'Maths', 'Physics'])))
    # тоже самое но через собственную функцию
    app.form.subjects.should_have_texts('Computer Science', 'Social', 'Chemistry', 'Maths', 'Physics')
    """
    SUBJECTS & HOBBIES HW6 POINT 2.1
    """

    subjects = TagsInput(browser.element('#subjectsInput'))
    # fluent pageobject
    (
    subjects.add('Comp', autocomplete='Computer Science')
        .add('Social')
        .add('Chem', autocomplete='Chemistry')
        .add('Maths')
        .add('Physics')
    )

    hobbies_checkbox = browser.element('#hobbiesWrapper').all('.custom-checkbox')
    hobbies_checkbox.element_by(have.exact_text(Hobbies.sports)).click()
    hobbies_checkbox.element_by(have.exact_text(Hobbies.music)).click()
    hobbies_checkbox.element_by(have.exact_text(Hobbies.reading)).click()

    """
    BROWSE PICTURE HW6 POINT 1.1
    """
    browser.element('#uploadPicture').send_keys(utils.paths.resource(Student.picture))

    """
    ADDRESS
    """
    browser.element('#currentAddress').type(Student.currentAddress)

    """
    CITY AND STATE HW6 POINT 2.2
    """
    state = DropDown(browser.element('#state'))
    state.select(option='Uttar Pradesh')
    city = DropDown(browser.element('#city'))
    city.select(option='Agra')

    # OR
    app.form.submit()
    """
    CLICK SUBMIT AND ASSERT MODAL
    """
    browser.element("#submit").perform(command.js.click)
    # OR


    """
    modal.table.cells_of_row(1).should(have.exact_texts('Student Name'))
    """
    app.modal.should_have_row_with_exact_texts('Student Name', 'Harry Potter')


    browser.all('.modal-dialog').should(be.present)

    """
    ASSERT REGISTER FORM HW6 POINT 2.4
    """
    results = TableControl(browser.element('.modal-content .table'))
    # results.cell(1, 2).start_editing().set('new value').save()
    results.check_cells_of_row(0).should(have.exact_texts(
        'Student Name',
        f'{Student.name} {Student.surname}'))
    results.check_cells_of_row(1).should(have.exact_texts(
        'Student Email',
        f'{Student.email}'))
    results.check_cells_of_row(2).should(have.exact_texts(
        'Gender',
        f'{Gender.male}'))
    results.check_cells_of_row(3).should(have.exact_texts(
        'Mobile',
        f'{Student.mobileNumber}'))
    results.check_cells_of_row(4).should(have.exact_texts(
        'Date of Birth',
        f'{Student.birthDay} {Student.birthMonthName},{Student.birthYear}'))
    results.check_cells_of_row(5).should(have.exact_texts(
        'Subjects',
        f'{Subjects.computer_science}, {Subjects.social_studies}, '
        f'{Subjects.chemistry}, {Subjects.maths}, {Subjects.physics}'))
    results.check_cells_of_row(6).should(have.exact_texts(
        'Hobbies',
        f'{Hobbies.sports}, {Hobbies.music}, {Hobbies.reading}'))
    results.check_cells_of_row(7).should(have.exact_texts(
        'Picture',
        Student.picture))
    results.check_cells_of_row(8).should(have.exact_texts(
        'Address',
        Student.currentAddress))
    results.check_cells_of_row(9).should(have.exact_texts(
        'State and City',
        f'{Student.state} {Student.city}'))

    """
    CLOSE AND ASSERT MODAL
    """
    browser.element('[id="closeLargeModal"]').click()
    browser.element('[id="closeLargeModal"]').should(be._not_.present)
