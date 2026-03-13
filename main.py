from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from book_page import BooksPage


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

print("============================================================")
print("TP : EXTRACTION DE DONNÉES DE LIVRES")
print("============================================================")

print("\n--- Phase 1: Navigation ---")

page = BooksPage(driver)

page.load()

print("Accédé à books.toscrape.com")

page.wait_books()

print("Livres chargés")

print("\n--- Phase 2: Extraction des Données ---")

books = page.extract_books()

print(f"{len(books)} livres extraits avec succès")

for i, book in enumerate(books):
    print(f"Livre {i+1}: {book}")

print("\n--- Phase 3: Rapport et Statistiques ---")

print(f"\nNombre total de livres: {len(books)}")

print("\n5 Premiers Livres:")

for i in range(5):
    b = books[i]

    print(f"  {i+1}. {b.title}")
    print(f"     Prix: £{b.price} | Rating: {b.rating} | {b.stock}")

prices = [b.price for b in books]

print("\nStatistiques de Prix:")

print(f"  Prix moyen: £{round(sum(prices)/len(prices),2)}")
print(f"  Prix minimum: £{min(prices)}")
print(f"  Prix maximum: £{max(prices)}")

ratings = {}

for b in books:
    ratings[b.rating] = ratings.get(b.rating, 0) + 1

print("\nDistribution par Note:")

for rating, count in ratings.items():
    print(f"  {rating} étoiles: {count} livres")

print("\nTP RÉUSSI!")

driver.quit()