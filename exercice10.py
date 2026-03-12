from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 1 & 2
driver.get("https://practicesoftwaretesting.com/")

wait = WebDriverWait(driver, 10)

# 3 attendre les titres produits
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card-title")))

# 4 récupérer titres et descriptions
titres = driver.find_elements(By.CSS_SELECTOR, ".card-title")
descriptions = driver.find_elements(By.CSS_SELECTOR, ".card-text")

produits = []

# 5 créer la liste Python
for i in range(len(titres)):
    
    nom = titres[i].text
    
    if i < len(descriptions):
        description = descriptions[i].text
    else:
        description = "Pas de description disponible sur la page d accueil"

    produits.append({
        "nom": nom,
        "description": description
    })

# 6 nombre de produits
print("Nombre de produits :", len(produits))

# 7 afficher 5 premiers
print("\n--- 5 premiers produits ---")
for p in produits[:5]:
    print(p)

# 8 afficher tout
print("\n--- Tous les produits ---")
for p in produits:
    print(p)

# 9 fermer navigateur
driver.quit()