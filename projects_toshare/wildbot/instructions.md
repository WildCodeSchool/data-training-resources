# 🤖 Wild bot en Python

Ce projet permet de déployer un bot discord intelligent sur un serveur de la wild en se basant sur des modèles de langage (pour le moment, gemini1.5 flash, étant gratuit)

---

## 📦 Installation

- Python 3.8+

On installe les librairies avec un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Etapes pour créer son bot discord et accéder au modèle de langage Gemini

### DISCORD :

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** and name it.
3. Go to the **Bot** tab and click **"Add Bot"**
4. Copy the **Bot Token** (keep this secret!)
5. Under **OAuth2 → URL Generator**:
   - Select `bot` scope
   - Under **Bot Permissions**, select at least: `Send Messages`, `Read Message History`
   - Copy the generated URL and use it to invite your bot to your server

### GEMINI

Aller sur ce site et créer une clé API pour utiliser les modèles de langage

https://aistudio.google.com/prompts/new_chat

### Configuration

Pour faire fonctionner le script, nous avons besoin de deux clés : la clé de notre bot discord, et la clé de l'API gemini.  `Ces clés seront placées dans un fichier .env`

```
DISCORD_BOT_KEY = XXX
API_GEMINI_KEY = XXX
```

---

## 🧪 Lancer le BOT

```bash
python bot.py
```

Tu devrais voir

---

## 📌 Next Steps

- Améliorer le prompt
- Améliorer la doc
- Fournir une interface pour modifier le prompt à distance
