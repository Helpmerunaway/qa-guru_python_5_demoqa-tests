from typing import Optional
from selene import command, have
from selene.support.shared import browser
from demoqa_tests import utils


class StudentRegistrationForm:

    def set_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

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
        return self

    def set_date_of_birth(self, day: int, month: int, year: int):
        browser.element('#dateOfBirthInput').click()
        browser.element('[class*="month-select"]').click().element(f'[value="{month - 1}"]').click()
        browser.element('[class*="year-select"]').click().element(f'[value="{year}"]').click()
        browser.element(f'[class*="datepicker__day--0{day}"]').click()
        return self

    def add_subject(self, from_: str, /, *, autocomplete: Optional[str] = None):
        browser.element('#subjectsInput').type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()
        # fluent pageobject позволяет вызывать метод цепочкой
        return self

    def add(self, from_: str, /, *, autocomplete: Optional[str] = None):
        browser.element.type(from_)
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
        return self

    def select_city(self, /, *, option: str):
        browser.element('#city').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select-][id*=-option]') \
            .element_by(have.exact_text(option)).click()
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self