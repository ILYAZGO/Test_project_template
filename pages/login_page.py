from playwright.sync_api import Page, expect
from pytest_base_url.plugin import base_url

from utils.variables import *

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 20000
        self.accept_default_city = page.locator('[class$="choice-city"]').locator('[class$="button normal"]')
        self.enter_button_in_main_window = page.locator('[class="log-in link"]')
        self.button_profile_in_main_window = page.locator('[href="/profile/settings"]')
        self.modal_window = page.locator('#modal')
        self.toggle_active = page.locator('[class="button toggle small active"]')
        self.toggle_not_active = page.locator('[class="button toggle small"]')
        self.phone_input = page.locator('[data-test="renderless-masked-phone"]').locator('[data-test="input"]')
        self.email_input = page.locator('[type="email"]')
        self.password_input = page.locator('[type="password"]')
        self.enter_button_in_modal_window = page.locator('[data-test="enter"]')
        self.error_message_in_modal_window = page.locator('[data-test="error"]')


    def navigate(self, url):
        """Opens main page"""
        self.page.goto(url)
        self.accept_default_city.click()

    def press_enter_from_main_page(self):
        """Press enter from main page"""
        self.enter_button_in_main_window.click()
        self.page.wait_for_selector('#modal', timeout=self.timeout)

    def switch_toggle_switch(self):
        """Switch toggle switch from active to not active"""
        self.toggle_not_active.click()

    def login_with_phone(self, phone: str, password: str):
        """Login with phone"""
        self.phone_input.type(phone, delay=100)
        self.password_input.type(password, delay=100)

    def login_with_email(self, email: str, password: str):
        """Login with email"""
        self.email_input.type(email, delay=100)
        self.password_input.type(password, delay=100)

    def press_enter_from_modal_window(self):
        """Press enter from modal window"""
        self.enter_button_in_modal_window.click()

    def assert_login_successful(self):
        """Check that after login (enter) button changed to (profile) """
        self.page.wait_for_selector('#modal', state="hidden", timeout=self.timeout)
        self.page.wait_for_selector('[href="/profile/settings"]')
        expect(self.button_profile_in_main_window).to_have_text("Профиль")

    def get_error_message(self):
        """Returns error message text"""
        return self.error_message_in_modal_window.inner_text()
