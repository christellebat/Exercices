from selenium import webdriver
from tests2.test_tp2 import run_tests


def main():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        run_tests(driver)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()