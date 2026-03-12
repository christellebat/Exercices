from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuration du navigateur
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 1 & 2. Accéder au site
    driver.get("https://practicesoftwaretesting.com/")
    
    # 3. Attendre que les cartes se chargent
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card")))
    
    # 4. Localiser les cartes produit avec le sélecteur CSS
    cards = driver.find_elements(By.CSS_SELECTOR, ".card")
    print(f"Nombre de cartes trouvées : {len(cards)}")
    
    # 5. Localiser les titres de produits avec le sélecteur CSS
    titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
    print(f"Nombre de titres trouvés : {len(titles)}")
    
    # 6. Vérifier que tous les éléments sont visibles
    all_cards_visible = all(card.is_displayed() for card in cards)
    all_titles_visible = all(title.is_displayed() for title in titles)
    print(f"Toutes les cartes visibles : {all_cards_visible}")
    print(f"Tous les titres visibles : {all_titles_visible}")
    
finally:
    # 8. Fermer le navigateur
    driver.quit()