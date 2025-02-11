import streamlit as st
import os
from dotenv import load_dotenv
import sqlite3

st.title("Application Locale avec Authentification Google")

def load_auth_config():
    """
    Charge les variables d'environnement depuis le fichier .env
    et les insère dans st.secrets pour configurer l'authentification.
    """
    # Charge le fichier .env
    load_dotenv()

    # Accès direct au singleton des secrets de Streamlit
    from streamlit.runtime.secrets import secrets_singleton

    # Configuration d'authentification pour Google
    auth_secrets = {
        "auth": {
            "redirect_uri": os.getenv("REDIRECT_URI", "http://localhost:8501/oauth2callback"),
            "cookie_secret": os.getenv("COOKIE_SECRET", "4PYGCElunlUn2VF75Mfr1Sb-FEx9A8R5CGaChoR6NOw"),
            "google": {
                "client_id": os.getenv("CLIENT_ID", ""),
                "client_secret": os.getenv("CLIENT_SECRET", ""),
                # URL des métadonnées OpenID Connect pour Google
                "server_metadata_url": "https://accounts.google.com/.well-known/openid-configuration",
                "client_kwargs": {
                    "prompt": "consent"  # Affiche l'écran de consentement à chaque connexion (modifiable en "select_account" par exemple)
                }
            }
        }
    }

    # Injection de la configuration dans le singleton des secrets de Streamlit
    secrets_singleton._secrets = auth_secrets

    # Optionnel : mettre à jour les variables d'environnement internes de Streamlit
    for k, v in auth_secrets.items():
        secrets_singleton._maybe_set_environment_variable(k, v)

# Charger la configuration d'authentification depuis le fichier .env
load_auth_config()
# Fonction pour initialiser la base de données SQLite
def init_db():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            name TEXT,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

# Fonction pour enregistrer les données de l'utilisateur
def save_user_data(email, name, data):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (email, name, data) 
        VALUES (?, ?, ?)
        ON CONFLICT(email) DO UPDATE SET data = ?
    """, (email, name, data, data))
    conn.commit()
    conn.close()

# Fonction pour récupérer les données de l'utilisateur
def get_user_data(email):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else ""

# Initialiser la base de données
init_db()

# Vérifier si l'utilisateur est connecté
if not st.experimental_user.get("is_logged_in", False):
    st.header("Connexion requise")
    st.write("Veuillez vous connecter avec votre compte Google pour accéder à l'application.")
    if st.button("Se connecter avec Google"):
        st.login("google")
else:
    st.success("Vous êtes connecté !")

    # Récupérer les informations de l'utilisateur
    user = st.experimental_user
    email = user.get("email", "inconnu")
    name = user.get("name", "Utilisateur inconnu")

    st.write(f"Bonjour, **{name}** 👋")
    
    # Récupérer les données précédemment stockées
    stored_data = get_user_data(email)
    
    st.subheader("Vos données stockées :")
    user_input = st.text_area("Modifiez vos données personnelles :", value=stored_data)
    
    if st.button("Enregistrer"):
        save_user_data(email, name, user_input)
        st.success("Vos données ont été enregistrées avec succès !")

    # Afficher les données stockées
    st.subheader("Données actuelles :")
    st.write(get_user_data(email))

    if st.button("Se déconnecter"):
        st.logout()