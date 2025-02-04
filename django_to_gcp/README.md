# Déploiement GCP - Guide d'Installation

## Prérequis
- Compte Google Cloud Platform
- PowerShell (Windows)
- gcloud CLI

## Configuration GCP

1. **Création Projet**
   - Créer nouveau projet GCP
   - Activer Cloud Run et Cloud Build API

2. **Artifact Registry**
   ```
   - Format: Docker
   - Mode: Standard
   - Region: europe-west4
   - Nom: utiliser tirets uniquement (-)
   - Immutable tags: activé
   ```

## Installation gcloud CLI

**Windows PowerShell:**
```powershell
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")

& $env:Temp\GoogleCloudSDKInstaller.exe
```

## Configuration

1. **Initialisation:**
   - Accepter autorisation Google
   - Sélectionner projet
   - ```bash
     gcloud auth configure-docker europe-west4-docker.pkg.dev
     ```

2. **Build & Deploy:**
   ```bash
   gcloud builds submit --tag europe-west4-docker.pkg.dev/ID_PROJET_GCP/nom-repo/nom-image:tag
   ```
   Exemple:
   ```bash
   gcloud builds submit --tag europe-west4-docker.pkg.dev/django-to-gcp/django-to-gcp/djangoimg:djangotag
   ```

## IAM Permissions
- Rôles requis:
  - Editor
  - Storage Object Viewer

## Cloud Run
1. Create Service
2. Sélectionner image depuis Artifact Registry
3. Configuration:
   - Region: europe-west4
   - Allow unauthenticated invocations

## Notes
- Utiliser uniquement des tirets (-)
- Pas de majuscules dans les noms
- Conserver les mêmes noms entre services

[Documentation officielle GCP](https://cloud.google.com/sdk/docs/install?hl=fr)
