---
title: Projet 2
description: 'Système de recommandation de films'
layout: default
---

## Introduction

![Header](assets/image/header.PNG)
{: .text-center }

« [Netflix](https://fr.wikipedia.org/wiki/Netflix) est un service de diffusion en streaming qui permet à ses membres de regarder une grande variété de séries TV, films, documentaires, etc. sur des milliers d'appareils connectés à Internet. »

Créé en 1998, Netflix pèse aujourd'hui plus de 20 milliards de dollars de chiffre d'affaires et consomme 12,6% de la bande passante Internet mondiale.

Au cœur de l'expérience Netflix se trouve son système de recommandation sophistiqué qui suggère de nouveaux contenus aux utilisateurs et personnalise leur page d'accueil. Ce système analyse non seulement l'historique de visionnage, mais également les caractéristiques détaillées des films, créant ainsi une expérience personnalisée pour chaque utilisateur. Netflix calcule la probabilité que l'utilisateur regarde un titre donné du catalogue, et peut ainsi optimiser ses partenariats ou plus globalement sa stratégie marketing. Netflix est l'archétype de la société *data-driven*.

**Votre client n'est pas Netflix, mais il a des ambitions cinématographiques significatives !**

## Objectif & Enjeux

Vous êtes un Data Analyst freelance. Un cinéma en perte de vitesse situé en France vous contacte. Il a décidé de passer le cap du digital en créant un site Internet adapté aux cinéphiles français.

Pour aller encore plus loin, il vous demande de développer trois fonctionnalités principales :

1. **Film-to-Film** : Recommander des films similaires à partir d'un film sélectionné par l'utilisateur
2. **Mood-to-Film** : Suggérer des films adaptés à l'humeur exprimée par l'utilisateur (joyeux, mélancolique, motivant, etc.)
3. **Group-to-Film** : Proposer un film qui conviendrait à un groupe de personnes aux préférences variées

Pour l'instant, aucun client n'a renseigné ses préférences, **vous êtes dans une situation de cold start**. Mais heureusement, le client vous donne accès à une base de données de films basée sur la plateforme IMDb.

Commencez par une étude de marché sur la consommation de cinéma en France, afin de mieux comprendre les attentes et les préférences du public national. Cette étape préliminaire vous permettra de définir une orientation adaptée pour la suite de l'analyse de votre base de données.

Après cette étude, réalisez une analyse approfondie de votre base de données pour identifier des tendances et caractéristiques spécifiques. Cette analyse devrait inclure : l'identification des acteurs les plus présents et les périodes associées, l'évolution de la durée moyenne des films au fil des années, la comparaison entre les acteurs présents au cinéma et dans les séries, l'âge moyen des acteurs, ainsi que les films les mieux notés et les caractéristiques qu'ils partagent.

Sur la base de ces informations, vous pourrez affiner vos recommandations pour mieux répondre aux attentes du public identifié lors de l'étude de marché.

## Objectif & Enjeux (suite)

![ML Logo](assets/image/sci-kit_learn_logo.PNG)
{: .text-center }

Après cette étape analytique, vous utiliserez des **algorithmes de machine learning** pour développer les trois fonctionnalités de recommandation demandées.

Le client vous fournit également une base de données complémentaire venant de [TMDB](https://www.themoviedb.org/), contenant des données sur les pays des boîtes de production, le budget, les recettes et également un chemin vers les posters des films. Il vous est demandé de [récupérer les images](https://developer.themoviedb.org/docs/image-basics) des films pour les afficher dans votre interface de recommandation.

**Attention !** L'objectif n'est pas de diffuser dans le cinéma les films recommandés. L'objectif final est de développer un prototype fonctionnel du système de recommandation qui pourra être mis à disposition des clients du cinéma afin de leur proposer un service supplémentaire, en ligne, en plus du cinéma classique. Votre prototype devra inclure une interface permettant de tester les trois fonctionnalités principales et de visualiser des KPI pertinents.

## Ressources

Les données sont disponibles sur le site IMDb, réparties en plusieurs tables (films, acteurs, réalisateurs, notes, etc.).

- [Documentation des colonnes et tables](https://www.imdb.com/interfaces/)
- [Datasets IMDb](https://datasets.imdbws.com/)
- [Dataset complémentaire TMDB](https://drive.google.com/file/d/1VB5_gl1fnyBDzcIOXZ5vUSbCY68VZN1v/view?usp=sharing)

## Remarques Techniques

- Vous pouvez télécharger les datasets en local, sur votre Drive ou bien sur un GitHub. L'utilisation d'un dépôt GitHub est fortement recommandée pour faciliter la collaboration entre les membres du binôme.
- Les datasets sont très volumineux, il y a plus de 7M films et 10M acteurs référencés. Pensez à échantillonner judicieusement les données pour vos tests initiaux, puis à étendre progressivement votre analyse.
- Pour rappel, Google Colab propose des serveurs "partagés". Les performances dépendent donc du nombre de personnes connectées en même temps. Parfois, vous ne pourrez donc pas charger tous ces volumineux datasets. N'hésitez pas à les traiter en local grâce à Anaconda / Jupyter.
- Les datasets IMDB sont au format TSV, pour "Tabulation Separated Values". C'est similaire au format CSV, mais séparé par des tabulations plutôt que des virgules. Vous pouvez utiliser la fonction suivante, qui indique que le séparateur est une tabulation : `pd.read_csv("dataset_link", sep = "\t", nrows=1000)`
- Pour l'enrichissement des données avec des tags d'humeur et pour la fonctionnalité Group-to-Film, plusieurs approches sont possibles :
  - **Text Mining** sur les synopsis des films (via TMDB API)
  - **Analyse de clustering** sur les caractéristiques des films pour identifier des groupes naturels
  - **Transfer Learning** à partir de bases de données existantes
  - **Crowdsourcing** : création d'un mini-système d'annotation manuelle pour un échantillon de films
- Pour la gestion collaborative du projet, utilisez les fonctionnalités de GitHub :
  - Branches pour les développements parallèles
  - Pull requests pour la revue de code
  - Issues pour le suivi des tâches et des bugs
  - Projects pour la planification agile

## Organisation et Planning

Ce projet se déroulera sur 7 semaines, en binôme. Voici un planning indicatif, que vous pouvez adapter selon vos contraintes et votre progression :

1. **Semaine 1** : Mise en place de l'environnement collaboratif (GitHub), étude de marché sur la consommation de cinéma en France (CNC, Insee)
2. **Semaine 2** : Exploration initiale des datasets et apprentissage des jointures entre tables
3. **Semaine 3** : Analyse approfondie des données et nettoyage (Pandas, Matplotlib, Seaborn)
4. **Semaine 4** : Développement de stratégies d'enrichissement pour les tags d'humeur et préférences de groupe
5. **Semaine 5** : Implémentation des algorithmes de recommandation pour les trois fonctionnalités
6. **Semaine 6** : Création de l'interface utilisateur pour tester les recommandations et affiner les algorithmes
7. **Semaine 7** : Finalisation, tests utilisateurs, documentation et préparation de la présentation

**Points d'attention pour la collaboration en binôme :**
- Répartissez clairement les responsabilités entre les membres de l'équipe
- Organisez des points réguliers pour synchroniser vos avancées
- Documentez vos choix techniques et vos hypothèses dans le README du projet
- Utilisez des conventions de nommage et de codage cohérentes
- Pratiquez la revue de code mutuelle avant chaque fusion dans la branche principale

## Besoins Clients

Le client a besoin d'un prototype fonctionnel qui démontre l'efficacité des trois systèmes de recommandation. Pour répondre à ce besoin, vous développerez une application simple mais complète qui permet de :

- Rechercher un film et obtenir des recommandations de films similaires (Film-to-Film)
- Sélectionner une humeur et générer des suggestions de films adaptés (Mood-to-Film)
- Entrer les préférences de plusieurs personnes et obtenir une recommandation de film pour le groupe (Group-to-Film)
- Visualiser des statistiques pertinentes sur les recommandations et le dataset (KPI)

Vous pouvez implémenter cette interface au moyen d'un outil de votre choix :
- Une application web (Flask, Streamlit, Dash)
- Un notebook interactif (Jupyter avec widgets)
- Une application desktop simple (PyQt, Tkinter)
- Un outil de business intelligence pour les visualisations (PowerBI, Tableau)

L'objectif n'est pas d'avoir une interface parfaite d'un point de vue esthétique, mais fonctionnelle et permettant de démontrer la pertinence de vos algorithmes de recommandation.

## Missions et Livrables Attendus

### Missions

- Réaliser une présentation synthétique de votre démarche, des méthodes d'enrichissement utilisées, des algorithmes de recommandation choisis, et des résultats obtenus.
- Présenter des indicateurs statistiques et KPI pertinents sur les films et la qualité des recommandations.
- Faire une démonstration en direct des trois fonctionnalités de recommandation, en utilisant des exemples proposés par le client.

### Livrables

- Un dépôt GitHub complet contenant l'ensemble du code source, bien documenté et organisé.
- Des notebooks détaillant l'exploration des données, l'enrichissement avec les tags d'humeur, et le développement des algorithmes de recommandation.
- Un rapport technique expliquant vos choix méthodologiques, les difficultés rencontrées et les pistes d'amélioration futures.
- Le prototype fonctionnel du système de recommandation avec son interface utilisateur.
- Un guide d'utilisation pour permettre au client de tester le prototype de manière autonome.

## Documentation

### Enrichissement des Données

L'un des défis majeurs de ce projet est l'enrichissement des données pour les fonctionnalités Mood-to-Film et Group-to-Film qui ne sont pas explicitement présentes dans les datasets originaux. Voici une méthodologie pour aborder ce problème :

#### Méthodologie d'enrichissement :

1. **Étude préliminaire et recherche** :
   - Recherchez des études existantes sur la perception émotionnelle des films
   - Explorez la littérature sur la relation entre genres cinématographiques et émotions
   - Analysez comment d'autres services de streaming catégorisent leurs contenus

2. **Analyse exploratoire des données** :
   - Examinez la distribution des caractéristiques des films (genres, durée, année, notes)
   - Identifiez des corrélations entre ces caractéristiques
   - Visualisez des clusters naturels dans les données

3. **Définition des catégories d'humeur et de préférences de groupe** :
   - Établissez une liste d'humeurs principales pertinentes pour votre application
   - Définissez les critères qui pourraient influencer les choix d'un groupe
   - Réfléchissez aux chevauchements possibles entre certaines catégories

4. **Élaboration des règles de classification** :
   - Pour chaque humeur, réfléchissez aux caractéristiques de films qui pourraient y être associées
   - Créez des règles combinant plusieurs caractéristiques (genres, acteurs, périodes)
   - Testez vos règles sur un échantillon de films connus pour vérifier leur pertinence

5. **Validation et itération** :
   - Testez vos classifications sur un petit panel d'utilisateurs
   - Ajustez vos règles en fonction des retours
   - Envisagez des approches plus avancées (apprentissage supervisé) si nécessaire

#### Questions à vous poser :

- Quels genres cinématographiques sont typiquement associés à certaines humeurs?
- Comment les critiques et notes influencent-elles la perception émotionnelle d'un film?
- Quels critères sont importants dans le choix d'un film pour un groupe (durée, accessibilité, diversité des thèmes)?
- Comment gérer les cas ambigus ou les films qui pourraient appartenir à plusieurs catégories d'humeur?
- Quelles sources externes pourraient vous aider à valider vos classifications?

L'objectif est de développer votre propre système de classification basé sur une réflexion approfondie et des tests empiriques, plutôt que d'utiliser des règles prédéfinies. Cette approche vous permettra de mieux comprendre les nuances de la perception cinématographique et d'affiner continuellement votre système.

### IMDb Dataset Details

Each dataset is contained in a gzipped, tab-separated-values (TSV) formatted file in the UTF-8 character set. The first line in each file contains headers that describe what is in each column. A '\N' is used to denote that a particular field is missing or null for that title/name. The available datasets are as follows:

title.akas.tsv.gz - Contains the following information for titles:
- titleId (string) - a tconst, an alphanumeric unique identifier of the title
- ordering (integer) – a number to uniquely identify rows for a given titleId
- title (string) – the localized title
- region (string) - the region for this version of the title
- language (string) - the language of the title
- types (array) - Enumerated set of attributes for this alternative title. One or more of the following: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay". New values may be added in the future without warning
- attributes (array) - Additional terms to describe this alternative title, not enumerated
- isOriginalTitle (boolean) – 0: not original title; 1: original title

title.basics.tsv.gz - Contains the following information for titles:
- tconst (string) - alphanumeric unique identifier of the title
- titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
- primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
- originalTitle (string) - original title, in the original language
- isAdult (boolean) - 0: non-adult title; 1: adult title
- startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
- endYear (YYYY) – TV Series end year. '\N' for all other title types
runtimeMinutes – primary runtime of the title, in minutes
- genres (string array) – includes up to three genres associated with the title

title.crew.tsv.gz – Contains the director and writer information for all the titles in IMDb. Fields include:
- tconst (string) - alphanumeric unique identifier of the title
- directors (array of nconsts) - director(s) of the given title
- writers (array of nconsts) – writer(s) of the given title

title.episode.tsv.gz – Contains the tv episode information. Fields include:
- tconst (string) - alphanumeric identifier of episode
- parentTconst (string) - alphanumeric identifier of the parent TV Series
- seasonNumber (integer) – season number the episode belongs to
- episodeNumber (integer) – episode number of the tconst in the TV series

title.principals.tsv.gz – Contains the principal cast/crew for titles
- tconst (string) - alphanumeric unique identifier of the title
- ordering (integer) – a number to uniquely identify rows for a given titleId
- nconst (string) - alphanumeric unique identifier of the name/person
- category (string) - the category of job that person was in
- job (string) - the specific job title if applicable, else '\N'
- characters (string) - the name of the character played if applicable, else '\N'

title.ratings.tsv.gz – Contains the IMDb rating and votes information for titles
- tconst (string) - alphanumeric unique identifier of the title
- averageRating – weighted average of all the individual user ratings
- numVotes - number of votes the title has received

name.basics.tsv.gz – Contains the following information for names:
- nconst (string) - alphanumeric unique identifier of the name/person
- primaryName (string)– name by which the person is most often credited
- birthYear – in YYYY format
- deathYear – in YYYY format if applicable, else '\N'
- primaryProfession (array of strings)– the top-3 professions of the person
- knownForTitles (array of tconsts) – titles the person is known for

### TMDB Dataset Details

- adult : Un champ indiquant si le film est destiné à un public adulte, avec les valeurs "true" ou "false".
- backdrop_path : Le chemin d'accès à l'image de fond associée au film, utilisée à des fins de marketing et de promotion.
- budget : Le budget du film, généralement en dollars ou dans la devise de référence.
- genres : Les genres du film, tels que "Action," "Comedy," "Science Fiction," etc.
- homepage : L'URL de la page d'accueil officielle du film.
- id : L'ID du film dans la base de données TMDB, utilisé pour identifier de manière unique chaque film.
- imdb_id : L'ID IMDB du film, un identifiant unique dans la base de données IMDB.
- original_language : La langue originale du film.
- original_title : Le titre original du film dans sa langue d'origine.
- overview : Une brève description ou un résumé du film.
- popularity : Un indicateur de la popularité du film.
- poster_path : Le chemin d'accès à l'affiche du film, utilisée à des fins de marketing.
- production_countries : Les pays de production du film, avec la possibilité d'avoir plusieurs pays listés.
- release_date : La date de sortie du film.
- revenue : Le chiffre d'affaires généré par le film, généralement en dollars ou dans la devise de référence.
- runtime : La durée en minutes du film.
- spoken_languages : Les langues parlées dans le film.
- status : Le statut du film, par exemple, "Released" ou "In Production".
- tagline : Une phrase ou un slogan court résumant le film, utilisée à des fins marketing.
- title : Le titre du film.
- video : Un indicateur booléen indiquant si le film a une bande-annonce vidéo ("true" ou "false").
- vote_average : La note moyenne attribuée au film par les utilisateurs ou les critiques.
- vote_count : Le nombre de votes ou de critiques reçus par le film.
- production_companies_name : Le nom des sociétés de production associées au film.
- production_companies_country : Le pays d'origine des sociétés de production associées au film.
