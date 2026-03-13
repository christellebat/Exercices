from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageShop:
    # Sélecteurs
    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BUTTON = (By.ID, "search-button")
    PRODUCTS_CONTAINER = (By.CSS_SELECTOR, ".product-card")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-title")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")
    PRODUCT_RATING = (By.CSS_SELECTOR, ".fa-star")

    def __init__(self, driver):
        self.driver = driver

    # Recherche d'un produit
    def search_product(self, keyword):
        search_box = self.driver.find_element(*self.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(keyword)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        # Attendre que les résultats soient visibles
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PRODUCTS_CONTAINER)
        )

    # Extraction des produits
    def get_products(self):
        products = self.driver.find_elements(*self.PRODUCTS_CONTAINER)
        products_list = []

        for product in products:
            # Nom
            try:
                name = product.find_element(*self.PRODUCT_NAME).text
            except:
                name = "Unknown"

            # Prix
            try:
                price_text = product.find_element(*self.PRODUCT_PRICE).text
                price = float(price_text.replace("$", "").strip())
            except:
                price = 0.0

            # Note (nombre d'étoiles)
            try:
                stars = product.find_elements(*self.PRODUCT_RATING)
                rating = len(stars)
            except:
                rating = 0

            products_list.append({
                "name": name,
                "price": price,
                "rating": rating
            })

        return products_list