from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://practicesoftwaretesting.com")

time.sleep(3)

produits = []

cards = driver.find_elements(By.CSS_SELECTOR, ".card")

for i in range(len(cards)):

    cards = driver.find_elements(By.CSS_SELECTOR, ".card")

    card = cards[i]

    nom = card.find_element(By.CSS_SELECTOR, ".card-title").text

    prix = card.find_element(By.CSS_SELECTOR, ".text-muted").text

    lien = card.get_attribute("href")

    driver.get(lien)

    time.sleep(2)

    description = driver.find_element(
        By.CSS_SELECTOR,
        '[data-test="product-description"]'
    ).text

    produits.append({
        "nom": nom,
        "prix": prix,
        "description": description
    })

    driver.back()

    time.sleep(2)

print("5 premiers produits :")

for p in produits[:5]:
    print(p)

print("\nListe complète :")

for p in produits:
    print(p)

driver.quit()