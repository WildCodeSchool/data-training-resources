---

# Application Text-to-Speech avec Zyphra (Async)

Cette application utilise [Streamlit](https://streamlit.io/) pour créer une interface web permettant de convertir du texte en audio grâce à l'API Zyphra. Le code exploite des fonctions asynchrones (async/await) et utilise `nest_asyncio` pour permettre l'exécution de boucles d'événements imbriquées, notamment dans l'environnement Streamlit.

## Prérequis

- **Python 3.7 ou supérieur**
- **Clé API Zyphra** : Vous devez disposer d'un compte et d'une clé API valide pour utiliser les services de Zyphra.
- **Fichier audio de référence** : Le code attend un fichier audio nommé `record_out.wav` qui sera utilisé comme base pour la synthèse vocale.

## Installation

1. **Cloner ou télécharger le dépôt**

   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_REPERTOIRE>
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé)**

   ```bash
   python -m venv env
   ```

   - Sous Linux/Mac :
     ```bash
     source env/bin/activate
     ```
   - Sous Windows :
     ```bash
     env\Scripts\activate
     ```

3. **Installer les dépendances**

   Installez les packages requis via pip :

   ```bash
   pip install streamlit nest_asyncio zyphra
   ```

4. **Préparer le fichier audio**

   Assurez-vous que le fichier `record_out.wav` est présent dans le répertoire racine du projet. Ce fichier est lu et encodé en base64 pour être utilisé par l'API Zyphra.

5. **Configurer la clé API Zyphra**

   Dans le code source, repérez la ligne suivante :

   ```python
   API_KEY = "API_KEY"
   ```

   Remplacez `"API_KEY"` par votre clé API personnelle.

   **Option alternative :**  
   Vous pouvez utiliser la gestion des secrets de Streamlit. Pour cela, créez un dossier nommé `.streamlit` à la racine du projet et, à l'intérieur, créez un fichier `secrets.toml` contenant :

   ```toml
   api_key = "VOTRE_CLÉ_API"
   ```

   Ensuite, modifiez le code pour récupérer la clé via `st.secrets["api_key"]` :
   
   ```python
   API_KEY = st.secrets["api_key"]
   ```

## Exécution de l'application

Pour lancer l'application, exécutez la commande suivante dans votre terminal :

```bash
streamlit run nom_du_fichier.py
```

> **Remarque :** Remplacez `nom_du_fichier.py` par le nom du fichier contenant le code (par exemple, `app.py`).

Une fois lancée, l'interface Streamlit s'ouvrira dans votre navigateur par défaut.

## Utilisation

1. **Saisie du texte**  
   Dans l'interface, saisissez le texte que vous souhaitez convertir en audio dans la zone de texte.

2. **Paramétrage**  
   - **Taux de parole** : Utilisez le curseur pour ajuster la vitesse de parole.
   - **Langue** : Choisissez la langue souhaitée (par exemple, `en-us`, `fr-fr`, etc.).
   - **Format de sortie** : Sélectionnez le format de l'audio (par exemple, `audio/wav`, `audio/mp3`, etc.).

3. **Génération de l'audio**  
   Cliquez sur le bouton **"Generate Audio"**. Le processus de génération s'exécutera de manière asynchrone. Un message d'information s'affichera pendant le traitement.

4. **Lecture de l'audio**  
   Une fois l'audio généré avec succès, il sera intégré dans l'interface Streamlit et vous pourrez l'écouter directement.

## Dépannage

- **Clé API invalide ou manquante :**  
  Vérifiez que vous avez bien renseigné votre clé API soit directement dans le code, soit via le fichier `secrets.toml`.

- **Fichier `record_out.wav` introuvable :**  
  Assurez-vous que le fichier existe dans le répertoire racine du projet et qu'il est accessible en lecture.

- **Problèmes de dépendances :**  
  Si vous rencontrez des erreurs liées aux modules, vérifiez que toutes les dépendances ont été correctement installées avec la commande `pip install streamlit nest_asyncio zyphra`.

- **Erreurs liées à l'API Zyphra :**  
  En cas d'erreur retournée par l'API (affichée via `ZyphraError`), vérifiez l'état de votre connexion Internet et la validité de votre clé API.

## Remarques

- **nest_asyncio :**  
  Ce module permet de contourner le problème des boucles d'événements imbriquées dans Streamlit. Il est appliqué dès le début du script avec `nest_asyncio.apply()`.

- **Asynchronicité :**  
  Le code fait appel à des fonctions asynchrones pour interagir avec l'API Zyphra. La fonction `asyncio.run()` est utilisée pour exécuter ces fonctions, ce qui est rendu possible grâce à `nest_asyncio`.

## Licence

Wild Code School - Soufiane Maski

## Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une _issue_ dans le dépôt ou à me contacter directement: soufianemaski1@gmail.com

---

Ce README devrait vous permettre de configurer, installer et faire fonctionner l'application de synthèse vocale avec Zyphra tout en clonnant une voix. Bonne utilisation !
