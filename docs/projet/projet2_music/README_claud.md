---
title: Projet 3
description: 'Système de recommandation musicale'
layout: default
---

## Introduction

![Header](assets/image/spotify_header.png)

« [Spotify](https://fr.wikipedia.org/wiki/Spotify) est un service suédois de streaming musical sous la forme d'un logiciel propriétaire et d'un site web. Cette plateforme de distribution numérique permet une écoute quasi instantanée de fichiers musicaux. »

Lancé en 2008, Spotify compte aujourd'hui plus de 422 millions d'utilisateurs actifs mensuels, dont 182 millions d'abonnés payants, dans 183 pays. Avec plus de 82 millions de titres disponibles, Spotify révolutionne notre façon de découvrir et de consommer la musique.

Au cœur de l'expérience Spotify se trouve son système de recommandation sophistiqué qui suggère de nouvelles chansons aux utilisateurs et génère des playlists personnalisées comme "Découvertes de la semaine". Ce système analyse non seulement les habitudes d'écoute, mais également les caractéristiques audio des chansons, créant ainsi une expérience musicale personnalisée pour chaque utilisateur.

**Votre client n'est pas Spotify, mais il a des ambitions musicales significatives !**

## Objectif & Enjeux

Vous êtes un AI Engineer junior freelance. Une start-up française spécialisée dans les applications musicales vous contacte. Elle souhaite lancer une nouvelle application qui se démarque de la concurrence par ses recommandations musicales innovantes.

La start-up vous demande de développer trois fonctionnalités principales :

1. **Song-to-Song** : Recommander des chansons similaires à partir d'une chanson sélectionnée par l'utilisateur
2. **Mood-to-Playlist** : Générer une playlist adaptée à l'humeur exprimée par l'utilisateur (joyeux, mélancolique, énergique, etc.)
3. **Activity-to-Playlist** : Proposer une playlist adaptée à une activité spécifique (sport, méditation, travail, conduite, etc.)

Pour mener à bien ce projet, la start-up vous fournit un accès au dataset public de Spotify, mais celui-ci présente un défi majeur : **il ne contient pas de données explicites sur l'humeur ou les activités associées aux chansons**. Vous devrez donc enrichir ces données pour répondre aux objectifs du projet.

Commencez par une étude de marché sur les habitudes d'écoute musicale des français et sur les applications de recommandation musicale existantes. Cette analyse vous permettra de mieux comprendre les attentes des utilisateurs et de positionner votre solution de manière pertinente.

Après cette étude, réalisez une analyse approfondie de la base de données Spotify pour identifier les corrélations entre les caractéristiques audio et les perceptions humaines. Cette exploration devrait inclure : l'analyse des attributs audio (tempo, énergie, dansabilité, etc.), l'évolution des préférences musicales au fil du temps, la popularité des genres musicaux, et les caractéristiques communes aux titres les plus écoutés.

Sur la base de ces informations, vous devrez développer une stratégie d'enrichissement des données pour attribuer des "tags" d'humeur et d'activité aux chansons de la base de données.

## Objectif & Enjeux (suite)

![ML Logo](assets/image/ml_music_logo.PNG)
{: .text-center }

Après cette étape analytique et d'enrichissement, vous utiliserez des **algorithmes de machine learning** pour développer les trois fonctionnalités de recommandation demandées.

En complément des données Spotify, vous pourrez exploiter des sources externes comme [MusicBrainz](https://musicbrainz.org/), [Last.fm](https://www.last.fm/) ou [Genius](https://genius.com/) pour enrichir votre base de données avec des informations sur les paroles, les tags communautaires, ou d'autres métadonnées pertinentes. Il vous est également demandé de [récupérer les pochettes d'albums](https://developer.spotify.com/documentation/web-api/reference/get-track) pour les afficher dans votre interface de recommandation.

**Attention !** L'objectif n'est pas de créer un service de streaming musical complet, mais de développer un prototype fonctionnel du système de recommandation qui pourra être intégré ultérieurement à l'application complète. Votre prototype devra inclure une interface permettant de tester les trois fonctionnalités principales et de visualiser les résultats des recommandations.

## Ressources

Les données principales sont disponibles via le dataset Spotify, qui contient des informations détaillées sur les caractéristiques audio des chansons.

- [Spotify Dataset sur Kaggle](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
- [Documentation de l'API Spotify](https://developer.spotify.com/documentation/web-api)
- [Dataset Million Song](http://millionsongdataset.com/) (ressource complémentaire)
- [MusicBrainz](https://musicbrainz.org/) (pour l'enrichissement des données)
- [Last.fm API](https://www.last.fm/api) (pour les tags communautaires)

## Remarques Techniques

- Vous pouvez télécharger les datasets en local, sur votre Drive ou bien sur un GitHub. L'utilisation d'un dépôt GitHub est fortement recommandée pour faciliter la collaboration entre les membres du binôme.
- Le dataset Spotify contient des centaines de milliers de chansons avec leurs caractéristiques audio. Pensez à échantillonner judicieusement les données pour vos tests initiaux, puis à étendre progressivement votre analyse.
- Pour l'enrichissement des données avec des tags d'humeur et d'activité, plusieurs approches sont possibles :
  - **Text Mining** sur les paroles des chansons (via Genius API ou autres sources)
  - **Analyse de clustering** sur les caractéristiques audio pour identifier des groupes naturels
  - **Transfer Learning** à partir de tags communautaires existants (Last.fm)
  - **Crowdsourcing** : création d'un mini-système d'annotation manuelle pour un échantillon de chansons
- Pour la gestion collaborative du projet, utilisez les fonctionnalités de GitHub :
  - Branches pour les développements parallèles
  - Pull requests pour la revue de code
  - Issues pour le suivi des tâches et des bugs
  - Projects pour la planification agile
  - Actions pour l'intégration continue
- Veillez à documenter soigneusement votre code et vos méthodologies d'enrichissement de données pour faciliter la maintenance future du projet.

## Organisation et Planning

Ce projet se déroulera sur 7 semaines, en binôme. Voici un planning indicatif, que vous pouvez adapter selon vos contraintes et votre progression :

1. **Semaine 1** : Mise en place de l'environnement collaboratif (GitHub), étude de marché et exploration initiale des données Spotify
2. **Semaine 2** : Analyse approfondie des caractéristiques audio et de leurs corrélations, définition de la stratégie d'enrichissement
3. **Semaine 3** : Implémentation des méthodes d'enrichissement pour les tags d'humeur et validation
4. **Semaine 4** : Implémentation des méthodes d'enrichissement pour les tags d'activité et validation
5. **Semaine 5** : Développement des algorithmes de recommandation pour les trois fonctionnalités
6. **Semaine 6** : Création de l'interface utilisateur pour tester les recommandations et affiner les algorithmes
7. **Semaine 7** : Finalisation, tests utilisateurs, documentation et préparation de la présentation

**Points d'attention pour la collaboration en binôme :**
- Répartissez clairement les responsabilités entre les membres de l'équipe
- Organisez des points réguliers (daily standup recommandé) pour synchroniser vos avancées
- Documentez vos choix techniques et vos hypothèses dans le README du projet
- Utilisez des conventions de nommage et de codage cohérentes
- Pratiquez la revue de code mutuelle avant chaque fusion dans la branche principale

## Besoins Clients

Le client a besoin d'un prototype fonctionnel qui démontre l'efficacité des trois systèmes de recommandation. Pour répondre à ce besoin, vous développerez une application simple mais complète qui permet de :

- Rechercher une chanson et obtenir des recommandations de titres similaires
- Sélectionner une humeur et générer une playlist adaptée
- Choisir une activité et obtenir une playlist correspondante
- Visualiser des statistiques pertinentes sur les recommandations (caractéristiques audio moyennes, diversité des genres, etc.)

Vous pouvez implémenter cette interface au moyen d'un outil de votre choix :
- Une application web (Flask, Streamlit, Dash)
- Un notebook interactif (Jupyter avec widgets)
- Une application desktop simple (PyQt, Tkinter)

L'objectif n'est pas d'avoir une interface parfaite d'un point de vue esthétique, mais fonctionnelle et permettant de démontrer la pertinence de vos algorithmes de recommandation.

## Missions et Livrables Attendus

### Missions

- Réaliser une présentation synthétique de votre démarche, des méthodes d'enrichissement utilisées, des algorithmes de recommandation choisis, et des résultats obtenus.
- Présenter des indicateurs statistiques et KPI pertinents sur la qualité des recommandations.
- Faire une démonstration en direct des trois fonctionnalités de recommandation, en utilisant des exemples proposés par le client.

### Livrables

- Un dépôt GitHub complet contenant l'ensemble du code source, bien documenté et organisé.
- Des notebooks détaillant l'exploration des données, l'enrichissement avec les tags d'humeur et d'activité, et le développement des algorithmes de recommandation.
- Un rapport technique expliquant vos choix méthodologiques, les difficultés rencontrées et les pistes d'amélioration futures.
- Le prototype fonctionnel du système de recommandation avec son interface utilisateur.
- Un guide d'utilisation pour permettre au client de tester le prototype de manière autonome.

## Documentation

### Spotify Audio Features

Le dataset Spotify contient plusieurs caractéristiques audio pour chaque chanson. Voici les principales features que vous utiliserez :

- **acousticness** (float) : Mesure de 0 à 1 indiquant si la chanson est acoustique (1.0) ou non (0.0).
- **danceability** (float) : Mesure de 0 à 1 indiquant si la chanson est adaptée à la danse, basée sur le tempo, la régularité du rythme, la force de la pulsation.
- **energy** (float) : Mesure de 0 à 1 représentant l'intensité et l'activité perceptible. Les morceaux énergiques sont rapides, forts et bruyants.
- **instrumentalness** (float) : Mesure de 0 à 1 prédisant si un morceau ne contient pas de voix. Les valeurs proches de 1.0 indiquent une forte probabilité que le morceau soit instrumental.
- **key** (int) : La tonalité du morceau. Les entiers sont mappés selon la notation standard, où 0 = C, 1 = C♯/D♭, 2 = D, etc.
- **liveness** (float) : Mesure de 0 à 1 indiquant la probabilité que le morceau ait été enregistré en présence d'un public.
- **loudness** (float) : Le volume global d'un morceau en décibels (dB). Les valeurs typiques vont de -60 à 0 dB.
- **mode** (int) : Modalité (majeur = 1, mineur = 0) du morceau.
- **speechiness** (float) : Mesure de 0 à 1 détectant la présence de paroles. Les valeurs supérieures à 0.66 indiquent des pistes probablement entièrement parlées.
- **tempo** (float) : Le tempo estimé en battements par minute (BPM).
- **time_signature** (int) : Une estimation de la signature rythmique, mesurée en temps par mesure.
- **valence** (float) : Mesure de 0 à 1 décrivant la positivité musicale transmise par un morceau. Les titres à haute valence sonnent plus positifs.

### Enrichissement des Données

Pour enrichir votre dataset avec des informations sur l'humeur et les activités, plusieurs approches sont possibles :

#### Humeurs (exemples) :
- **Joyeux/Positif** : Forte valence (>0.7), haute énergie (>0.6)
- **Triste/Mélancolique** : Faible valence (<0.4), faible énergie (<0.4)
- **Énergique/Excitant** : Haute énergie (>0.8), tempo élevé (>120 BPM)
- **Calme/Relaxant** : Forte acousticness (>0.7), faible énergie (<0.4)
- **Nostalgique** : Valence moyenne (0.4-0.6), instrumentalness modérée

#### Activités (exemples) :
- **Sport/Workout** : Énergie très élevée (>0.8), tempo élevé (>120 BPM), danceability élevée (>0.7)
- **Concentration/Travail** : Faible speechiness (<0.2), instrumentalness élevée (>0.6)
- **Méditation/Relaxation** : Acousticness élevée (>0.8), énergie très faible (<0.3)
- **Fête/Soirée** : Danceability très élevée (>0.8), énergie élevée (>0.7)
- **Conduite** : Énergie modérée (0.5-0.7), valence modérée à élevée (0.5-0.8)

Ces mappings initiaux devront être affinés par vos analyses et éventuellement complétés par d'autres sources de données.

### Structure du Dataset Spotify

Le dataset Spotify contient les colonnes suivantes :

- **genre** (string) : Le genre musical associé au morceau
- **artist_name** (string) : Le nom de l'artiste
- **track_name** (string) : Le nom du morceau
- **track_id** (string) : L'identifiant Spotify du morceau
- **popularity** (int) : Score de popularité de 0 à 100
- **acousticness** (float) : Mesure de 0 à 1 indiquant si la chanson est acoustique
- **danceability** (float) : Mesure de 0 à 1 indiquant si la chanson est adaptée à la danse
- **duration_ms** (int) : Durée du morceau en millisecondes
- **energy** (float) : Mesure de 0 à 1 représentant l'intensité perceptible
- **instrumentalness** (float) : Mesure de 0 à 1 prédisant si un morceau ne contient pas de voix
- **key** (int) : La tonalité du morceau
- **liveness** (float) : Mesure de 0 à 1 indiquant la probabilité que le morceau ait été enregistré en présence d'un public
- **loudness** (float) : Le volume global d'un morceau en décibels (dB)
- **mode** (int) : Modalité (majeur = 1, mineur = 0) du morceau
- **speechiness** (float) : Mesure de 0 à 1 détectant la présence de paroles
- **tempo** (float) : Le tempo estimé en battements par minute (BPM)
- **time_signature** (int) : Une estimation de la signature rythmique
- **valence** (float) : Mesure de 0 à 1 décrivant la positivité musicale transmise par un morceau

### API Complémentaires

- **Last.fm** : Permet d'obtenir des tags communautaires pour les artistes et les morceaux
- **Genius** : Permet d'obtenir les paroles des chansons pour analyse textuelle
- **MusicBrainz** : Fournit des métadonnées détaillées sur les morceaux et les artistes
- **Spotify Web API** : Permet d'obtenir des informations supplémentaires comme les artistes similaires, les pochettes d'album, etc.

L'utilisation combinée de ces sources vous permettra d'enrichir significativement vos données et d'améliorer la pertinence de vos recommandations.
