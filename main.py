from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.test_tp1 import run_all_tests


def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordCheck,SafeBrowsingEnhancedProtection")

    # Désactive les infobars et popups liés au gestionnaire de mots de passe
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)

    # optionnel si tu veux lancer sans interface
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(2)
    return driver


def main():
    driver = None
    try:
        print("Démarrage du navigateur...")
        driver = create_driver()
        run_all_tests(driver)
    finally:
        if driver:
            print("Fermeture du navigateur...")
            driver.quit()


if __name__ == "__main__":
    main()