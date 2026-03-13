from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    URL = "https://practicesoftwaretesting.com/"

    PRODUCTS = (By.CSS_SELECTOR, ".card")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".card-title")
    CATEGORIES = (By.CSS_SELECTOR, "input[name='category_id']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def wait_products(self):
        self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCTS)
        )

    def get_categories(self):

        categories = self.driver.find_elements(*self.CATEGORIES)

        categories_list = []

        for cat in categories:
            label = cat.find_element(By.XPATH, "..").text
            categories_list.append((label, cat))

        return categories_list

    def select_category(self, category_element):
        category_element.click()

    def get_products(self):

        products = self.driver.find_elements(*self.PRODUCTS)

        product_names = []

        for product in products:
            name = product.find_element(*self.PRODUCT_NAME).text
            product_names.append(name)

        return product_names