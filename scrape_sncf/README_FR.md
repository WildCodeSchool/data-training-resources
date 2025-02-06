# SNCF Scraper de Prix de Trains 🚅

## Description

Ce script Python automatise la recherche de prix des billets de train sur SNCF Connect (sncf-connect.com). Il utilise Selenium WebDriver pour simuler les interactions utilisateur et extraire les informations de prix pour les voyages en train entre les villes françaises spécifiées.

## Fonctionnalités

- Recherche automatisée de billets de train entre deux villes françaises
- Extraction de multiples options de voyage avec informations détaillées :
  - Heures de départ et d'arrivée
  - Noms des gares
  - Prix en première et seconde classe
- Utilisation d'un profil Chrome réel pour éviter la détection
- Implémentation d'un comportement humain avec délais aléatoires et mouvements de souris
- Gestion du chargement dynamique des pages et des suggestions

## Prérequis

- Python 3.x
- Navigateur Google Chrome
- Chrome WebDriver
- Un profil Chrome valide

## Bibliothèques Requises

```bash
pip install -r requirements.txt
```

## Configuration

Avant d'exécuter le script, vous devez configurer le chemin de votre profil Chrome. Par défaut, il est configuré pour Windows :

```python
options.add_argument(r"--user-data-dir=C:\Users\coach\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Default")
```

Modifiez ces chemins selon votre configuration système.

## Utilisation

1. Lancez le script :
```bash
python sncf_scraper.py
```

2. Saisissez les informations demandées :
- Ville de départ
- Ville d'arrivée

3. Le script va :
- Ouvrir Chrome avec votre profil
- Naviguer vers SNCF Connect
- Saisir vos détails de voyage
- Extraire et afficher les options de train disponibles
- Montrer les prix en première et seconde classe

## Exemple de Sortie

```
Prix recommandé : 45€
-------------------
Départ : 10:30 de PARIS GARE DE LYON
Arrivée : 12:30 à LYON PART DIEU
1er Prix : 89€ / 2ème Prix : 45€
-------------------
```

## Notes Importantes

- Le script utilise votre vrai profil Chrome pour éviter les CAPTCHA et les problèmes d'authentification
- Des délais aléatoires sont implémentés pour simuler un comportement humain
- Gardez la fenêtre Chrome visible pendant l'exécution
- N'interagissez pas avec le navigateur pendant l'exécution du script
- Le script inclut un délai de 10 secondes à la fin avant la fermeture

## Détails Techniques

Le script utilise plusieurs fonctionnalités de Selenium :
- WebDriverWait pour gérer le contenu dynamique
- ActionChains pour simuler les mouvements de souris
- Exécution JavaScript pour le défilement fluide et la gestion des entrées
- Sélecteurs CSS et XPath pour la localisation des éléments

## Limitations

- Fonctionne uniquement avec la disposition actuelle de SNCF Connect (Février 2025)
- Nécessite une connexion Internet stable
- Peut nécessiter des ajustements si SNCF Connect met à jour la structure de leur site

## Notice Légale

Ce script est uniquement à des fins éducatives. Assurez-vous de respecter les conditions d'utilisation de SNCF Connect lors de l'utilisation d'outils automatisés.

## Contribution

N'hésitez pas à soumettre des problèmes et des demandes d'amélioration !

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

---
Fait avec ❤️ pour le groupe de la Wild Code School qui travaille sur l'automatisation des voyages en train
