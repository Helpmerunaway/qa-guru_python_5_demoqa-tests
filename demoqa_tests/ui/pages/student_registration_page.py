from typing import Optional

from selene import command, have
from selene.support.shared import browser

from demoqa_tests import utils

# PAGE OBJECT
class StudentRegistrationForm:
    """
    # когда не нужно получать индивидуальный обьект можно делать так:
    # поля класса
    # общие поля
    # first_name = browser.element('#firstName')
    # last_name = browser.element('#lastName')
    # subjects = TagsInput('subjectsInput')
    # submit = browser.element('#submit')

    # метод класса
    # @staticmethod
    # def do_something():
    #     ...

    # # низкоуровневые шаги, каждый элемент выписан в инит функцию
    # def __init__(self):
    #     # поля обьектов класса
    #     # индивидуальные поля
    #     self.first_name = browser.element('#firstName')
    #     self.last_name = browser.element('#lastName')
    #     self.subjects = TagsInput('subjectsInput')
    #     self.submit = browser.element('#submit')
    """


    # функция ввода имени, принадлежит обьекту класса - метод обьекта
    def set_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    """
    # # можно без инита, но тогда нужно будет привязать метод к классу (статик) и не будет возможности вернуть селф
    # @staticmethod
    # def set_first_nam_without_init(value):
    #     browser.element('#firstName').type('Harry')
    """

    def set_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def set_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def set_gender(self):
        gender_group = browser.element('#genterWrapper')
        gender_group.all('.custom-radio').element_by(have.exact_text('male')).click()
        return self

    def set_male_gender(self):
        browser.element('label[for="gender-radio-1"]').click()
        return self

    def set_mobile_number(self, num):
        browser.element('#userNumber').type(num)

    """
    # def set_birthday(self, value):
    #     browser.element('#dateOfBirthInput').type(value)

    # def set_birthday(self, option: str):
    #     browser.element('#dateOfBirthInput').perform(command.js.set_value(option)).press_enter()
    """

    def set_date_of_birth(self, day: int, month: int, year: int):
        browser.element('#dateOfBirthInput').click()
        browser.element('[class*="month-select"]').click().element(f'[value="{month - 1}"]').click()
        browser.element('[class*="year-select"]').click().element(f'[value="{year}"]').click()
        browser.element(f'[class*="datepicker__day--0{day}"]').click()

    def add_subject(self, from_: str, /, *, autocomplete: Optional[str] = None):
        browser.element('#subjectsInput').type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()
        # fluent pageobject позволяет вызывать метод цепочкой
        return self

    # функция добавления нового предмета
    def add_subjects(self, *names):
        for name in names:
            browser.element('#subjectsInput').add(name)
            return self

    # функция проверяет добавлен ли предмет
    def should_have_subjects(self, *names):
        browser.element('#subjectsInput').should(have.text(''.join(names)))
        return self

    def add_hobbies(self, hobby: str):
        hobby_checkbox = browser.element('#hobbiesWrapper').all('.custom-checkbox')
        hobby_checkbox.element_by(have.exact_text(hobby)).click()
        return self

    def browse_picture(self, pic_name: str):
        browser.element('#uploadPicture').send_keys(utils.paths.resource(pic_name))
        return self

    def set_address(self, address: str):
        browser.element('#currentAddress').type(address)
        return self

    def select_state(self, /, *, option: str):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select-][id*=-option]') \
            .element_by(have.exact_text(option)).click()

    def select_city(self, /, *, option: str):
        browser.element('#city').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select-][id*=-option]') \
            .element_by(have.exact_text(option)).click()

    def submit(self):
        browser.element('#submit').perform(command.js.click)

"""
# # высокоуровневые шаги
# 	def fill_form(self, first_name, last_name, subjects):
# 		# self.set_first_name(first_name).set_last_name(last_name).add_subjects(*subjects)
# 		self.form.set_first_name(first_name)
# 		self.form.set_last_name(last_name)
# 		self.form.add_subjects(*subjects)
# 		self.form.submit()
"""