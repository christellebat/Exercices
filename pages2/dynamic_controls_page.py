from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages2.base_page import BasePage


class DynamicControlsPage(BasePage):

    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    checkbox = (By.ID, "checkbox")
    remove_add_button = (By.CSS_SELECTOR, "#checkbox-example button")
    message = (By.ID, "message")

    input_field = (By.CSS_SELECTOR, "#input-example input")
    enable_button = (By.CSS_SELECTOR, "#input-example button")

    def open_page(self):
        self.open(self.URL)

    def is_page_loaded(self):
        return "dynamic_controls" in self.driver.current_url

    def is_checkbox_present(self):
        return len(self.driver.find_elements(*self.checkbox)) > 0

    def click_remove(self):
        self.click(self.remove_add_button)

    def wait_checkbox_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(self.checkbox))

    def click_add(self):
        self.click(self.remove_add_button)

    def wait_checkbox_appear(self):
        self.wait.until(EC.presence_of_element_located(self.checkbox))

    def get_message(self):
        return self.get_text(self.message)

    def is_input_disabled(self):
        field = self.find(self.input_field)
        return not field.is_enabled()

    def click_enable(self):
        self.click(self.enable_button)

    def wait_input_enabled(self):
        self.wait.until(EC.element_to_be_clickable(self.input_field))

    def write_input(self, text):
        field = self.find(self.input_field)
        field.send_keys(text)

    def get_input_value(self):
        field = self.find(self.input_field)
        return field.get_attribute("value")