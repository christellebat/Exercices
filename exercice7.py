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
    
    # 3. Attendre que les cartes produit se chargent
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'card')]")))
    
    # 4. Localiser les cartes produit avec XPath contains()
    cards = driver.find_elements(By.XPATH, "//*[contains(@class,'card')]")
    print(f"Nombre de cartes trouvées : {len(cards)}")
    
    # 5. Localiser les titres de produits avec XPath descendant
    titles = driver.find_elements(By.XPATH, "//div[contains(@class,'card')]//h5[contains(@class,'card-title')]")
    print(f"Nombre de titres trouvés : {len(titles)}")
    
    # 6. Variations de XPath
    # - Utiliser position() pour prendre la première carte
    first_card = driver.find_element(By.XPATH, "(//*[contains(@class,'card')])[1]")
    print(f"Première carte visible : {first_card.is_displayed()}")
    
    # - Utiliser not() pour exclure certaines classes (exemple: exclure notifications)
    non_notification_cards = driver.find_elements(By.XPATH, "//*[contains(@class,'card') and not(contains(@class,'notification'))]")
    print(f"Cartes excluant notification : {len(non_notification_cards)}")
    
    # - Utiliser descendant pour obtenir tous les titres à l’intérieur des cartes
    descendant_titles = driver.find_elements(By.XPATH, "//*[contains(@class,'card')]//descendant::*[contains(@class,'card-title')]")
    print(f"Tous les titres via descendant : {len(descendant_titles)}")
    
finally:
    # 8. Fermer le navigateur
    driver.quit()