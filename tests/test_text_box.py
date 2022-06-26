from selene import have, be, command
from selene.support.shared import browser

import pytest

def given_opened_text_box():
	browser.open('/text-box')
	browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).\
		should(have.size_greater_than_or_equal(1)).perform(command.js.remove)


def test_submit_form():
	given_opened_text_box()
	# точный поиск
	browser.should(have.title('ToolsQA'))
	# поиск по части
	browser.should(have.title_containing('QA'))

	browser.element('.main-header').should(have.exact_text('Text Box'))
	# XPATH
	# browser.element('[class="main-header"]')
	browser.element('#userName').type('yasha')
	browser.element('#userEmail').type('yashaka@gmail.com')
	browser.element('#currentAddress').type('Earth')
	browser.element('#permanentAddress').type('Universe & abroad')
	# скролл до элемента
	#browser.element('#submit').perform(command.js.scroll_into_view).click()

	# удалить рекламу можно при помощи скрипта на JS
	browser.execute_script(
		"""
		document.querySelectorAll("[id^=google_ads]")
			.forEach(element => element.remove())
		"""
	)
	# скрыть элемент JS
	browser.execute_script(
		"""
		document.querySelectorAll("[id^=google_ads]")
			.forEach(element => element.visibility = "hidden")
		"""
	)
	# удалить элемент рекламы
	browser.element('[id^=google_ads]')._execute_script('element.remove()')
	# или через селен
	for ads in browser.all('[id^=google_ads]'):
		ads._execute_script('element.remove()')
	# или так
	browser.all('[id^=google_ads]').perform(command.js.remove)

	browser.element('#submit').click().perform(command.js.click)
	# алл для всех элементов
	# XPATH
	# browser.all('//*[@id="output]"')
	browser.all('#output p').should(have.texts(
		'yasha',
		'yashaka@gmail.com',
		'Earth',
		'Universe & abroad',
	))
	# Второй current address - плохой селектор
	browser.all('#currentAddress')[1].should(have.text('Earth'))
	# двухсоставный селектор, более сложный - лучше так не делать
	browser.element('#output #currentAddress').should(have.text('Earth'))
	# разбить селектор на два, будем знать по какой причине упал и где именно - бест практис
	browser.element('#output').element('#currentAddress').should(have.text('Earth'))

	browser.element('#name').should(have.text('Earth'))
	browser.element('#name').should(have.value('Earth'))

	# XPATH
	browser.element('//*[@id = "userName"]')
	# CSS
	browser.all('custom-radio').element_by(have.exact_text('Impressive')).click()

	# класс включает в себя (~=)main-header, точный поиск exact_text
	# browser.element('[class~=main-header]').should(have.exact_text('Text Box'))
	# вместо ~= ставим . (точку)

	# поиск по части элемента
	# browser.element('[class=main-header]').should(have.text('Box'))

	# ассерты - should have url have title

