from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dropdown"

    DROPDOWN = (By.ID, "dropdown")
    HEADER = (By.TAG_NAME, "h3")

    def open_page(self):
        self.open(self.URL)

    def is_dropdown_page_displayed(self):
        header = self.get_text(*self.HEADER)
        return "Dropdown List" in header

    def is_dropdown_present(self):
        return self.is_visible(*self.DROPDOWN)

    def select_option_by_text(self, text):
        dropdown = self.find(*self.DROPDOWN)
        Select(dropdown).select_by_visible_text(text)

    def get_selected_option(self):
        dropdown = self.find(*self.DROPDOWN)
        return Select(dropdown).first_selected_option.text.strip()