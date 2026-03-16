from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class AddRemovePage(BasePage):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    HEADER = (By.TAG_NAME, "h3")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "#elements button.added-manually")

    def open_page(self):
        self.open(self.URL)

    def is_page_displayed(self):
        header = self.get_text(*self.HEADER)
        return "Add/Remove Elements" in header

    def click_add_element(self, times=1):
        for expected_count in range(1, times + 1):
            button = self.find_clickable(*self.ADD_BUTTON)

            try:
                button.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", button)

            try:
                self.wait.until(
                    lambda driver: len(driver.find_elements(*self.DELETE_BUTTONS)) == expected_count
                )
            except TimeoutException:
                actual_count = self.count_delete_buttons()
                raise TimeoutException(
                    f"Après clic sur 'Add Element', le nombre attendu était {expected_count}, "
                    f"mais le nombre réel est {actual_count}."
                )

    def count_delete_buttons(self):
        return len(self.driver.find_elements(*self.DELETE_BUTTONS))

    def delete_one_element(self):
        current_count = self.count_delete_buttons()

        if current_count > 0:
            buttons = self.driver.find_elements(*self.DELETE_BUTTONS)

            try:
                buttons[0].click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", buttons[0])

            try:
                self.wait.until(
                    lambda driver: len(driver.find_elements(*self.DELETE_BUTTONS)) == current_count - 1
                )
            except TimeoutException:
                actual_count = self.count_delete_buttons()
                raise TimeoutException(
                    f"Après suppression, le nombre attendu était {current_count - 1}, "
                    f"mais le nombre réel est {actual_count}."
                )

    def delete_all_elements(self):
        while self.count_delete_buttons() > 0:
            self.delete_one_element()