from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from home_page import HomePage
import product_stats


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

page = HomePage(driver)

print("Ouverture du site...")

page.open()

page.wait_products()

# récupérer catégories
categories = page.get_categories()

print("\nCatégories disponibles :")

for i, (name, _) in enumerate(categories):
    print(f"{i+1}. {name}")

# choix utilisateur
choice = int(input("\nChoisir une catégorie : ")) - 1

selected_category = categories[choice]

print("\nCatégorie choisie :", selected_category[0])

page.select_category(selected_category[1])

page.wait_products()

products = page.get_products()

print("\nProduits trouvés :", len(products))

print("\n5 premiers produits :")

for p in products[:5]:
    print("-", p)

# statistiques
print("\nStatistiques")

print("Total :", product_stats.total_products(products))

print("Nom le plus long :", product_stats.longest_name(products))

print("Nom le plus court :", product_stats.shortest_name(products))

print("Longueur moyenne :", product_stats.average_name_length(products))

driver.quit()