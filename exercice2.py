from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Ouvrir le navigateur
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Accéder au site
    driver.get("https://example.com")

    # Trouver le premier lien avec TAG_NAME
    link = driver.find_element(By.TAG_NAME, "a")

    # Vérifier que c'est bien un lien
    assert link.tag_name == "a", f"Ce n'est pas un lien : {link.tag_name}"

    # Récupérer l'attribut href
    href = link.get_attribute("href")

    # Vérifier que le lien n'est pas vide
    assert href is not None and href != "", "Le href est vide"

    # Afficher l'URL
    print("Lien trouvé :", href)

    # Pause pour voir la page
    input("Appuie sur Entrée pour fermer...")

except AssertionError as e:
    print("Erreur de validation :", e)

except Exception as e:
    print("Erreur :", e)

finally:
    # Fermer le navigateur
    driver.quit()
    print("Navigateur fermé")