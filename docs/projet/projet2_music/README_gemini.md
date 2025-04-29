---
title: Projet 3 - Recommandation Musicale Intelligente
description: 'Système de recommandation de chansons et de génération de playlists par humeur/activité'
layout: default
---

## Introduction

![Spotify Logo](assets/image/spotify_logo.png) 
{: .text-center }

« [Spotify](https://fr.wikipedia.org/wiki/Spotify) est un service de streaming musical qui permet aux utilisateurs d'écouter des millions de chansons, podcasts et vidéos d'artistes du monde entier. »

Lancé en 2008, Spotify domine le marché du streaming musical, non seulement par son catalogue gigantesque mais aussi par sa capacité à proposer des découvertes musicales personnalisées grâce à des algorithmes sophistiqués. La recommandation est au cœur de l'expérience utilisateur, permettant de découvrir de nouveaux titres, artistes ou de créer des playlists adaptées à chaque moment.

**Votre client est une jeune startup ambitieuse, "MelodyMind", qui souhaite créer une nouvelle expérience d'écoute personnalisée.**

## Objectif & Enjeux

![Mood Playlist Concept](assets/image/playlist_mood.png) 
{: .text-center }

Vous travaillez en binôme comme Data Analysts pour MelodyMind. La startup veut développer un service innovant permettant aux utilisateurs non seulement d'obtenir des recommandations basées sur une chanson qu'ils aiment, mais aussi de générer des playlists correspondant à leur **humeur** (joyeux, triste, relaxé...) ou à leur **activité** (sport, concentration, soirée...).

Le défi principal réside dans le fait que les datasets musicaux standards, comme ceux issus de Spotify, contiennent principalement des métadonnées factuelles (artiste, album, titre) et des caractéristiques audio techniques (tempo, énergie, valence, etc.). Ils n'incluent **pas directement d'informations sur l'humeur ou l'activité associées aux chansons**.

Votre première tâche sera donc d'explorer un dataset Spotify pour comprendre les caractéristiques disponibles. Ensuite, une partie cruciale du projet consistera à **rechercher et mettre en œuvre des stratégies pour enrichir vos données**, afin de pouvoir prédire ou associer des humeurs et activités aux chansons.

Ce projet doit être mené en **collaboration étroite au sein de votre binôme**, en utilisant **GitHub** pour le versionnement du code, le partage des tâches et la gestion de projet. Une bonne organisation et communication seront essentielles.

## Objectif & Enjeux (suite)

![Data Enrichment Concept](assets/image/data_enrichment.png) 
{: .text-center }

Après l'exploration et surtout l'**enrichissement des données**, vous développerez des **algorithmes de machine learning** pour répondre aux deux besoins principaux de MelodyMind :

1.  **Recommandation Chanson-à-Chanson :** Proposer des chansons similaires à une chanson donnée par l'utilisateur. Vous pourrez vous baser sur les métadonnées et/ou les caractéristiques audio.
2.  **Génération de Playlists Humeur/Activité :** Créer une playlist pertinente lorsqu'un utilisateur spécifie une humeur ou une activité. Cela nécessitera d'exploiter les données enrichies que vous aurez créées.

L'objectif final est de livrer un prototype fonctionnel démontrant ces deux capacités, potentiellement via une interface simple ou un outil de dashboarding.

**Comment enrichir les données ? (Pistes à explorer)**

*   **Utiliser les caractéristiques audio :** Certaines features comme la `valence` (positivité musicale), l'`energy` ou le `tempo` peuvent être de bons indicateurs indirects de l'humeur ou de l'énergie d'une activité. Vous pourriez définir des seuils ou utiliser des modèles de clustering.
*   **Analyse de texte (NLP) :** Si vous trouvez des paroles de chansons, une analyse de sentiments pourrait aider à déterminer l'humeur.
*   **Mapping de genres :** Certains genres sont plus typiquement associés à certaines humeurs ou activités (ex: musique classique pour la concentration, EDM pour le sport).
*   **Datasets externes ou APIs :** Rechercher des bases de données existantes qui lient chansons et tags d'humeur/activité (ex: Last.fm tags, si accessibles).
*   *Approche créative :* Vous pourriez même envisager de créer un petit set de données annotées manuellement pour entraîner un modèle simple.

## Ressources

Un dataset courant et riche pour ce type de projet est disponible sur Kaggle. Vous pouvez également explorer l'API Web de Spotify pour obtenir des données plus spécifiques ou à jour, si vous le souhaitez.

*   **Dataset Spotify sur Kaggle (Exemple) :** [Spotify Tracks DB](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db) (ou un dataset similaire de votre choix)
*   **Documentation des Caractéristiques Audio Spotify :** [Spotify API Documentation - Audio Features](https://developer.spotify.com/documentation/web-api/reference/get-audio-features)
*   **Gestion de Projet Collaboratif :** Guides et bonnes pratiques pour l'utilisation de GitHub en équipe (Branches, Pull Requests, Issues).

## Remarques Techniques

*   **Collaboration sur GitHub :** Organisez votre travail en binôme sur un dépôt GitHub partagé. Utilisez des branches pour développer de nouvelles fonctionnalités, faites des Pull Requests pour revoir le code de votre partenaire, et utilisez les Issues pour suivre les tâches.
*   **Gestion des Données :** Les datasets peuvent être volumineux. Pensez à filtrer, échantillonner ou à sauvegarder des versions nettoyées/enrichies pour accélérer le chargement et le traitement.
*   **Enrichissement des Données :** C'est un point clé et ouvert. Documentez bien votre démarche, vos hypothèses et les méthodes choisies pour créer les labels d'humeur/activité.
*   **Format des Données :** Les datasets sont souvent au format CSV. Utilisez `pd.read_csv("lien_ou_chemin_dataset.csv")` pour les charger dans Pandas.
*   **Environnement :** Vous pouvez travailler en local (Anaconda/Jupyter) ou sur des plateformes cloud comme Google Colab.

## Organisation et Planning (7 Semaines - Travail en Binôme)

Voici un planning indicatif. Adaptez-le en fonction de votre rythme et de la répartition des tâches au sein du binôme :

1.  **Semaine 1 & 2 :** Mise en place de l'environnement, création du dépôt GitHub, définition des règles de collaboration, exploration initiale du dataset Spotify (Pandas, Matplotlib, Seaborn).
2.  **Semaine 3 & 4 :** Nettoyage des données, ingénierie des caractéristiques (features engineering), recherche et implémentation des **stratégies d'enrichissement** (création des labels humeur/activité). C'est une phase critique.
3.  **Semaine 5 & 6 :** Développement des modèles de **Machine Learning** (Scikit-learn) :
    *   Modèle(s) pour la recommandation chanson-à-chanson (ex: similarité cosinus sur features audio/métadonnées).
    *   Modèle(s) pour la recommandation par humeur/activité (ex: classification, clustering, filtrage basé sur les labels enrichis).
4.  **Semaine 7 :** Intégration dans un prototype/dashboard simple, tests, finalisation de la documentation, préparation de la présentation finale.

## Besoins Clients (MelodyMind)

MelodyMind souhaite pouvoir tester vos algorithmes. Comme le temps est limité, un prototype fonctionnel suffira. Vous avez le choix de l'outil pour la démonstration.

Les besoins sont :

*   **Statistiques et KPIs :** Présenter des analyses sur le dataset (ex: distribution des genres, popularité des artistes, analyse des caractéristiques audio moyennes par genre/décennie). Des visualisations claires sont attendues (Python ou outil de BI).
*   **Système de Recommandation Testable :**
    *   Une fonction/interface où l'utilisateur entre le nom d'une chanson et obtient une liste de N recommandations similaires.
    *   Une fonction/interface où l'utilisateur sélectionne une humeur ou une activité (parmi celles que vous avez définies/créées) et obtient une playlist de N chansons correspondantes.
    *   La démonstration peut se faire via un notebook interactif, une ligne de commande, ou un outil de dashboarding simple (Streamlit, Gradio, etc.).

L'objectif est d'avoir un système fonctionnel et de pouvoir discuter des choix effectués et des pistes d'amélioration.

## Missions et Livrables Attendus

### Missions

*   **Collaboration Efficace :** Démontrer une bonne gestion de projet et collaboration via GitHub (historique des commits, branches, PRs...).
*   **Analyse Exploratoire et Enrichissement :** Présenter une analyse pertinente du dataset et expliquer clairement la démarche choisie pour l'enrichissement des données (humeur/activité).
*   **Modélisation :** Implémenter et expliquer les algorithmes de recommandation choisis.
*   **Présentation Finale :** Réaliser une présentation orale synthétisant le projet : objectifs, démarche (y compris collaborative), outils, résultats, difficultés, et pistes d'amélioration.
*   **Démonstration :** Montrer le fonctionnement des deux types de recommandations sur des exemples concrets.

### Livrables

*   **Dépôt GitHub :** Un dépôt bien organisé contenant tout le code source (notebooks, scripts), les éventuels datasets nettoyés/enrichis, et un README clair. L'historique doit refléter le travail du binôme.
*   **Notebook(s) d'Analyse et Modélisation :** Un ou plusieurs notebooks Jupyter contenant :
    *   L'exploration, le nettoyage, et l'enrichissement des données (avec explications).
    *   Le développement, l'entraînement et l'évaluation des modèles de recommandation. Le code doit être commenté.
*   **Prototype/Dashboard :** L'outil choisi pour la démonstration des KPIs et des systèmes de recommandation.
*   **Support de Présentation :** Les diapositives utilisées lors de la présentation finale.

## Documentation (Exemple de Dataset Spotify Kaggle)

Voici un aperçu des colonnes *typiques* que l'on peut trouver dans un dataset Spotify sur Kaggle (le dataset exact peut varier) :

*   `track_id` (string): Identifiant unique de la chanson sur Spotify.
*   `artists` (string): Nom(s) de(s) artiste(s).
*   `album_name` (string): Nom de l'album.
*   `track_name` (string): Nom de la chanson.
*   `popularity` (integer): Score de popularité de la chanson (0-100).
*   `duration_ms` (integer): Durée de la chanson en millisecondes.
*   `explicit` (boolean): Indique si la chanson contient des paroles explicites.
*   `danceability` (float): Mesure à quel point une piste est adaptée à la danse (0.0-1.0). Basé sur le tempo, la régularité du rythme, la force du beat.
*   `energy` (float): Mesure perceptive d'intensité et d'activité (0.0-1.0). Les pistes énergiques sont rapides, bruyantes et fortes.
*   `key` (integer): Clé musicale de la piste (0=Do, 1=Do#, ..., 11=Si).
*   `loudness` (float): Volume global de la piste en décibels (dB).
*   `mode` (integer): Modalité de la piste (Majeur=1, Mineur=0).
*   `speechiness` (float): Détecte la présence de mots parlés (0.0-1.0). > 0.66 : probablement que de la parole (podcast), 0.33-0.66 : peut contenir musique et parole (rap), < 0.33 : probablement musique sans parole.
*   `acousticness` (float): Mesure de l'acousticité de la piste (0.0-1.0). 1.0 représente une forte confiance que la piste est acoustique.
*   `instrumentalness` (float): Prédit si une piste ne contient pas de voix (0.0-1.0). > 0.5 représente une piste instrumentale.
*   `liveness` (float): Détecte la présence d'un public dans l'enregistrement (0.0-1.0). > 0.8 indique une forte probabilité que la piste soit live.
*   `valence` (float): Mesure de la positivité musicale transmise par la piste (0.0-1.0). Haut = plus joyeux/euphorique, Bas = plus triste/colérique.
*   `tempo` (float): Tempo estimé en battements par minute (BPM).
*   `time_signature` (integer): Indique combien de temps contient chaque mesure (barre).

Vous devrez explorer le dataset spécifique que vous choisirez pour confirmer les colonnes exactes et leur signification. Bonne chance pour ce projet !
