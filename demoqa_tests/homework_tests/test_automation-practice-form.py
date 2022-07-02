from selene.support.shared import browser
from selene import be, have, command
from demoqa_tests.utils import resource


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
    DATE OF BIRTH
    """
    browser.element('#dateOfBirthInput').click()
    browser.element('[value="1990"]').click()
    browser.element('#react-datepicker__month-select')
    browser.element('[value="3"]').click()
    day_of_born_button = browser.element(
        '[class="react-datepicker__day react-datepicker__day--023"]')
    day_of_born_button.click()

    """
    SUBJECTS & HOBBIES
    """
    browser.element('#subjectsInput').type(Subjects.computer_science).press_enter()
    browser.all('.subjects-auto-complete__option').element_by(have.text(
        Subjects.computer_science))
    browser.element('#subjectsInput').type(Subjects.social_studies).press_enter()
    browser.all('.subjects-auto-complete__option').element_by(have.text(
        Subjects.social_studies))
    hobbies_checkbox = browser.element('#hobbiesWrapper').all('.custom-checkbox')
    hobbies_checkbox.element_by(have.exact_text(Hobbies.sports)).click()
    hobbies_checkbox.element_by(have.exact_text(Hobbies.music)).click()
    hobbies_checkbox.element_by(have.exact_text(Hobbies.reading)).click()

    """
    BROWSE PICTURE
    """
    browser.element('#uploadPicture').send_keys(resource(Student.picture))

    """
    ADDRESS
    """
    browser.element('#currentAddress').type(Student.currentAddress)

    """
    CITY AND STATE
    """
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('#react-select-3-option-1').element_by(have.exact_text(
        Student.state)).click()
    browser.element('#city').perform(command.js.scroll_into_view).click()
    browser.all('#react-select-4-option-0').element_by(have.exact_text(
        Student.city)).click()

    """
    CLICK SUBMIT AND ASSERT MODAL
    """
    browser.element("#submit").perform(command.js.click)
    browser.all('.modal-dialog').should(be.present)

    """
    ASSERT REGISTER FORM
    """
    def cells_of_row(index, should_have_texts: list[str]):
        browser.element('.modal-dialog').all('table tr')[index].all('td').should(
            have.exact_texts(*should_have_texts)
        )
    cells_of_row(index=1, should_have_texts=[
        'Student Name',
        f'{Student.name} {Student.surname}'
    ])
    cells_of_row(index=2, should_have_texts=[
        'Student Email',
        Student.email
    ])
    cells_of_row(index=3, should_have_texts=[
        'Gender',
        Gender.male
    ])
    cells_of_row(index=4, should_have_texts=[
        'Mobile',
        Student.mobileNumber
    ])
    cells_of_row(index=5, should_have_texts=[
        'Date of Birth',
        f'{Student.birthDay} {Student.birthMonthName},{Student.birthYear}'
    ])
    cells_of_row(index=6, should_have_texts=[
        'Subjects',
        f'{Subjects.computer_science}, {Subjects.social_studies}'
    ])
    cells_of_row(index=7, should_have_texts=[
        'Hobbies',
        f'{Hobbies.sports}, {Hobbies.music}, {Hobbies.reading}'
    ])
    cells_of_row(index=8, should_have_texts=[
        'Picture',
        Student.picture
    ])
    cells_of_row(index=9, should_have_texts=[
        'Address',
        Student.currentAddress
    ])
    cells_of_row(index=10, should_have_texts=[
        'State and City',
        f'{Student.state} {Student.city}'
    ])

    """
    CLOSE AND ASSERT MODAL
    """
    browser.element('[id="closeLargeModal"]').click()
    browser.element('[id="closeLargeModal"]').should(be._not_.present)
