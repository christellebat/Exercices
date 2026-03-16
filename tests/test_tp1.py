import logging
from datetime import datetime

from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from pages.dropdown_page import DropdownPage
from pages.add_remove_page import AddRemovePage


USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


def run_all_tests(driver):

    login_page = LoginPage(driver)
    secure_page = SecureAreaPage(driver)
    dropdown_page = DropdownPage(driver)
    add_remove_page = AddRemovePage(driver)

    try:

        logging.info("===== PARTIE 1 — AUTHENTIFICATION =====")

        logging.info("1. Ouverture de la page login")
        login_page.open_page()

        logging.info("2. Vérification de la page d'authentification")
        assert login_page.is_login_page_displayed(), "La page Login n'est pas affichée correctement."
        logging.info("Page login détectée")

        logging.info("3. Saisie des identifiants")
        logging.info("4. Clic sur le bouton de connexion")

        login_page.login(USERNAME, PASSWORD)

        logging.info(f"URL après login : {driver.current_url}")

        logging.info("5. Vérification que la connexion a réussi")
        assert secure_page.is_secure_area_displayed(), "La zone sécurisée n'est pas affichée."
        logging.info("Connexion réussie")

        logging.info("6. Vérification du message de succès")
        flash_message = secure_page.get_flash_message()

        logging.info(f"Message affiché : {flash_message}")

        assert "You logged into a secure area!" in flash_message
        logging.info("Message de succès validé")

        logging.info("7. Vérification de la présence du bouton logout")
        assert secure_page.is_logout_visible(), "Le bouton Logout est absent."
        logging.info("Bouton logout visible")

        logging.info("8. Clic sur logout")
        secure_page.logout()

        logging.info("9. Vérification du retour vers la page login")
        assert login_page.is_login_page_displayed(), "Retour à la page login échoué."
        logging.info("Logout validé")



        logging.info("===== PARTIE 2 — LISTE DÉROULANTE =====")

        logging.info("1. Ouverture de la page Dropdown")
        dropdown_page.open_page()

        logging.info("2. Vérification de la présence de la liste déroulante")
        assert dropdown_page.is_dropdown_page_displayed(), "La page Dropdown n'est pas correcte."
        assert dropdown_page.is_dropdown_present(), "La liste déroulante est absente."

        logging.info("Liste déroulante détectée")

        logging.info("3. Sélection de Option 1")
        dropdown_page.select_option_by_text("Option 1")

        logging.info("4. Vérification de la sélection de Option 1")

        selected = dropdown_page.get_selected_option()
        logging.info(f"Option sélectionnée : {selected}")

        assert selected == "Option 1", "Option 1 n'est pas sélectionnée."
        logging.info("Option 1 bien sélectionnée")

        logging.info("5. Sélection de Option 2")
        dropdown_page.select_option_by_text("Option 2")

        logging.info("6. Vérification de la sélection de Option 2")

        selected = dropdown_page.get_selected_option()
        logging.info(f"Option sélectionnée : {selected}")

        assert selected == "Option 2", "Option 2 n'est pas sélectionnée."
        logging.info("Option 2 bien sélectionnée")



        logging.info("===== PARTIE 3 — AJOUT / SUPPRESSION D'ÉLÉMENTS =====")

        logging.info("1. Ouverture de la page Add/Remove Elements")
        add_remove_page.open_page()

        logging.info("2. Vérification de la page")
        assert add_remove_page.is_page_displayed(), "La page Add/Remove Elements n'est pas affichée."
        logging.info("Page Add/Remove Elements détectée")

        logging.info("3. Clic 3 fois sur Add Element")
        add_remove_page.click_add_element(times=3)

        logging.info("4. Vérification de la présence de 3 boutons Delete")

        delete_count = add_remove_page.count_delete_buttons()
        logging.info(f"Nombre de boutons Delete trouvés : {delete_count}")

        assert delete_count == 3, "Le nombre de boutons Delete n'est pas égal à 3."
        logging.info("3 boutons Delete affichés")

        logging.info("5. Suppression de 1 élément")
        add_remove_page.delete_one_element()

        logging.info("6. Vérification qu'il reste 2 boutons Delete")

        delete_count = add_remove_page.count_delete_buttons()
        logging.info(f"Nombre de boutons Delete restants : {delete_count}")

        assert delete_count == 2, "Le nombre de boutons Delete restants n'est pas égal à 2."
        logging.info("Il reste 2 boutons Delete")

        logging.info("7. Suppression de tous les éléments restants")
        add_remove_page.delete_all_elements()

        logging.info("8. Vérification qu'il ne reste aucun bouton Delete")

        delete_count = add_remove_page.count_delete_buttons()
        logging.info(f"Nombre final de boutons Delete : {delete_count}")

        assert delete_count == 0, "Il reste encore des boutons Delete."
        logging.info("Tous les éléments ont été supprimés")



        logging.info("===== RÉSULTAT FINAL =====")
        logging.info("Tous les scénarios ont été exécutés avec succès")



    except AssertionError as e:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"assertion_error_{timestamp}.png"

        try:
            login_page.save_screenshot(filename)
        except Exception:
            pass

        logging.error(f"Erreur assertion : {e}")
        raise


    except Exception as e:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"unexpected_error_{timestamp}.png"

        try:
            login_page.save_screenshot(filename)
        except Exception:
            pass

        logging.error(f"Erreur inattendue : {e}")
        raise
