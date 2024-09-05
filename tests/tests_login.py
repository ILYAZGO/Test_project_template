from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import pytest
import allure
from utils.variables import *

"""
Hi! this is demo-project. Here i gave few examples how i can test login for https://fix-price.com/ in Page Object pattern.
Also i attached .gitlab-ci.yml that needs a little tweaking to make it work correctly.
And also allure steps i made for first 3 tests as example

"""


#  login by phone

@pytest.mark.login
@pytest.mark.positive
@allure.title("test_login_by_phone_correct_phone_correct_password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_phone_correct_phone_correct_password")
def test_login_by_phone_correct_phone_correct_password(page):
    login_page = LoginPage(page)
    with allure.step("Go to url"):
        login_page.navigate()
    with allure.step("Press (Enter) from main page"):
        login_page.press_enter_from_main_page()
    with allure.step("Try to login"):
        login_page.login_with_phone(phone, password)
    with allure.step("Press (Enter) from modal window"):
        login_page.press_enter_from_modal_window()
    with allure.step("Check error message"):
        login_page.assert_login_successful()

@pytest.mark.login
@pytest.mark.negotive
@allure.title("test_login_by_phone_empty_phone_empty_password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_phone_empty_phone_empty_password")
def test_login_by_phone_empty_phone_empty_password(page):
    login_page = LoginPage(page)
    with allure.step("Go to url"):
        login_page.navigate()
    with allure.step("Press (Enter) from main page"):
        login_page.press_enter_from_main_page()
    with allure.step("Press (Enter) from modal window"):
        login_page.press_enter_from_modal_window()
    with allure.step("Check error message"):
        assert login_page.get_error_message() == 'Требуется указать телефон'

@pytest.mark.login
@pytest.mark.negotive
@allure.title("test_login_by_phone_incorrect_password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_phone_incorrect_password")
def test_login_by_phone_incorrect_password(page):
    login_page = LoginPage(page)
    with allure.step("Go to url"):
        login_page.navigate()
    with allure.step("Press (Enter) from main page"):
        login_page.press_enter_from_main_page()
    with allure.step("Try to login"):
        login_page.login_with_phone(phone, 'incorrect_password')
    with allure.step("Press (Enter) from modal window"):
        login_page.press_enter_from_modal_window()
    with allure.step("Check error message"):
        assert 'Неверный логин или пароль. Проверьте введённые данные и попробуйте снова. Осталось попыток:' in login_page.get_error_message()

@pytest.mark.login
@pytest.mark.negotive
@allure.title("test_login_by_phone_empty_password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_phone_empty_password")
def test_login_by_phone_empty_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.press_enter_from_main_page()
    login_page.login_with_phone(phone, '')
    login_page.press_enter_from_modal_window()
    assert login_page.get_error_message() == 'Неверный логин или пароль'

@pytest.mark.login
@pytest.mark.negotive
@allure.title("test_login_by_phone_invalid_phone")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_phone_invalid_phone")
def test_login_by_phone_invalid_phone(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.press_enter_from_main_page()
    login_page.login_with_phone("123456789", password)
    login_page.press_enter_from_modal_window()
    assert login_page.get_error_message() == 'Укажите корректный номер телефона'

@pytest.mark.login
@pytest.mark.negotive
@allure.title("test_login_by_phone_from_other_country")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_phone_from_other_country")
def test_login_by_phone_from_other_country(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.press_enter_from_main_page()
    login_page.login_with_phone("6919160252", password)
    login_page.press_enter_from_modal_window()
    assert login_page.get_error_message() == 'Формат телефонного номера не соответствует Вашей стране'

@pytest.mark.login
@pytest.mark.negotive
@allure.title("test_login_by_phone_letters_phone")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_phone_letters_phone")
def test_login_by_phone_letters_phone(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.press_enter_from_main_page()
    login_page.login_with_phone("number", password)
    login_page.press_enter_from_modal_window()
    assert login_page.get_error_message() == 'Требуется указать телефон'

#  login by email

@pytest.mark.login
@pytest.mark.positive
@pytest.mark.email
@allure.title("test_login_by_email_correct_email_correct_password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_email_correct_email_correct_password")
def test_login_by_email_correct_email_correct_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.press_enter_from_main_page()
    login_page.switch_toggle_switch()
    login_page.login_with_email(email, password)
    login_page.press_enter_from_modal_window()
    login_page.assert_login_successful()

@pytest.mark.login
@pytest.mark.negotive
@pytest.mark.email
@allure.title("test_login_by_email_empty_email_empty_password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_email_empty_email_empty_password")
def test_login_by_email_empty_email_empty_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.press_enter_from_main_page()
    login_page.switch_toggle_switch()
    login_page.press_enter_from_modal_window()
    assert login_page.get_error_message() == 'Требуется указать email'

@pytest.mark.login
@pytest.mark.negotive
@pytest.mark.email
@allure.title("test_login_by_email_incorrect_password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("test_login_by_email_incorrect_password")
def test_login_by_email_incorrect_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.press_enter_from_main_page()
    login_page.switch_toggle_switch()
    login_page.login_with_email(email, 'incorrect_password')
    login_page.press_enter_from_modal_window()
    assert 'Неверный логин или пароль. Проверьте введённые данные и попробуйте снова. Осталось попыток:' in login_page.get_error_message()

