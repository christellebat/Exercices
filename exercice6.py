from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuration du navigateur
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Accéder au site
    driver.get("https://practicesoftwaretesting.com/")
    
    # Attendre que les cartes se chargent
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".card")))
    
    # Récupérer les cartes et les titres
    cards = driver.find_elements(By.CSS_SELECTOR, ".card")
    titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
    
    print(f"Nombre total de cartes produit : {len(cards)}\n")
    
    # Vérifier visibilité et afficher les titres
    for i, (card, title) in enumerate(zip(cards, titles), start=1):
        card_visible = card.is_displayed()
        title_visible = title.is_displayed()
        print(f"Carte #{i}: '{title.text}' | Carte visible: {card_visible}, Titre visible: {title_visible}")
    
    # Vérification globale
    all_visible = all(card.is_displayed() for card in cards) and all(title.is_displayed() for title in titles)
    print(f"\nTous les éléments sont visibles : {all_visible}")

finally:
    driver.quit()