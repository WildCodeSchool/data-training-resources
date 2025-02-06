import os
import platform
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def valider_et_formater_heure(heure_str):
    """
    Convertit une heure (format HH:MM) en le prochain créneau valide sur 2 heures 
    (entre 4h et 22h). Si les minutes sont supérieures à 0, passe au créneau suivant.
    Retourne l'heure valide sous forme de chaîne.
    """
    try:
        # Découper l'heure en heures et minutes
        heure, minutes = map(int, heure_str.split(':'))
        # Créneaux horaires valides : 4, 6, 8, ..., 22
        heures_valides = list(range(4, 23, 2))
        # Trouver le premier créneau supérieur à l'heure saisie
        prochaine_heure = next((h for h in heures_valides if h > heure), 4)
        # Si des minutes sont indiquées, passer au créneau suivant
        if minutes > 0:
            index_prochaine = heures_valides.index(prochaine_heure)
            if index_prochaine + 1 < len(heures_valides):
                prochaine_heure = heures_valides[index_prochaine + 1]
            else:
                prochaine_heure = heures_valides[0]  # Retourner à 4h en cas de dépassement
        return str(prochaine_heure)
    except Exception:
        # En cas d'erreur, retourner 8 par défaut
        return "8"


def demander_donnees_utilisateur():
    """
    Demande à l'utilisateur les informations de voyage et retourne les données saisies.
    """
    ville_depart = input("Ville de départ : ")
    ville_arrivee = input("Ville d'arrivée : ")
    date_depart = input("Date de départ (format: DD/MM/YYYY) : ")
    date_retour = input("Date de retour (format: DD/MM/YYYY) : ")
    heure_depart = input("Heure de départ (format: HH:MM) : ")
    heure_retour = input("Heure de retour (format: HH:MM) : ")
    
    # Valider et reformater les heures saisies
    heure_depart = valider_et_formater_heure(heure_depart)
    heure_retour = valider_et_formater_heure(heure_retour)
    
    return ville_depart, ville_arrivee, date_depart, date_retour, heure_depart, heure_retour


def initialiser_navigateur():
    options = webdriver.ChromeOptions()

    # Récupérer le répertoire personnel de l'utilisateur
    repertoire_utilisateur = os.path.expanduser("~")
    
    # Déterminer le chemin du profil Chrome selon le système d'exploitation
    if platform.system() == "Windows":
        chemin_profil = os.path.join(repertoire_utilisateur, "AppData", "Local", "Google", "Chrome", "User Data")
    elif platform.system() == "Darwin":  # Mac OS
        chemin_profil = os.path.join(repertoire_utilisateur, "Library", "Application Support", "Google", "Chrome")
    else:
        # Pour Linux par exemple, vous pouvez ajouter :
        # chemin_profil = os.path.join(repertoire_utilisateur, ".config", "google-chrome")
        chemin_profil = None

    # Si un chemin a été défini, l'ajouter aux options de Chrome
    if chemin_profil:
        options.add_argument(f"--user-data-dir={chemin_profil}")
        # Vous pouvez spécifier un sous-dossier de profil (par exemple "Default") si besoin
        options.add_argument("--profile-directory=Default")

    # Désactiver la détection des automatisations par le navigateur
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Créer et retourner l'instance du navigateur
    navigateur = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return navigateur


def simuler_interaction_humaine(navigateur):
    """
    Simule des interactions humaines (déplacement de souris et défilement) pour rendre l'action moins robotique.
    """
    # Attendre quelques secondes avant d'interagir
    time.sleep(random.uniform(5, 7))
    actions = ActionChains(navigateur)
    # Déplacer la souris vers une position aléatoire
    actions.move_by_offset(random.randint(200, 400), random.randint(100, 300)).perform()
    # Faire défiler la page vers le bas
    navigateur.execute_script("window.scrollBy(0, 300);")
    time.sleep(random.uniform(2, 4))


def selectionner_ville_depart(navigateur, attente, ville_depart):
    """
    Remplit le champ de la ville de départ et sélectionne la suggestion affichée.
    """
    # Attendre que le champ soit cliquable
    champ_depart = attente.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="D\'où partons-nous ?"]'))
    )
    # Faire défiler la page pour s'assurer de la visibilité
    navigateur.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
    time.sleep(random.uniform(1, 2))
    champ_depart.click()
    time.sleep(0.5)
    # Saisir la ville de départ
    champ_depart.send_keys(ville_depart)
    # Déclencher l'événement d'input pour afficher les suggestions
    navigateur.execute_script("arguments[0].dispatchEvent(new Event('input'));", champ_depart)
    # Attendre le chargement des suggestions
    time.sleep(2)
    element_suggestions = attente.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-autocomplete="list"]'))
    )
    # Récupérer l'ID de la suggestion active
    id_actif = element_suggestions.get_attribute('aria-activedescendant')
    print("ID actif pour le départ :", id_actif)
    if id_actif:
        suggestion = attente.until(
            EC.presence_of_element_located((By.ID, id_actif))
        )
        suggestion.click()
    else:
        # Si l'attribut n'est pas défini, cliquer sur la première option disponible
        suggestion = attente.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[role="option"]'))
        )
        suggestion.click()


def selectionner_ville_arrivee(navigateur, attente, ville_arrivee):
    """
    Remplit le champ de la ville d'arrivée et sélectionne la suggestion affichée.
    """
    champ_arrivee = attente.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Où allons-nous ?"]'))
    )
    navigateur.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
    time.sleep(random.uniform(1, 2))
    champ_arrivee.click()
    time.sleep(0.5)
    # Saisir la ville d'arrivée
    champ_arrivee.send_keys(ville_arrivee)
    navigateur.execute_script("arguments[0].dispatchEvent(new Event('input'));", champ_arrivee)
    # Attendre le chargement des suggestions
    time.sleep(2)
    element_suggestions = attente.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-autocomplete="list"]'))
    )
    id_actif = element_suggestions.get_attribute('aria-activedescendant')
    print("ID actif pour l'arrivée :", id_actif)
    if id_actif:
        suggestion = attente.until(
            EC.presence_of_element_located((By.ID, id_actif))
        )
        suggestion.click()
    else:
        # Si l'attribut n'est pas défini, cliquer sur la première option disponible
        suggestion = attente.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[role="option"]'))
        )
        suggestion.click()


def ouvrir_selection_dates(navigateur, attente):
    """
    Ouvre la section de sélection des dates en cliquant sur le bouton 'Aller :'.
    """
    bouton_aller = attente.until(
        EC.element_to_be_clickable((By.XPATH, "//button[starts-with(@aria-label, 'Aller :')]"))
    )
    bouton_aller.click()


def selectionner_dates_et_heures(navigateur, attente, date_depart, heure_depart, date_retour, heure_retour):
    """
    Sélectionne les dates et heures de départ et de retour via l'interface du calendrier.
    """
    # --- Date et heure de départ ---
    champ_date_depart = attente.until(
        EC.presence_of_element_located((By.ID, "input-date-startDate"))
    )
    champ_date_depart.click()
    champ_date_depart.send_keys(Keys.CONTROL + "a")
    champ_date_depart.send_keys(Keys.DELETE)
    champ_date_depart.send_keys(date_depart)
    print("Date de départ modifiée.")
    attente.until(EC.presence_of_element_located((By.CLASS_NAME, "MuiDialog-scrollPaper")))
    print("Calendrier de départ affiché.")

    # Sélectionner l'heure de départ
    menu_heure_depart = attente.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="startDateTime"]'))
    )
    menu_heure_depart.click()
    print("Menu déroulant de l'heure de départ ouvert.")
    attente.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.MuiMenu-list')))
    
    # Identifier l'option correspondant à l'heure souhaitée
    option_heure_depart = attente.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{heure_depart}"]'))
    )
    # Faire défiler l'option dans la vue pour s'assurer qu'elle est visible
    navigateur.execute_script("arguments[0].scrollIntoView(true);", option_heure_depart)
    time.sleep(0.5)
    
    try:
        option_heure_depart.click()
    except Exception as e:
        print("Clic intercepté, tentative via JavaScript :", e)
        navigateur.execute_script("arguments[0].click();", option_heure_depart)
    print("Heure de départ sélectionnée.")

    # --- Date et heure de retour ---
    champ_date_retour = attente.until(
        EC.presence_of_element_located((By.ID, "input-date-endDate"))
    )
    champ_date_retour.click()
    champ_date_retour.send_keys(Keys.CONTROL + "a")
    champ_date_retour.send_keys(Keys.DELETE)
    champ_date_retour.send_keys(date_retour)
    time.sleep(random.uniform(1, 2))
    print("Date de retour modifiée.")
    attente.until(EC.presence_of_element_located((By.CLASS_NAME, "MuiDialog-scrollPaper")))
    print("Calendrier de retour affiché.")
    
    # Sélectionner l'heure de retour
    menu_heure_retour = attente.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="endDateTime"]'))
    )
    menu_heure_retour.click()
    print("Menu déroulant de l'heure de retour ouvert.")
    attente.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.MuiMenu-list')))
    
    option_heure_retour = attente.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{heure_retour}"]'))
    )
    navigateur.execute_script("arguments[0].scrollIntoView(true);", option_heure_retour)
    time.sleep(0.5)
    try:
        option_heure_retour.click()
    except Exception as e:
        print("Clic intercepté pour l'heure de retour, tentative via JavaScript :", e)
        navigateur.execute_script("arguments[0].click();", option_heure_retour)
    print("Heure de retour sélectionnée.")

    # Valider la sélection
    bouton_valider = attente.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButton-containedPrimary[type='submit']"))
    )
    bouton_valider.click()
    print("Dates et heures validées.")


def cliquer_voir_les_prix(navigateur, attente):
    """
    Fait défiler la page et clique sur le bouton 'Voir les prix'.
    """
    navigateur.execute_script("window.scrollTo(0, 500);")
    time.sleep(random.uniform(1, 2))
    bouton_voir_prix = attente.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Voir les prix')]"))
    )
    if bouton_voir_prix:
        bouton_voir_prix.click()
        print("Bouton 'Voir les prix' cliqué.")
    else:
        time.sleep(5)


def afficher_prix_recommande(navigateur):
    """
    Recherche et affiche le prix recommandé affiché sur la page.
    """
    time.sleep(4)
    elements_prix = navigateur.find_elements(By.CSS_SELECTOR, 'span[data-test="newPrice"]')
    if elements_prix:
        prix_recommande = elements_prix[0].text
        print(f"Prix recommandé : {prix_recommande}\n")
        print("-------------------")
    else:
        print("Aucun prix recommandé trouvé.")
        time.sleep(5)


def afficher_propositions_train(navigateur, attente):
    """
    Parcourt et affiche les propositions de train (horaires, gares et prix) disponibles.
    """
    propositions = attente.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='nav-tab-panel-TRAIN']//ul[@role='list']/li[@data-test='proposal-card']")
        )
    )
    for proposition in propositions:
        # Récupérer les horaires (départ et arrivée)
        elements_horaires = proposition.find_elements(By.CSS_SELECTOR, "span[data-test='time-label']")
        heure_dep = elements_horaires[0].text if len(elements_horaires) > 0 else ""
        heure_arr = elements_horaires[1].text if len(elements_horaires) > 1 else ""
        # Récupérer les gares (départ et arrivée)
        elements_gares = proposition.find_elements(By.CSS_SELECTOR, "span[data-test='place']")
        gare_dep = elements_gares[0].text if len(elements_gares) > 0 else ""
        gare_arr = elements_gares[1].text if len(elements_gares) > 1 else ""
        # Récupérer les prix affichés
        elements_prix = proposition.find_elements(By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h3')
        prix_1 = elements_prix[0].text if len(elements_prix) > 0 else ""
        prix_2 = elements_prix[1].text if len(elements_prix) > 1 else ""
        # Afficher les informations de la proposition
        print(f"Départ : {heure_dep} de {gare_dep}")
        print(f"Arrivée : {heure_arr} à {gare_arr}")
        print(f"1er Prix : {prix_1} / 2ème Prix : {prix_2}")
        print("-------------------")


# --- Exécution du script ---

# Récupérer les informations de voyage auprès de l'utilisateur
ville_depart, ville_arrivee, date_depart, date_retour, heure_depart, heure_retour = demander_donnees_utilisateur()

# Initialiser le navigateur
navigateur = initialiser_navigateur()

# Accéder au site SNCF Connect
navigateur.get("https://www.sncf-connect.com/app/home/search/od")

# Simuler des interactions humaines pour éviter les détections de robot
simuler_interaction_humaine(navigateur)

# Créer une instance d'attente explicite longue (20 secondes)
attente_longue = WebDriverWait(navigateur, 20)

# Utiliser l'attente longue pour toutes les étapes qui dépendent du chargement dynamique
selectionner_ville_depart(navigateur, attente_longue, ville_depart)
selectionner_ville_arrivee(navigateur, attente_longue, ville_arrivee)
ouvrir_selection_dates(navigateur, attente_longue)
selectionner_dates_et_heures(navigateur, attente_longue, date_depart, heure_depart, date_retour, heure_retour)
cliquer_voir_les_prix(navigateur, attente_longue)
afficher_prix_recommande(navigateur)
afficher_propositions_train(navigateur, attente_longue)

# Attendre quelques secondes avant de terminer pour visualiser les résultats
time.sleep(10)
# Pour fermer automatiquement le navigateur, décommentez la ligne suivante :
# navigateur.quit()
