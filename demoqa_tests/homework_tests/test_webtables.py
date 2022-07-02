from selene.support.shared import browser
from selene import be, have


def test_web_tables(open_webtables_page):
    browser.element('#addNewRecordButton').click()

    # CHECK MODAL WINDOW
    user_form = browser.element('[id="userForm"]')
    user_form.should(be.present)

    # ADD NEW RECORD 4
    first_name_input = browser.element('[id="firstName"]')
    first_name_input.type('Dev')
    last_name_input = browser.element('[id="lastName"]')
    last_name_input.type('Patel')
    user_email_input = browser.element('[id="userEmail"]')
    user_email_input.type('dev_patel@gmail.com')
    age_input = browser.element('[id="age"]')
    age_input.type('32')
    salary_input = browser.element('[id="salary"]')
    salary_input.type('10000000')
    departament_input = browser.element('[id="department"]')
    departament_input.type('Hollywood')
    submit_button = browser.element('#submit')
    submit_button.click()

    # CHECK FORM
    user_form.should(be._not_.present)

    # ASSERT RECORD 4
    # TODO: make assert like in test_automation_practice_form
    browser.element('[class="rt-table"]') \
        .should(have.text('Dev')) \
        .should(have.text('Patel')) \
        .should(have.text('dev_patel@gmail.com')) \
        .should(have.text('32')) \
        .should(have.text('10000000')) \
        .should(have.text('Hollywood'))

    # EDIT INFO ON RECORD 2
    browser.element('#edit-record-2').click()
    user_form.should(be.present)
    first_name_input.set_value('John')
    last_name_input.set_value('Cena')
    user_email_input.set_value('john_cena@gmail.com')
    age_input.set_value('44')
    salary_input.set_value('8500000')
    departament_input.set_value('WWE')
    submit_button.click()
    user_form.should(be._not_.present)

    # ASSERT RECORD 2
    # TODO: make assert like in test_automation_practice_form
    browser.element('[class="rt-table"]') \
        .should(have.text('John')) \
        .should(have.text('Cena')) \
        .should(have.text('john_cena@gmail.com')) \
        .should(have.text('44')) \
        .should(have.text('8500000')) \
        .should(have.text('WWE'))

    # DELETE RECORD 3
    browser.element('#delete-record-3').click()

    # ASSERT RECORD 3
    # TODO: make assert like in test_automation_practice_form
    browser.element('[class="rt-tr -odd"]')\
        .should_not(have.text('Kierra'))\
        .should_not(have.text('Gentry'))\
        .should_not(have.text('29'))\
        .should_not(have.text('kierra@example.com'))\
        .should_not(have.text('2000'))\
        .should_not(have.text('Legal'))
