from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class SecureAreaPage(BasePage):
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")
    SECURE_HEADER = (By.CSS_SELECTOR, "div.example h2")

    def is_secure_area_displayed(self):
        try:
            self.wait.until(lambda driver: "/secure" in driver.current_url)
            header = self.get_text(*self.SECURE_HEADER)
            return "Secure Area" in header
        except Exception:
            return False

    def get_flash_message(self):
        return self.get_text(*self.FLASH_MESSAGE)

    def is_logout_visible(self):
        return self.is_visible(*self.LOGOUT_BUTTON)

    def logout(self):
        self.click(*self.LOGOUT_BUTTON)