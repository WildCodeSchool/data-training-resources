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

import time
import random

# Récupération des données des villes de départ et d'arrivée

ville_depart = input("Ville de départ: ")
ville_arrivee = input("Ville d'arrivée: ")
date_depart = input("Date de départ (format: DD/MM/YYYY): ")
date_retour = input("Date de retour (format: DD/MM/YYYY): ")
heure_depart = input("Heure de départ (format: HH:MM): ")
heure_retour = input("Heure de retour (format: HH:MM): ")

def validate_and_format_time(time_str):
    """Convert HH:MM to the next valid 2-hour interval between 4h and 22h"""
    try:
        # Split time into hours and minutes
        hour, minutes = map(int, time_str.split(':'))
        
        # Valid hours are 4, 6, 8, 10, 12, 14, 16, 18, 20, 22
        valid_hours = list(range(4, 23, 2))
        
        # Find the next valid hour
        next_hour = next((h for h in valid_hours if h > hour), 4)  # If no next hour found, wrap to 4
        
        # If we have minutes > 0, get the next 2-hour slot
        if minutes > 0:
            next_hour_index = valid_hours.index(next_hour)
            if next_hour_index + 1 < len(valid_hours):
                next_hour = valid_hours[next_hour_index + 1]
            else:
                next_hour = valid_hours[0]  # Wrap around to 4 if we're at the end
                
        return str(next_hour)
    except:
        return "8"  # Default to 8 if there's any error

heure_depart = validate_and_format_time(heure_depart)
heure_retour = validate_and_format_time(heure_retour)

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

# Ouvrir le site SNCF
navigateur.get("https://www.sncf-connect.com/app/home/search/od")

# Attendre le chargement de la page
time.sleep(random.uniform(5, 7))

# Simuler des interactions humaines
actions = ActionChains(navigateur)
actions.move_by_offset(random.randint(200, 400), random.randint(100, 300)).perform()
navigateur.execute_script("window.scrollBy(0, 300);")
time.sleep(random.uniform(2, 4))

# Créer un objet d'attente explicite
attente = WebDriverWait(navigateur, 20)
attente1 = WebDriverWait(navigateur, 1)

# Gérer la ville de départ
# Try multiple possible selectors for the departure field
    # Wait for the page to be fully loaded
time.sleep(random.uniform(2, 3))

def press_ville_depart(ville_depart):

    champ_depart = attente1.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="D\'où partons-nous ?"]')))
    navigateur.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
    time.sleep(random.uniform(1, 2))
    champ_depart.click()
    time.sleep(0.5)
    champ_depart.send_keys(ville_depart)

    navigateur.execute_script("arguments[0].dispatchEvent(new Event('input'));", champ_depart)

    # Attendre le chargement des suggestions
    time.sleep(2)
    liste_suggestions_depart = attente1.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-autocomplete="list"]')))
    print(liste_suggestions_depart)
    # Obtenir la valeur de l'attribut aria-activedescendant
    id_actif_depart = liste_suggestions_depart.get_attribute('aria-activedescendant')
    print("ID actif départ:", id_actif_depart)

    premiere_suggestion = attente1.until(
        EC.presence_of_element_located((By.ID, id_actif_depart))
    )
    premiere_suggestion.click()

def press_ville_retour(ville_retour):

    champ_depart = attente1.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Où allons-nous ?"]')))
    navigateur.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
    time.sleep(random.uniform(1, 2))
    champ_depart.click()
    time.sleep(0.5)
    champ_depart.send_keys(ville_retour)

    navigateur.execute_script("arguments[0].dispatchEvent(new Event('input'));", champ_depart)

    # Attendre le chargement des suggestions
    time.sleep(2)
    liste_suggestions_arrivee = attente1.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-autocomplete="list"]')))
    print(liste_suggestions_arrivee)
    # Obtenir la valeur de l'attribut aria-activedescendant
    id_actif_arrivee = liste_suggestions_arrivee.get_attribute('aria-activedescendant')
    print("ID actif arrivée:", id_actif_arrivee)

    if id_actif_arrivee:
        # Cliquer sur la première suggestion d'arrivée
        premiere_suggestion_arrivee = attente1.until(EC.presence_of_element_located((By.ID, id_actif_arrivee)))
        premiere_suggestion_arrivee.click()
    else:
        # Approche alternative pour l'arrivée
        premiere_suggestion_arrivee = attente1.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[role="option"]')))
        premiere_suggestion_arrivee.click()

press_ville_depart(ville_depart)
press_ville_retour(ville_arrivee)



input_date_depart = attente.until(EC.element_to_be_clickable((By.XPATH, "//button[starts-with(@aria-label, 'Aller :')]")))

input_date_depart.click()


#### Choisir la date de départ et la date de retour

def select_date_temps(navigateur, date_depart, heure_depart, date_retour, heure_retour):

    # Wait for the date input to be clickable

    date_depart_input = attente.until(EC.presence_of_element_located((By.ID, "input-date-startDate")))
            
    # Clear the field and enter the date directly
    date_depart_input.click()
    date_depart_input.send_keys(Keys.CONTROL + "a")  # Select all existing text
    date_depart_input.send_keys(Keys.DELETE)         # Delete selected text
    date_depart_input.send_keys(date_depart)                # Enter new date

    print("Date_départ changée")
    # Wait for a moment to ensure the calendar processes the input
    attente.until(EC.presence_of_element_located((By.CLASS_NAME, "MuiDialog-scrollPaper")))
    print("scroll trouvé")
    #### Pour l'heure de départ
    
    # Wait for and click the time dropdown
    time_dropdown = attente.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="startDateTime"]')))
    time_dropdown.click()
    print("dropdown ouvert")

    attente.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.MuiMenu-list')))
    print("element present en liste")
    
    # Click the specific time option
    time_option = attente.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{heure_depart}"]')))
    time_option.click()
    print("selection")

    # Date de retour
    date_retour_input = attente.until(EC.presence_of_element_located((By.ID, "input-date-endDate")))
            
    # Clear the field and enter the date directly
    date_retour_input.click()
    date_retour_input.send_keys(Keys.CONTROL + "a")  # Select all existing text
    date_retour_input.send_keys(Keys.DELETE)         # Delete selected text
    date_retour_input.send_keys(date_retour)

    time.sleep(random.uniform(1, 2))

    print("Date_retour changée")
    # Wait for a moment to ensure the calendar processes the input
    attente.until(EC.presence_of_element_located((By.CLASS_NAME, "MuiDialog-scrollPaper")))
    print("scroll trouvé")
    #### Pour l'heure de retour
    
    # Wait for and click the time dropdown
    time_dropdown = attente.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="endDateTime"]')))
    time_dropdown.click()
    print("dropdown ouvert")

    attente.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.MuiMenu-list')))
    print("element present en liste")
    
    # Click the specific time option
    time_option = attente.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{heure_retour}"]')))
    time_option.click()
    print("selection")

    # Wait for and click the validate button

    validate_button = attente.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButton-containedPrimary[type='submit']")))
    validate_button.click()
    print("validation")

# Usage
select_date_temps(navigateur, date_depart, heure_depart, date_retour, heure_retour)

# Faire défiler vers le bas pour trouver le bouton
navigateur.execute_script("window.scrollTo(0, 500);")
time.sleep(random.uniform(1, 2))

bouton_voir_prix = attente.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Voir les prix')]")))
if bouton_voir_prix:
    bouton_voir_prix.click()
else : 
    time.sleep(5)

time.sleep(4)

# Prix recommendé : chercher le div avec data-test="newPrice"
element_recommande = navigateur.find_elements(By.CSS_SELECTOR, 'span[data-test="newPrice"]')
if element_recommande:
    prix_recommande = element_recommande[0].text
    print(f"Prix recommandé: {prix_recommande}\n")
    print("-------------------")
else : 
    print("Aucun prix recommandé trouvé")
    time.sleep(5)

# Trouver tous les trajets dans la liste
propositions_train = attente.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@id='nav-tab-panel-TRAIN']//ul[@role='list']/li[@data-test='proposal-card']")
    )
)

# Parcourir chaque proposition et extraire les informations
for proposition in propositions_train:
    # Horaires : chercher les spans avec data-test="time-label"
    horaires = proposition.find_elements(By.CSS_SELECTOR, "span[data-test='time-label']")
    heure_depart = horaires[0].text  # Premier horaire = départ
    heure_arrivee = horaires[1].text # Second horaire = arrivée
    
    # Gares : chercher les spans avec data-test="place"
    gares = proposition.find_elements(By.CSS_SELECTOR, "span[data-test='place']")
    gare_depart = gares[0].text  # Première gare = départ
    gare_arrivee = gares[1].text # Seconde gare = arrivée
    
    elements_prix = proposition.find_elements(By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h3')
    premier_prix = elements_prix[0].text
    deuxieme_prix = elements_prix[1].text
    
    # Afficher les informations extraites
    print(f"Départ: {heure_depart} de {gare_depart}")
    print(f"Arrivée: {heure_arrivee} à {gare_arrivee}")
    print(f"1er Prix: {premier_prix} / 2ème Prix: {deuxieme_prix}")
    print("-------------------")

# Ne pas fermer le navigateur immédiatement
time.sleep(10)
# navigateur.quit()  # Décommenter pour fermer automatiquement le navigateur
