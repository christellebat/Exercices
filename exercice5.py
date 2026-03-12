from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # 1. ouvrir la page
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # 2. localiser les checkboxes
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    checkbox1 = checkboxes[0]
    checkbox2 = checkboxes[1]

    # 3. vérifier état initial
    print("Checkbox 1 initial :", checkbox1.is_selected())
    print("Checkbox 2 initial :", checkbox2.is_selected())

    # 4. cocher la première si nécessaire
    if not checkbox1.is_selected():
        checkbox1.click()

    # 5. vérifier
    assert checkbox1.is_selected()
    print("Checkbox 1 cochée")

    # 6. décocher la deuxième si nécessaire
    if checkbox2.is_selected():
        checkbox2.click()

    # 7. vérifier
    assert not checkbox2.is_selected()
    print("Checkbox 2 décochée")

finally:
    time.sleep(2)
    driver.quit()