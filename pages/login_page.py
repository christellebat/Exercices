from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    PAGE_TITLE = (By.TAG_NAME, "h2")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open_page(self):
        self.open(self.URL)

    def is_login_page_displayed(self):
        title = self.get_text(*self.PAGE_TITLE)
        return "Login Page" in title

    def login(self, username, password):
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)