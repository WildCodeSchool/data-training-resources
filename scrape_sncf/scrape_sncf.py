from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Récupération des données des villes de départ et d'arrivée

ville_depart = input("Ville de départ: ")
ville_arrivee = input("Ville d'arrivée: ")

# Configuration des options Chrome
options = webdriver.ChromeOptions()

# Ajout du chemin du profil Chrome
options.add_argument(r"--user-data-dir=C:\Users\coach\AppData\Local\Google\Chrome\User Data") 
options.add_argument(r"--profile-directory=Default")

# Désactiver la détection des bots
options.add_argument("--disable-blink-features=AutomationControlled")

# Démarrer le navigateur avec le profil réel
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

# Gérer la ville de départ
champ_depart = attente.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input[placeholder="D\'où partons-nous ?"]'))
)

# Saisir la ville de départ
navigateur.execute_script("arguments[0].value = arguments[1];", champ_depart, ville_depart)
navigateur.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });") # TRES IMPORTANT POUR SCROLL
navigateur.execute_script("arguments[0].dispatchEvent(new Event('input'));", champ_depart)

# Attendre le chargement des suggestions
time.sleep(2)
liste_suggestions_depart = attente.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-autocomplete="list"]')))

# Obtenir la valeur de l'attribut aria-activedescendant
id_actif_depart = liste_suggestions_depart.get_attribute('aria-activedescendant')
print("ID actif départ:", id_actif_depart)

if id_actif_depart:
    # Cliquer sur la première suggestion en utilisant l'ID actif
    premiere_suggestion = attente.until(
        EC.presence_of_element_located((By.ID, id_actif_depart))
    )
    premiere_suggestion.click()
else:
    # Approche alternative : trouver la première suggestion dans la liste déroulante
    premiere_suggestion = attente.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[role="option"]'))
    )
    premiere_suggestion.click()

time.sleep(random.uniform(1, 2))  # Attente entre les saisies

# Gérer la ville d'arrivée
champ_arrivee = attente.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input[placeholder="Où allons-nous ?"]'))
)

# Saisir la ville d'arrivée
navigateur.execute_script("arguments[0].value = arguments[1];", champ_arrivee, ville_arrivee)
navigateur.execute_script("arguments[0].dispatchEvent(new Event('input'));", champ_arrivee)

# Attendre le chargement des suggestions pour l'arrivée
time.sleep(2)
liste_suggestions_arrivee = attente.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-autocomplete="list"]'))
)

# Obtenir la valeur de l'attribut aria-activedescendant pour l'arrivée
id_actif_arrivee = liste_suggestions_arrivee.get_attribute('aria-activedescendant')
print("ID actif arrivée:", id_actif_arrivee)

if id_actif_arrivee:
    # Cliquer sur la première suggestion d'arrivée
    premiere_suggestion_arrivee = attente.until(
        EC.presence_of_element_located((By.ID, id_actif_arrivee))
    )
    premiere_suggestion_arrivee.click()
else:
    # Approche alternative pour l'arrivée
    premiere_suggestion_arrivee = attente.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[role="option"]'))
    )
    premiere_suggestion_arrivee.click()

# Faire défiler vers le bas pour trouver le bouton
navigateur.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(random.uniform(1, 2))

bouton_voir_prix = attente.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Voir les prix')]")))
bouton_voir_prix.click()

time.sleep(4)

# Attendre que la liste soit présente
time.sleep(random.uniform(2, 3))

# Prix recommendé : chercher le div avec data-test="newPrice"
element_recommande = navigateur.find_elements(By.CSS_SELECTOR, 'span[data-test="newPrice"]')
prix_recommande = element_recommande[0].text
print(f"Prix recommandé: {prix_recommande}\n")
print("-------------------")

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
