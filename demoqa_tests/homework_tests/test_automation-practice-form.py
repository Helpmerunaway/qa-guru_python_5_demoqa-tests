from selene.support.shared import browser
from selene import be, have, command


def test_auto_practice_form(open_auto_practice_form):
    browser.element('#firstName').click().should(be.blank).type('Dev')
    browser.element('#lastName').click().should(be.blank).type('Patel')
    browser.element('#userEmail').click().should(be.blank).type('dev_patel@gmail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').click().should(be.blank).type('9999119999')
    browser.element('#dateOfBirthInput').click()
    browser.element('[value="1990"]').click()
    browser.element('#react-datepicker__month-select')
    browser.element('[value="3"]').click()
    day_of_born_button = browser.element('[class="react-datepicker__day react-datepicker__day--023"]')
    day_of_born_button.click()
    subjects_input = browser.element('#subjectsInput')
    subjects_input.click().clear().send_keys('Computer Science').press_enter()
    browser.element('#subjectsInput').click().clear().send_keys('Social Studies').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').type("/home/ruslan/Downloads/dev.png")
    browser.element('#currentAddress').perform(command.js.scroll_into_view).click()\
        .type("Milky Way, Solar System, Earth")
    browser.element('#state').click()
    browser.element('#react-select-3-input').type("Uttar Pradesh").press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Agra').press_enter().press_enter()
    browser.element('[class="modal-body"]')\
        .should(have.text('Dev Patel'))\
        .should(have.text('dev_patel@gmail.com'))\
        .should(have.text('Male'))\
        .should(have.text('9999119999'))\
        .should(have.text('23 April,1990'))\
        .should(have.text('Computer Science')) \
        .should(have.text('Social Studies')) \
        .should(have.text('Sports'))\
        .should(have.text('dev.png'))\
        .should(have.text('Milky Way, Solar System, Earth'))\
        .should(have.text('Uttar Pradesh Agra'))
    browser.element('[id="closeLargeModal"]').click()
