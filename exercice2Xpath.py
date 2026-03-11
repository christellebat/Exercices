from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://example.com")

    # trouver le lien avec XPath
    link = driver.find_element(By.XPATH, "//a")

    assert link.tag_name == "a", "Ce n'est pas un lien"

    href = link.get_attribute("href")
    assert href, "Oups,Le href est vide"

    print("Lien trouvé :", href)

    input("Entrée pour fermer...")

finally:
    driver.quit()