from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        self.find_clickable(by, value).click()

    def type(self, by, value, text, clear_first=True):
        element = self.find(by, value)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text.strip()

    def is_visible(self, by, value):
        try:
            self.wait.until(EC.visibility_of_element_located((by, value)))
            return True
        except Exception:
            return False

    def save_screenshot(self, filename="error.png"):
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)
        path = screenshots_dir / filename
        self.driver.save_screenshot(str(path))
        print(f"[SCREENSHOT] Capture enregistrée : {path}")