# Installation de Mage AI avec Docker et PostgreSQL (macOS)

Ce guide vous permettra d'installer et de configurer Mage AI avec PostgreSQL dans un environnement Docker sur macOS.

## Prérequis

- macOS Monterey (12.0) ou plus récent
- [Docker Desktop pour Mac](https://www.docker.com/products/docker-desktop/) installé et fonctionnel
- [Visual Studio Code](https://code.visualstudio.com/) (recommandé)
- Extension Docker pour VSCode (recommandée)
- Git installé sur votre machine
- Terminal (intégré à macOS)

## 1. Préparation de l'environnement (Sur Terminal ou VSCode)

### 1.1 Nettoyage de Docker (si nécessaire)

Si vous avez déjà travaillé avec Docker, il est recommandé de nettoyer votre environnement :

```bash
# Arrêter tous les conteneurs en cours d'exécution
docker stop $(docker ps -a -q)

# Supprimer tous les conteneurs
docker rm $(docker ps -a -q)

# Supprimer tous les volumes non utilisés
docker volume prune

# Supprimer toutes les images non utilisées
docker system prune -a
```

⚠️ **Attention** : La commande `docker system prune -a` supprimera toutes les images Docker non utilisées. Assurez-vous de ne pas avoir des images importantes que vous souhaitez conserver.

### 1.2 Configuration de l'environnement Python

```bash
# Créer un environnement virtuel
python3 -m venv docker_mage

# Activer l'environnement virtuel
source docker_mage/bin/activate
```

## 2. Cloner le repository

```bash
# Cloner le repository
git clone https://github.com/WildCodeSchool/data-training-resources.git repo_to_clone

# Accéder au dossier du projet
cd repo_to_clone/
```

## 3. Structure des fichiers

Vérifiez que vous avez bien tous les fichiers nécessaires :

```
repo_to_clone/
│
├── .env                  # Variables d'environnement
├── docker-compose.yml    # Configuration Docker Compose
├── Dockerfile           # Instructions de build de l'image
├── io_config.yaml       # Configuration Mage AI
├── requirements.txt     # Dépendances Python
└── README_macOs.md            # Ce fichier
```

## 4. Construction et démarrage des conteneurs

Assurez-vous d'être dans le bon dossier :
```bash
# Vérifier votre position dans l'arborescence
pwd

# Si nécessaire, retournez dans le dossier du projet
cd repo_to_clone
```

Ensuite, lancez la construction et le démarrage :
```bash
# Construire les images
docker compose build

# Démarrer les conteneurs
docker compose up
```

Pour exécuter en arrière-plan (mode détaché) :
```bash
docker compose up -d
```

## 5. Vérification de l'installation

1. Ouvrez Docker Desktop et vérifiez que les deux conteneurs sont en cours d'exécution :
   - `[PROJECT_NAME]_mageai`
   - `[PROJECT_NAME]_postgres`

2. Accédez à l'interface Mage AI :
   - Ouvrez votre navigateur
   - Accédez à `http://localhost:6789`

## 6. Arrêt des conteneurs

Pour arrêter les conteneurs :
```bash
# Si en mode détaché
docker compose down

# Si en mode interactif
# Appuyez sur Ctrl+C puis exécutez :
docker compose down
```

## 7. Commandes utiles

```bash
# Voir les logs des conteneurs
docker compose logs

# Voir les logs d'un conteneur spécifique
docker compose logs mageai
docker compose logs postgres

# Redémarrer les conteneurs
docker compose restart

# Reconstruire les images et redémarrer les conteneurs
docker compose up --build
```

## Résolution des problèmes courants

### Les conteneurs ne démarrent pas

1. Vérifiez que Docker Desktop est en cours d'exécution
2. Vérifiez que les ports 6789 et 5432 ne sont pas déjà utilisés
3. Consultez les logs avec `docker compose logs`

### Erreur "port is already allocated"

```bash
# Identifier le processus utilisant le port
lsof -i :6789
lsof -i :5432

# Arrêter le processus (remplacer [PID] par l'ID du processus)
kill -9 [PID]
```

### Problèmes de permissions

Si vous rencontrez des problèmes de permissions sur macOS :
1. Assurez-vous que Docker Desktop a accès à votre dossier de projet dans Préférences > Resources > File sharing
2. Exécutez les commandes avec `sudo` si nécessaire
3. Vérifiez les permissions du dossier : `ls -la`

## Support

En cas de problème :
1. Consultez les logs Docker
2. Vérifiez que tous les fichiers de configuration sont correctement formatés
3. Assurez-vous que Docker Desktop dispose de suffisamment de ressources dans Préférences > Resources

## Notes importantes

- Ne modifiez pas les fichiers de configuration pendant que les conteneurs sont en cours d'exécution
- Assurez-vous d'avoir suffisamment d'espace disque disponible (minimum 10GB recommandé)
- Gardez Docker Desktop à jour
- En cas de modification des fichiers de configuration, redémarrez les conteneurs
- Sur les Macs M1/M2 (Apple Silicon), assurez-vous d'avoir la dernière version de Docker Desktop compatible

## Ressources additionnelles

- [Documentation officielle de Mage AI](https://docs.mage.ai/)
- [Documentation Docker](https://docs.docker.com/)
- [Documentation PostgreSQL](https://www.postgresql.org/docs/)
