from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Ouvrir le navigateur
driver = webdriver.Chrome()

try:
    # 2. Accéder au site
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    wait = WebDriverWait(driver, 10)

    # 3. Cliquer sur le bouton Start
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 4. Attendre que "Hello World!" apparaisse
    hello = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    texte = hello.text

    # 5. Vérifier que le texte contient "Hello World!"
    print("Contient Hello World :", "Hello World!" in texte)

    # 6. Vérifier que le texte ne contient pas "It's gone!"
    print("Ne contient pas It's gone! :", "It's gone!" not in texte)

    print("Texte trouvé :", texte)

finally:
    # 7. Fermer le navigateur
    driver.quit()