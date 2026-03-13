from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from book import Book


class BooksPage:

    URL = "https://books.toscrape.com"

    BOOKS = (By.CSS_SELECTOR, ".product_pod")
    TITLE = (By.CSS_SELECTOR, "h3 a")
    PRICE = (By.CSS_SELECTOR, ".price_color")
    STOCK = (By.CSS_SELECTOR, ".instock")
    RATING = (By.CSS_SELECTOR, ".star-rating")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.URL)

    def wait_books(self):
        self.wait.until(
            EC.presence_of_all_elements_located(self.BOOKS)
        )

    def extract_books(self):

        books_data = []

        books = self.driver.find_elements(*self.BOOKS)

        for book in books:

            title = book.find_element(*self.TITLE).get_attribute("title")

            price_text = book.find_element(*self.PRICE).text
            price = float(price_text.replace("£", ""))

            stock = book.find_element(*self.STOCK).text

            rating_class = book.find_element(*self.RATING).get_attribute("class")
            rating = rating_class.split()[1]

            books_data.append(
                Book(title, price, rating, stock)
            )

        return books_data