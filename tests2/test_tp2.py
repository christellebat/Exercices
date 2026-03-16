from pages2.dynamic_controls_page import DynamicControlsPage
from pages2.dynamic_loading_page import DynamicLoadingPage


def run_tests(driver):

    dynamic_controls = DynamicControlsPage(driver)
    dynamic_loading = DynamicLoadingPage(driver)

    print("===== PARTIE 1 : Dynamic Controls =====")

    dynamic_controls.open_page()

    assert dynamic_controls.is_page_loaded()

    print("Checkbox présente")
    assert dynamic_controls.is_checkbox_present()

    print("Suppression de la checkbox")
    dynamic_controls.click_remove()
    dynamic_controls.wait_checkbox_disappear()

    message = dynamic_controls.get_message()
    print("Message :", message)
    assert "gone" in message

    print("Ajout de la checkbox")
    dynamic_controls.click_add()
    dynamic_controls.wait_checkbox_appear()

    message = dynamic_controls.get_message()
    print("Message :", message)
    assert "back" in message

    print("Vérification champ désactivé")
    assert dynamic_controls.is_input_disabled()

    print("Activation du champ")
    dynamic_controls.click_enable()
    dynamic_controls.wait_input_enabled()

    dynamic_controls.write_input("test selenium")

    value = dynamic_controls.get_input_value()
    assert value == "test selenium"

    print("PARTIE 1 OK")

    print("===== PARTIE 2 : Dynamic Loading =====")

    dynamic_loading.open_page()

    dynamic_loading.open_example2()

    print("Bouton start")
    dynamic_loading.click_start()

    dynamic_loading.wait_hello_world()

    text = dynamic_loading.get_hello_text()
    print("Texte affiché :", text)

    assert "Hello World!" in text

    print("PARTIE 2 OK")