from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://demoqa.com/text-box")

    driver.find_element(By.ID, "userName").send_keys("John Doe")
    driver.find_element(By.ID, "userEmail").send_keys("john@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street")

    submit = driver.find_element(By.ID, "submit")

    # scroll vers le bouton
    driver.execute_script("arguments[0].scrollIntoView();", submit)

    # clic JS
    driver.execute_script("arguments[0].click();", submit)

    output = driver.find_element(By.ID, "output")

    assert "John Doe" in output.text
    assert "john@example.com" in output.text

    print("Test réussi")

    input("Entrée pour fermer...")

finally:
    driver.quit()