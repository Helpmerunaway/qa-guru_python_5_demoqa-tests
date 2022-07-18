from selene import have
from demoqa_tests.data.data import User, Subjects, Hobbies
from demoqa_tests.ui.application_manager import app


def test_register_student_dev_patel(open_auto_practice_form):
    student = User()
    """
    NAME AND SURNAME
    """
    app.registration_form.set_first_name(student.first_name)\
        .set_last_name(student.last_name)
    """
    OR
    app.registration_form.set_first_name('Dev').set_last_name('Patel')
    """

    "EMAIL"
    app.registration_form.set_email(student.email)
    """
    OR
    app.registration_form.set_email('dev_patel@gmail.com')
    """

    """
    GENDER
    """
    app.registration_form.set_male_gender()
    """
    OR
    app.registration_form.set_male_gender()
    """

    """
    MOBILE NUMBER
    """
    app.registration_form.set_mobile_number(student.mobile_number)
    """
    OR
    app.registration_form.set_mobile_number('9999119999')
    """

    """
    DATE OF BIRTH
    """
    app.registration_form.set_date_of_birth(student.birthday_day, student.birthday_month, student.birthday_year)

    """
    OR
    app.registration_form.set_date_of_birth(23, 4, 1990)
    """

    """
    SUBJECTS HW7 POINT 1 FLUENT PAGEOBJECT
    """
    # app.registration_form \
    #     .add_subject('Comp', autocomplete='Computer Science') \
    #     .add_subject('Social') \
    #     .add_subject('Chem', autocomplete='Chemistry') \
    #     .add_subject('Maths') \
    #     .add_subject('Physics')


    app.registration_form.add_subject(student.subjects)


    """
    HOBBIES
    """
    app.registration_form \
        .add_hobbies('Sports') \
        .add_hobbies('Reading') \
        .add_hobbies('Music')

    """
    OR
    app.registration_form.add_hobbies(student.hobbies)
    """

    """
    BROWSE PICTURE HW6 POINT 1.1
    """
    app.registration_form.browse_picture(student.picture)
    """
    
    OR
    app.registration_form.browse_picture('screen.png')
    """

    """
    ADDRESS
    """
    app.registration_form.set_address(student.address)

    """
    OR
    app.registration_form.set_address('Milky Way, Solar System, Earth')
    """

    """
    CITY AND STATE HW6 POINT 2.2
    """
    app.registration_form.select_state(option=student.state)
    app.registration_form.select_city(option=student.city)

    """
    OR
    app.registration_form.select_state(option='Uttar Pradesh')
    app.registration_form.select_city(option='Agra')
    """

    """
    CLICK SUBMIT AND ASSERT MODAL
    """
    app.registration_form.submit()

    """
    ASSERT REGISTER FORM FROM MODAL TABLE
    """
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
    """
    app.results_modal.table.check_cells_of_row(6).should(have.exact_texts(
        'Subjects', f'{student.subjects}'))
    """
    app.results_modal.table.check_cells_of_row(7).should(have.exact_texts(
        'Hobbies', f'{Hobbies.sports}, {Hobbies.reading}, {Hobbies.music}'))
    """
    app.results_modal.table.check_cells_of_row(7).should(have.exact_texts(
        'Hobbies', f'{student.hobbies}'))
    """
    app.results_modal.table.check_cells_of_row(8).should(have.exact_texts(
        'Picture', student.picture))
    app.results_modal.table.check_cells_of_row(9).should(have.exact_texts(
        'Address', student.address))
    app.results_modal.table.check_cells_of_row(10).should(have.exact_texts(
        'State and City', f'{student.state} {student.city}'))

    """
    CLOSE AND ASSERT MODAL
    """
    app.results_modal.close_modal_and_check_result()
