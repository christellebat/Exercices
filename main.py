import logging
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.test_tp1 import run_all_tests


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler("logs/test.log")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(2)
    return driver


def main():
    setup_logger()
    logging.info("Démarrage des tests Selenium")

    driver = None

    try:
        logging.info("Lancement du navigateur")
        driver = create_driver()

        run_all_tests(driver)

        logging.info("Tous les tests sont terminés")

    finally:
        if driver:
            logging.info("Fermeture du navigateur")
            driver.quit()


if __name__ == "__main__":
    main()