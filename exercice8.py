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
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
    wait = WebDriverWait(driver, 10)

    # 3. Cliquer sur "Click for JS Alert"
    js_alert_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
    js_alert_button.click()

    # 4. Accepter l'alerte
    alert = driver.switch_to.alert
    print(f"Message de l'alerte : {alert.text}")
    alert.accept()

    # 5. Vérifier le message affiché après l'acceptation
    result_text = driver.find_element(By.ID, "result").text
    print(f"Résultat après acceptation : {result_text}")

    # 6. Cliquer sur "Click for JS Confirm"
    js_confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    js_confirm_button.click()

    # 7. Refuser l'alerte
    confirm_alert = driver.switch_to.alert
    print(f"Message du confirm : {confirm_alert.text}")
    confirm_alert.dismiss()

    # 8. Vérifier le message après refus
    result_text_confirm = driver.find_element(By.ID, "result").text
    print(f"Résultat après refus : {result_text_confirm}")

finally:
    # 9. Fermer le navigateur
    time.sleep(2)  # Pause pour visualiser avant fermeture
    driver.quit()