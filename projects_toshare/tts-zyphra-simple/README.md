---

# Text-to-Speech avec Zyphra

Ce script simple convertit un texte en audio à l'aide de l'API Zyphra. Le code s'exécute de manière synchronisée et génère un fichier audio directement dans le répertoire de travail.

## Prérequis

- **Python 3.7 ou supérieur**  
- **Clé API Zyphra** : Vous devez obtenir une clé API valide auprès de [Zyphra](https://zyphra.io/) pour utiliser leurs services.
- **Connexion Internet** : Le script se connecte à l'API Zyphra pour générer l'audio.

## Installation

1. **Cloner ou télécharger le dépôt**

   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_REPERTOIRE>
   ```

2. **Créer un environnement virtuel (optionnel, mais recommandé)**

   ```bash
   python -m venv env
   ```

   Activez ensuite l'environnement virtuel :

   - Sous Linux/Mac :
     ```bash
     source env/bin/activate
     ```
   - Sous Windows :
     ```bash
     env\Scripts\activate
     ```

3. **Installer la dépendance**

   Installez le package `zyphra` via pip :

   ```bash
   pip install zyphra
   ```

## Configuration

Ouvrez le fichier contenant le code et localisez la ligne suivante :

```python
client = ZyphraClient(api_key="API_KEY")
```

Remplacez `"API_KEY"` par votre clé API personnelle fournie par Zyphra.

## Exécution du script

Pour lancer le script, exécutez la commande suivante dans votre terminal :

```bash
python nom_du_fichier.py
```

> **Remarque :** Remplacez `nom_du_fichier.py` par le nom de votre fichier (par exemple, `app.py`).

## Fonctionnement

Le script utilise l'API Zyphra pour convertir le texte suivant :

```python
text="Je suis le meilleur élève de la classe."
```

en un fichier audio nommé `output.webm` qui sera généré dans le même répertoire que le script. Vous pouvez modifier le texte, le taux de parole (`speaking_rate`) ou le code de langue (`language_iso_code`) selon vos besoins.

## Dépannage

- **Clé API invalide ou manquante :**  
  Vérifiez que vous avez bien remplacé `"API_KEY"` par votre clé API valide.
  
- **Erreur de connexion ou API :**  
  Assurez-vous d'avoir une connexion Internet stable et que l'API Zyphra est accessible.

- **Problèmes d'installation :**  
  Si le module `zyphra` n'est pas trouvé, vérifiez que vous l'avez bien installé via `pip install zyphra`.

## Licence

Indiquez ici la licence de votre projet (par exemple, MIT License).

## Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une _issue_ dans le dépôt ou à me contacter directement.

---

Ce fichier README vous guidera pour configurer, installer et exécuter le script de conversion de texte en audio avec l'API Zyphra. Bonne utilisation !
