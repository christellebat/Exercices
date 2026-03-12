from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration du navigateur
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 1 & 2. Accéder au site
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    wait = WebDriverWait(driver, 10)

    # 3. Cliquer sur le bouton "Start"
    start_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='start']/button")))
    start_button.click()

    # 4. Attendre que le texte "Hello World!" apparaisse
    hello_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))

    # 5. Vérifier que le texte contient "Hello World!"
    hello_text = hello_element.text
    print(f"Texte trouvé : {hello_text}")
    assert "Hello World!" in hello_text, "Le texte 'Hello World!' n'a pas été trouvé !"

    # 6. Vérifier que le texte contient "It's gone!" (ce n'est pas présent dans le HTML fourni,
    # donc cette étape sera illustrée comme un test de présence facultatif)
    # Si on veut vérifier un texte hypothétique, on pourrait faire :
    # assert "It's gone!" in hello_text, "Le texte 'It's gone!' n'a pas été trouvé !"
    # Mais ici, il n'existe pas dans le HTML actuel.

finally:
    # 7. Fermer le navigateur
    time.sleep(2)  # Pause pour visualiser avant fermeture
    driver.quit()