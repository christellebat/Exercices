from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages2.base_page import BasePage


class DynamicLoadingPage(BasePage):

    URL = "https://the-internet.herokuapp.com/dynamic_loading"

    example2_link = (By.CSS_SELECTOR, "a[href='/dynamic_loading/2']")
    start_button = (By.CSS_SELECTOR, "#start button")
    hello_text = (By.CSS_SELECTOR, "#finish h4")

    def open_page(self):
        self.open(self.URL)

    def open_example2(self):
        self.click(self.example2_link)

    def click_start(self):
        self.click(self.start_button)

    def wait_hello_world(self):
        self.wait.until(
            EC.visibility_of_element_located(self.hello_text)
        )

    def get_hello_text(self):
        return self.get_text(self.hello_text)