from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from books_scraper import BooksScraper
import statistics_books


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

scraper = BooksScraper(driver)

print("Chargement du site...")

scraper.load()

# récupérer les catégories
categories = scraper.get_categories()

print("\nCatégories disponibles :")

for i, cat in enumerate(categories.keys()):
    print(f"{i+1}. {cat}")

# choix utilisateur
choice = int(input("\nChoisir une catégorie (numéro): "))

selected_category = list(categories.keys())[choice - 1]
category_url = categories[selected_category]

print(f"\nCatégorie choisie : {selected_category}")

# ouvrir catégorie
scraper.open_category(category_url)

scraper.wait_books()

books = scraper.extract_books()

print(f"\n{len(books)} livres trouvés dans cette catégorie")

print("\n5 premiers livres :")

for b in books[:5]:
    print(b)

# statistiques
stats = statistics_books.global_stats(books)

print("\nStatistiques :")

print("Nombre total :", stats["total_books"])

print("Prix moyen :", stats["price_stats"]["average"])
print("Prix min :", stats["price_stats"]["min"])
print("Prix max :", stats["price_stats"]["max"])

driver.quit()