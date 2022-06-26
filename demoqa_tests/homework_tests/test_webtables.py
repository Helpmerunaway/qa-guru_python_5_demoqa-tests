from selene.support.shared import browser
from selene import be, have


def test_web_tables(open_webtables_page):
    browser.element('#addNewRecordButton').click()
    # проверяем что модалка появилась
    user_form = browser.element('[id="userForm"]')
    user_form.should(be.present)
    # добавляем новую строчку
    first_name_input = browser.element('[id="firstName"]')
    first_name_input.click().type('Dev')
    last_name_input = browser.element('[id="lastName"]')
    last_name_input.click().type('Patel')
    user_email_input = browser.element('[id="userEmail"]')
    user_email_input.click().type('dev_patel@gmail.com')
    age_input = browser.element('[id="age"]')
    age_input.click().type('32')
    salary_input = browser.element('[id="salary"]')
    salary_input.click().type('10000000')
    departament_input = browser.element('[id="department"]')
    departament_input.click().type('Hollywood')
    submit_button = browser.element('#submit')
    submit_button.click()
    user_form.should(be._not_.present)
    # проверяем что отправленная форма присутствует на странице
    browser.element('[class="rt-table"]') \
        .should(have.text('Dev')) \
        .should(have.text('Patel')) \
        .should(have.text('dev_patel@gmail.com')) \
        .should(have.text('32')) \
        .should(have.text('10000000')) \
        .should(have.text('Hollywood'))
    # меняем информацию из второй строчки в таблице
    browser.element('#edit-record-2').click()
    user_form.should(be.present)
    first_name_input.should(have.value('Alden'))\
        .click().clear().type('John')
    last_name_input.should(have.value('Cantrell'))\
        .click().clear().type('Cena')
    user_email_input.should(have.value('alden@example.com'))\
        .click().clear().type('john_cena@gmail.com')
    age_input.should(have.value('45'))\
        .click().clear().type('44')
    salary_input.should(have.value('12000'))\
        .click().clear().type('8500000')
    departament_input.should(have.value('Compliance'))\
        .click().clear().type('WWE')
    submit_button.click()
    user_form.should(be._not_.present)
    # проверяем что измененная форма присутствует
    browser.element('[class="rt-table"]') \
        .should(have.text('John')) \
        .should(have.text('Cena')) \
        .should(have.text('john_cena@gmail.com')) \
        .should(have.text('44')) \
        .should(have.text('8500000')) \
        .should(have.text('WWE'))
    # удаляем 3 строчку и проверяем что она удалилась
    browser.element('#delete-record-3').click()
    browser.element('[class="rt-tr -odd"]')\
        .should_not(have.text('Kierra'))\
        .should_not(have.text('Gentry'))\
        .should_not(have.text('29'))\
        .should_not(have.text('kierra@example.com'))\
        .should_not(have.text('2000'))\
        .should_not(have.text('Legal'))
