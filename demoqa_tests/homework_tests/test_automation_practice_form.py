from selene.support.shared import browser
from selene import be, have, command
from demoqa_tests import utils
from demoqa_tests.controls.datepicker import DatePicker
from demoqa_tests.controls.dropdown import DropDown
from demoqa_tests.controls.tags_input_ import TagsInput
from demoqa_tests.controls.table import TableControl


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

    """
    DATE OF BIRTH HW6 POINT 2.3
    """
    date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
    date_of_birth.choose_date(23, 4, 1990)

    """
    SUBJECTS & HOBBIES HW6 POINT 2.1
    """
    subjects = TagsInput(browser.element('#subjectsInput'))
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

    """
    CLICK SUBMIT AND ASSERT MODAL
    """
    browser.element("#submit").perform(command.js.click)
    browser.all('.modal-dialog').should(be.present)

    """
    ASSERT REGISTER FORM HW6 POINT 2.4
    """
    results = TableControl(browser.element('.modal-content .table'))
    results.cells_of_row(0).should(have.exact_texts(
        'Student Name',
        f'{Student.name} {Student.surname}'))
    results.cells_of_row(1).should(have.exact_texts(
        'Student Email',
        f'{Student.email}'))
    results.cells_of_row(2).should(have.exact_texts(
        'Gender',
        f'{Gender.male}'))
    results.cells_of_row(3).should(have.exact_texts(
        'Mobile',
        f'{Student.mobileNumber}'))
    results.cells_of_row(4).should(have.exact_texts(
        'Date of Birth',
        f'{Student.birthDay} {Student.birthMonthName},{Student.birthYear}'))
    results.cells_of_row(5).should(have.exact_texts(
        'Subjects',
        f'{Subjects.computer_science}, {Subjects.social_studies}, '
        f'{Subjects.chemistry}, {Subjects.maths}, {Subjects.physics}'))
    results.cells_of_row(6).should(have.exact_texts(
        'Hobbies',
        f'{Hobbies.sports}, {Hobbies.music}, {Hobbies.reading}'))
    results.cells_of_row(7).should(have.exact_texts(
        'Picture',
        Student.picture))
    results.cells_of_row(8).should(have.exact_texts(
        'Address',
        Student.currentAddress))
    results.cells_of_row(9).should(have.exact_texts(
        'State and City',
        f'{Student.state} {Student.city}'))

    """
    CLOSE AND ASSERT MODAL
    """
    browser.element('[id="closeLargeModal"]').click()
    browser.element('[id="closeLargeModal"]').should(be._not_.present)
