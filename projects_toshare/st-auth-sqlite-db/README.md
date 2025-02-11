Voici un exemple complet de README en français pour votre projet :

---

# Application Locale avec Authentification Google

Ce projet est une application web locale développée avec [Streamlit](https://streamlit.io/), qui permet aux utilisateurs de se connecter via leur compte Google grâce à l'implémentation d'OpenID Connect et OAuth 2.0. Une base de données SQLite est utilisée pour stocker et récupérer les données des utilisateurs.

## Fonctionnalités

- **Authentification Google** : Connexion sécurisée en utilisant les API OAuth 2.0 de Google, conforme au protocole OpenID Connect.
- **Stockage de données** : Enregistrement et mise à jour des données utilisateurs dans une base SQLite.
- **Interface simple et interactive** : Grâce à Streamlit, l'interface est facile à prendre en main et à utiliser.

## Configuration de l'authentification avec GCP

Pour configurer l'authentification via Google, vous devez effectuer plusieurs étapes dans la Google Cloud Console :

1. **Création d'un projet**  
   Rendez-vous sur la [Google Cloud Console](https://console.cloud.google.com/) et créez un nouveau projet.

2. **Activation des API OAuth 2.0**  
   Dans le projet, activez l'API OAuth 2.0 afin de pouvoir utiliser les services d'authentification de Google.

3. **Obtention des identifiants OAuth 2.0**  
   - Créez des identifiants pour une application OAuth 2.0.  
   - Vous obtiendrez un **Client ID** et un **Client Secret** qui sont indispensables pour l'authentification.
   - Pour visualiser ces identifiants, cliquez sur le nom de vos identifiants dans la section **Clients** de la console.

4. **Définition de l'URI de redirection**  
   Configurez l'URI de redirection dans la Google Cloud Console pour que Google sache où rediriger l'utilisateur après authentification. Par exemple :  
   ```
   http://localhost:8501/oauth2callback
   ```

5. **Personnalisation de l'écran de consentement**  
   Dans la console, vous pouvez personnaliser l'écran de consentement (branding, logo, etc.) qui est présenté aux utilisateurs lors de la connexion. Cela inclut la description des données auxquelles l'application souhaite accéder (adresse email, profil de base, etc.).

6. **Intégration dans votre projet**  
   Créez un fichier `.env` à la racine de votre projet et ajoutez-y les variables d'environnement nécessaires :
   ```env
   REDIRECT_URI=http://localhost:8501/oauth2callback
   COOKIE_SECRET=VotreCookieSecretIci
   CLIENT_ID=VotreClientIDIci
   CLIENT_SECRET=VotreClientSecretIci
   ```
   Le code Python utilise la bibliothèque [python-dotenv](https://pypi.org/project/python-dotenv/) pour charger ces variables et les injecter dans `st.secrets`, ce qui permet à Streamlit de configurer l'authentification automatiquement.

Pour plus de détails sur l'implémentation et la certification OpenID Connect de Google, vous pouvez consulter la [documentation officielle de Google sur OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect) et le [guide "Sign in with Google"](https://developers.google.com/identity/sign-in/web/sign-in).

## Installation des dépendances

Assurez-vous d'avoir [Python](https://www.python.org/) installé sur votre machine, puis installez les dépendances nécessaires avec pip :

```bash
pip install streamlit python-dotenv
```

> **Note :**  
> La bibliothèque `sqlite3` est incluse dans la bibliothèque standard de Python. Il n'est donc pas nécessaire de l'installer séparément.

## Lancer l'application

Pour démarrer l'application, exécutez la commande suivante dans votre terminal :

```bash
streamlit run nom_du_fichier.py
```

Remplacez `nom_du_fichier.py` par le nom de votre fichier contenant le code (par exemple, `app.py`).

## Structure du projet

- **app.py** : Fichier principal contenant le code source de l'application.
- **.env** : Fichier de configuration pour les variables d'environnement (à créer localement, non inclus dans le dépôt).
- **user_data.db** : Base de données SQLite utilisée pour stocker les informations des utilisateurs (créée automatiquement lors du lancement).

## Contribuer

Les contributions sont les bienvenues !  
Pour proposer des améliorations ou corriger des bugs, veuillez créer une branche à partir de `main`, effectuer vos modifications, puis soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

Ce README fournit une vue d'ensemble du projet, des instructions pour la configuration de l'authentification avec Google via GCP, ainsi que les étapes pour installer et lancer l'application. N'hésitez pas à adapter et à compléter ce fichier selon vos besoins spécifiques.
