from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

try:
    # 1. ouvrir la page
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # 2. localiser le dropdown
    dropdown_element = driver.find_element(By.ID, "dropdown")

    # 3. transformer en objet Select
    dropdown = Select(dropdown_element)

    # 4. sélectionner Option 1
    dropdown.select_by_visible_text("Option 1")
    time.sleep(2)

    # 5. vérifier que Option 1 est sélectionné
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Option 1"
    print("Option 1 sélectionnée")

    # 6. changer pour Option 2
    dropdown.select_by_visible_text("Option 2")
    time.sleep(2)

    # 7. vérifier Option 2
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Option 2"
    print("Option 2 sélectionnée")

finally:
    # 8. fermer navigateur
    time.sleep(2)
    driver.quit()