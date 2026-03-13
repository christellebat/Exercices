from selenium import webdriver
from page_shop import PageShop
from utils import print_summary

# 1️⃣ Lancer le navigateur
driver = webdriver.Chrome()
driver.get("https://example.com")  # Remplace par l'URL du site

# 2️⃣ Créer l'objet page
page = PageShop(driver)

# 3️⃣ Rechercher le produit
keyword = "hammer"
print(f"Recherche du produit : {keyword}")
page.search_product(keyword)

# 4️⃣ Extraire les produits
products = page.get_products()

# 5️⃣ Afficher le reporting
print_summary(products)

# 6️⃣ Fermer le navigateur
driver.quit()