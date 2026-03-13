from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from books_scraper import BooksScraper
import statistics_books


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

scraper = BooksScraper(driver)

print("Chargement du site...")

scraper.load()
scraper.wait_books()

books = scraper.extract_books()

print(f"{len(books)} livres récupérés")

print("\n5 premiers livres :")

for b in books[:5]:
    print(b)

print("\nStatistiques :")

stats = statistics_books.global_stats(books)

print("Nombre total :", stats["total_books"])

print("Prix moyen :", stats["price_stats"]["average"])
print("Prix min :", stats["price_stats"]["min"])
print("Prix max :", stats["price_stats"]["max"])

print("\nRépartition des notes :")

for rating, count in stats["ratings"].items():
    print(rating, ":", count)

driver.quit()