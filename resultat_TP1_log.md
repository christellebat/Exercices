(.venv) PS C:\Users\chris\Desktop\Exercices> python main.py
2026-03-16 15:26:15,162 | INFO | Démarrage des tests Selenium
2026-03-16 15:26:15,163 | INFO | Lancement du navigateur
2026-03-16 15:26:15,172 | INFO | ====== WebDriver manager ======
2026-03-16 15:26:16,819 | INFO | Get LATEST chromedriver version for google-chrome
2026-03-16 15:26:17,290 | INFO | Get LATEST chromedriver version for google-chrome
2026-03-16 15:26:17,673 | INFO | Driver [C:\Users\chris\.wdm\drivers\chromedriver\win64\145.0.7632.117\chromedriver-win32/chromedriver.exe] found in cache
2026-03-16 15:26:20,110 | INFO | ===== PARTIE 1 — AUTHENTIFICATION =====
2026-03-16 15:26:20,111 | INFO | 1. Ouverture de la page login
2026-03-16 15:26:21,457 | INFO | 2. Vérification de la page d'authentification
2026-03-16 15:26:21,488 | INFO | Page login détectée
2026-03-16 15:26:21,488 | INFO | 3. Saisie des identifiants
2026-03-16 15:26:21,488 | INFO | 4. Clic sur le bouton de connexion
2026-03-16 15:26:22,066 | INFO | URL après login : https://the-internet.herokuapp.com/secure
2026-03-16 15:26:22,066 | INFO | 5. Vérification que la connexion a réussi
2026-03-16 15:26:22,093 | INFO | Connexion réussie
2026-03-16 15:26:22,093 | INFO | 6. Vérification du message de succès
2026-03-16 15:26:22,112 | INFO | Message affiché : You logged into a secure area!
×
2026-03-16 15:26:22,113 | INFO | Message de succès validé
2026-03-16 15:26:22,113 | INFO | 7. Vérification de la présence du bouton logout
2026-03-16 15:26:22,129 | INFO | Bouton logout visible
2026-03-16 15:26:22,130 | INFO | 8. Clic sur logout
2026-03-16 15:26:22,447 | INFO | 9. Vérification du retour vers la page login
2026-03-16 15:26:22,465 | INFO | Logout validé
2026-03-16 15:26:22,465 | INFO | ===== PARTIE 2 — LISTE DÉROULANTE =====
2026-03-16 15:26:22,465 | INFO | 1. Ouverture de la page Dropdown
2026-03-16 15:26:22,607 | INFO | 2. Vérification de la présence de la liste déroulante
2026-03-16 15:26:22,643 | INFO | Liste déroulante détectée
2026-03-16 15:26:22,644 | INFO | 3. Sélection de Option 1
2026-03-16 15:26:22,735 | INFO | 4. Vérification de la sélection de Option 1
2026-03-16 15:26:22,780 | INFO | Option sélectionnée : Option 1
2026-03-16 15:26:22,781 | INFO | Option 1 bien sélectionnée
2026-03-16 15:26:22,781 | INFO | 5. Sélection de Option 2
2026-03-16 15:26:22,861 | INFO | 6. Vérification de la sélection de Option 2
2026-03-16 15:26:22,910 | INFO | Option sélectionnée : Option 2
2026-03-16 15:26:22,910 | INFO | Option 2 bien sélectionnée
2026-03-16 15:26:22,910 | INFO | ===== PARTIE 3 — AJOUT / SUPPRESSION D'ÉLÉMENTS =====
2026-03-16 15:26:22,911 | INFO | 1. Ouverture de la page Add/Remove Elements
2026-03-16 15:26:23,046 | INFO | 2. Vérification de la page
2026-03-16 15:26:23,062 | INFO | Page Add/Remove Elements détectée
2026-03-16 15:26:23,063 | INFO | 3. Clic 3 fois sur Add Element
2026-03-16 15:26:23,281 | INFO | 4. Vérification de la présence de 3 boutons Delete
2026-03-16 15:26:23,292 | INFO | Nombre de boutons Delete trouvés : 3
2026-03-16 15:26:23,292 | INFO | 3 boutons Delete affichés
2026-03-16 15:26:23,293 | INFO | 5. Suppression de 1 élément
2026-03-16 15:26:23,361 | INFO | 6. Vérification qu'il reste 2 boutons Delete
2026-03-16 15:26:23,367 | INFO | Nombre de boutons Delete restants : 2
2026-03-16 15:26:23,368 | INFO | Il reste 2 boutons Delete
2026-03-16 15:26:23,369 | INFO | 7. Suppression de tous les éléments restants
2026-03-16 15:26:27,524 | INFO | 8. Vérification qu'il ne reste aucun bouton Delete
2026-03-16 15:26:29,585 | INFO | Nombre final de boutons Delete : 0
2026-03-16 15:26:29,586 | INFO | Tous les éléments ont été supprimés
2026-03-16 15:26:29,586 | INFO | ===== RÉSULTAT FINAL =====
2026-03-16 15:26:29,586 | INFO | Tous les scénarios ont été exécutés avec succès
2026-03-16 15:26:29,586 | INFO | Tous les tests sont terminés
2026-03-16 15:26:29,587 | INFO | Fermeture du navigateur
(.venv) PS C:\Users\chris\Desktop\Exercices> 