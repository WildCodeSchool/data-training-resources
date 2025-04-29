---
title: Projet 2
description: 'Système de recommandation de chansons'
layout: default
---

## Introduction

![Header](assets/image/header_music.PNG)
{: .text-center }

« [Spotify](https://fr.wikipedia.org/wiki/Spotify) est un service de streaming musical donnant accès à des millions de titres, podcasts et contenus audio sur une large gamme d’appareils connectés à Internet. »

Créé en 2006, Spotify compte aujourd’hui plus de 600 millions d’utilisateurs mensuels et génère plus de 13 milliards de dollars de chiffre d’affaires annuel.

Lorsqu’un auditeur ouvre l’application, l’algorithme de recommandation l’aide à découvrir de nouvelles chansons, albums ou playlists susceptibles de lui plaire, en se basant sur ses écoutes précédentes et sur l’analyse de millions de signaux audio et comportementaux. Spotify est l’archétype de l’entreprise *data-driven*.

**Votre client n’est pas Spotify, mais il a de grandes ambitions !**

## Objectif & Enjeux

![CreuseMap](assets/image/creuse_music.PNG)
{: .text-center }

Vous êtes Data Analyst freelance. Une salle de concert associative située dans la Creuse souhaite lancer une **plateforme web** destinée aux habitants du département : recommandations de morceaux, création de playlists, partage d’écoutes.

Pour aller plus loin, on vous demande de mettre en place un moteur capable :

1. De recommander une chanson « similaire » à celle choisie par l’utilisateur.  
2. De composer une playlist correspondant à **l’humeur** (joyeuse, chill, énergique…) ou à **l’activité** courante (sport, travail, détente…).

Pour l’instant, aucun utilisateur n’a encore indiqué ses goûts : **vous êtes en situation de _cold start_**.  
Heureusement, le client met à votre disposition un jeu de données Spotify (plusieurs centaines de milliers de titres) contenant les caractéristiques audio (danceability, valence, energy, tempo, etc.).

### Enrichissement indispensable

Le dataset standard Spotify ne contient ni « humeur » ni « activité ». Vous devrez donc **enrichir** les données :

- Récupérer les *tags* Last.fm, AllMusic ou MusicBrainz (API publiques) ;
- Analyser les paroles avec du _sentiment analysis_ (API Hugging Face, spaCy) ;
- Utiliser la cartographie des fonctionnalités audio Spotify (valence ↔︎ émotion, energy ↔︎ dynamisme) pour inférer des labels.

Ces étapes d’enrichissement seront détaillées dans le projet.

## Objectif & Enjeux (suite)

![Scikit-Learn Logo](assets/image/scikit_learn_logo_music.PNG)
{: .text-center }

Une fois la phase analytique terminée, vous implémenterez des **algorithmes de machine learning** :

- **K-NN** ou **Approximate NN** sur les embeddings audio ;
- **Matrix Factorization** sur le couple utilisateur × morceau (quand les premiers retours d’usage seront disponibles) ;
- Génération de playlists par **clustering** (K-Means, HDBSCAN) des pistes ;
- *Fine-tuning* possible d’un modèle de langage musical (MusicLM / Jukebox) pour l’aspect créatif.

Le client souhaite également récupérer les pochettes via l’[API Spotify](https://developer.spotify.com/documentation/web-api/) (endpoint `/albums/{id}`) et les afficher dans l’interface.

**Attention !** Il ne s’agit pas de diffuser de la musique en salle : l’application est un service **complémentaire** en ligne, pensé pour la fidélisation des spectateurs.

## Ressources

- [API Spotify – documentation](https://developer.spotify.com/documentation/web-api/)
- [Dataset Spotify Tracks (Kaggle)](https://www.kaggle.com/datasets/maharshipandya/spotify-dataset-19212020-600k-tracks)
- [API Last.fm – Get Tags](https://www.last.fm/api/show/track.getTopTags)
- [Lyrics OVH](https://lyricsovh.docs.apiary.io/) ou [Genius API](https://docs.genius.com/)
- [Playlists « mood » publiques Spotify](https://open.spotify.com/genre/mood) (pour créer un jeu d’entraînement)

## Remarques Techniques

- Les datasets peuvent être chargés directement dans Pandas via leur URL (CSV gzip).  
  `pd.read_csv("https://...", compression="gzip", nrows=1000)`
- Le jeu complet (~600 k pistes) pèse plus de 500 Mo ; filtrez puis exportez un sous-ensemble propre pour accélérer vos expérimentations.
- Travaillez idéalement en local (Anaconda/Jupyter) ; Google Colab reste possible mais dépendant de la charge serveur.
- Pensez à **versionner vos notebooks et scripts** ; nettoyez-les avant commit (extension *nbstripout*, *jupytext*…).

## Organisation et Planning

| Semaine | Tâches principales | Compétences |
|---------|-------------------|-------------|
| **1 & 2** | Étude de marché : habitudes d’écoute dans la Creuse (CNC, SNEP, Insee). | Desk research, data viz |
| **3 & 4** | Acquisition, exploration, nettoyage, **enrichissement mood/activity**. | Pandas, APIs, NLP |
| **5 & 6** | Modélisation : algos de recommandation, évaluation offline. | scikit-learn, implicit |
| **7** | Affinage, **interface** (Streamlit, Dash, Power BI) et présentation finale. | Dev web, storytelling |

Le projet est réalisé **par binôme** ; dépôt GitHub commun ; gestion de projet via GitHub Projects/Kanban et *pull requests* systématiques.

## Besoins Clients

- **Statistiques & KPI** : répartition des genres, durée moyenne, distribution valence/energy, artistes les plus présents… visualisés dans un dashboard.
- **Recommandation** :  
  1. Suggestions de titres proches d’un morceau donné (champ *input*).  
  2. Playlist générée selon humeur ou activité sélectionnée (menu déroulant).

## Missions et Livrables Attendus

### Missions

- Présentation orale (15 min) détaillant : démarche, outils, difficultés, axes d’amélioration.
- Démonstration du dashboard et du système de recommandation (cas d’usage live).

### Livrables

1. **Notebook Exploration** : nettoyage + visualisations commentées.  
2. **Dashboard** (Streamlit, Power BI ou équivalent) avec KPI.  
3. **Notebook Recommandation** : code + commentaires + export des modèles (pickle/joblib).  
4. Documentation Markdown dans le dépôt (`docs/` ou Wiki) : guide d’installation et d’usage.

## Documentation

### Spotify Dataset – Colonnes principales

| Colonne | Description |
|---------|-------------|
| `id` | Identifiant unique de la piste (Spotify URI). |
| `name` | Titre de la chanson. |
| `artists` | Liste des artistes. |
| `release_date` | Date de sortie (AAAA-MM-JJ). |
| `duration_ms` | Durée en millisecondes. |
| `danceability` | De 0 à 1 : capacité à danser. |
| `energy` | Intensité perçue. |
| `loudness` | Volume moyen (dB). |
| `speechiness` | Présence de parole. |
| `acousticness` | Caractère acoustique. |
| `instrumentalness` | Probabilité d’être instrumental. |
| `liveness` | Indice de performance live. |
| `valence` | Positivité / humeur musicale. |
| `tempo` | Tempo (BPM). |
| `time_signature` | Chiffre de mesure. |
| `key`, `mode` | Tonalité et mode (majeur/mineur). |

### Stratégies d’Enrichissement *Mood* / *Activity*

1. **Tags communautaires**  
   - Last.fm `track.getTopTags` → *happy*, *workout*, *study*…  
   - Filtrer / normaliser les tags les plus fréquents pour créer des labels.

2. **Analyse des paroles**  
   - Récupérer les lyrics (Genius, Lyrics OVH).  
   - _Sentiment analysis_ (polarity, subjectivity), détection d’émotions (NRC Lexicon).  
   - Mapping vers des classes *mood* standard (*joyful*, *melancholic*, *calm*, …).

3. **Audio Features Heuristics**  
   - (valence > 0.7 & energy > 0.6) ⇒ *Happy / Workout*  
   - (valence < 0.3 & acousticness > 0.5) ⇒ *Sad / Relax*  
   - Concevoir une grille heuristique puis la valider sur playlists « Mood » officielles.

4. **Playlists publiques**  
   - Scraper les playlists Spotify par activité (*Morning Run*, *Deep Focus*, *Dinner with Friends*).  
   - Attribuer l’activité dominante à toutes les pistes de la playlist (semi-supervisé).

> **Conseil** : constituer un échantillon de 10 000 pistes labellisées afin de tester vos modèles de classification (baseline : Random Forest, MLP ; puis fine-tuning BERT lyrics + audio embeddings).

---

En suivant cette trame, vous proposerez aux étudiant·e·s un projet clair, structuré et parfaitement aligné sur les exigences pédagogiques (travail collaboratif, gestion de version, démarche data-science complète).  
Bon courage et bonne musique ! 🎧
