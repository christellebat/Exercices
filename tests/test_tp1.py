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
        print("\n===== PARTIE 1 — AUTHENTIFICATION =====")
        print("1. Ouverture de la page login...")
        login_page.open_page()

        print("2. Vérification de la page d'authentification...")
        assert login_page.is_login_page_displayed(), "La page Login n'est pas affichée correctement."
        print("[OK] Page login détectée.")

        print("3. Saisie des identifiants...")
        print("4. Clic sur le bouton de connexion...")
        login_page.login(USERNAME, PASSWORD)

        print("5. Vérification que la connexion a réussi...")
        assert secure_page.is_secure_area_displayed(), "La zone sécurisée n'est pas affichée."
        print("[OK] Connexion réussie.")

        print("6. Vérification du message de succès...")
        flash_message = secure_page.get_flash_message()
        assert "You logged into a secure area!" in flash_message, "Message de succès introuvable."
        print("[OK] Message de succès validé.")

        print("7. Vérification de la présence du bouton logout...")
        assert secure_page.is_logout_visible(), "Le bouton Logout est absent."
        print("[OK] Bouton logout visible.")

        print("8. Clic sur logout...")
        secure_page.logout()

        print("9. Vérification du retour vers la page login...")
        assert login_page.is_login_page_displayed(), "Retour à la page login échoué."
        print("[OK] Logout validé.")

        print("\n===== PARTIE 2 — LISTE DÉROULANTE =====")
        print("1. Ouverture de la page Dropdown...")
        dropdown_page.open_page()

        print("2. Vérification de la présence de la liste déroulante...")
        assert dropdown_page.is_dropdown_page_displayed(), "La page Dropdown n'est pas correcte."
        assert dropdown_page.is_dropdown_present(), "La liste déroulante est absente."
        print("[OK] Liste déroulante présente.")

        print("3. Sélection de Option 1...")
        dropdown_page.select_option_by_text("Option 1")

        print("4. Vérification de la sélection de Option 1...")
        assert dropdown_page.get_selected_option() == "Option 1", "Option 1 n'est pas sélectionnée."
        print("[OK] Option 1 bien sélectionnée.")

        print("5. Sélection de Option 2...")
        dropdown_page.select_option_by_text("Option 2")

        print("6. Vérification de la sélection de Option 2...")
        assert dropdown_page.get_selected_option() == "Option 2", "Option 2 n'est pas sélectionnée."
        print("[OK] Option 2 bien sélectionnée.")

        print("\n===== PARTIE 3 — AJOUT / SUPPRESSION D'ÉLÉMENTS =====")
        print("1. Ouverture de la page Add/Remove Elements...")
        add_remove_page.open_page()

        print("2. Vérification de la page...")
        assert add_remove_page.is_page_displayed(), "La page Add/Remove Elements n'est pas affichée."
        print("[OK] Page Add/Remove Elements détectée.")

        print("3. Clic 3 fois sur Add Element...")
        add_remove_page.click_add_element(times=3)

        print("4. Vérification de la présence de 3 boutons Delete...")
        assert add_remove_page.count_delete_buttons() == 3, "Le nombre de boutons Delete n'est pas égal à 3."
        print("[OK] 3 boutons Delete affichés.")

        print("5. Suppression de 1 élément...")
        add_remove_page.delete_one_element()

        print("6. Vérification qu'il reste 2 boutons Delete...")
        assert add_remove_page.count_delete_buttons() == 2, "Le nombre de boutons Delete restants n'est pas égal à 2."
        print("[OK] Il reste 2 boutons Delete.")

        print("7. Suppression de tous les éléments restants...")
        add_remove_page.delete_all_elements()

        print("8. Vérification qu'il ne reste aucun bouton Delete...")
        assert add_remove_page.count_delete_buttons() == 0, "Il reste encore des boutons Delete."
        print("[OK] Tous les éléments ont été supprimés.")

        print("\n===== RÉSULTAT FINAL =====")
        print("Tous les scénarios ont été exécutés avec succès.")

    except AssertionError as e:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"assertion_error_{timestamp}.png"
        try:
            login_page.save_screenshot(filename)
        except Exception:
            pass
        print(f"[ERREUR ASSERTION] {e}")
        raise

    except Exception as e:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"unexpected_error_{timestamp}.png"
        try:
            login_page.save_screenshot(filename)
        except Exception:
            pass
        print(f"[ERREUR INATTENDUE] {e}")
        raise