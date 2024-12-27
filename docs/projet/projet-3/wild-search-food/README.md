---
title: Wild Search Food
description: ' '
layout: default
---

## Introduction et Contexte

![Header](assets/image/gras.jpeg)
{: .text-center }

Le projet **WildSearchFood** vise à fournir une solution innovante pour l’analyse et la recherche de restaurants en combinant des données issues d’APIs comme Yelp avec des sources Open Data. Ce projet répond aux besoins des utilisateurs en matière de recherche personnalisée, d’analyse des avis clients, et de visualisation des tendances sous forme de dashboards interactifs.

## Objectifs Pédagogiques

- Comprendre et utiliser les techniques de collecte de données via APIs comme Yelp.
- Maîtriser le prétraitement et le nettoyage de données JSON avec Python et ses bibliothèques associées.
- Concevoir et déployer un pipeline ETL efficace en utilisant Mage AI.
- Gérer les données dans une base PostgreSQL locale ou hébergée.
- Créer des dashboards dynamiques pour des visualisations interactives des données.
- Implémenter des fonctionnalités IA pour enrichir l’analyse des restaurants et des avis clients.

## Organisation

Le projet se déroule en plusieurs phases organisées de manière itérative et collaborative sur une durée de 4 semaines :

1. Collecte des Données via API.
2. Prétraitement et Nettoyage des Données.
3. Base de Données et ETL.
4. Visualisation et Dashboard.
5. Interface Utilisateur.
6. Fonctionnalités IA (optionnelles).

## Phases de Développement

1. Collecte des Données via API

    - **Technologies** : Python, API Yelp, APIs Open Data.
    - **Objectif** :
    - Récupérer les données des restaurants (informations, notes, commentaires) via l’API Yelp (300 requêtes/jour gratuites).
    - Enrichir les données avec des sources Open Data.
    - **Lien avec l’étape suivante** : Les données brutes au format JSON sont transmises au processus de nettoyage pour structuration.

2. Prétraitement et Nettoyage des Données

    - **Technologies** : Python, pandas, datetime, re, json.
    - **Objectif** :
    - Nettoyer et structurer les données JSON.
    - Extraire les informations pertinentes et standardiser les formats pour faciliter leur exploitation.
    - **Lien avec l’étape suivante** : Les données nettoyées sont préparées pour le chargement dans une base de données via une brique ETL.

3. Base de Données et ETL

    - **Technologies** : Mage AI (ETL), PostgreSQL (local), PostgreSQL (Cloud, optionnel).
    - **Objectif** :
    - Utiliser Mage AI pour orchestrer les processus d’Extraction, Transformation et Chargement des données (ETL).
    - Stocker les données nettoyées et structurées dans une base PostgreSQL.
    - **Lien avec l’étape suivante** : La base de données alimente les dashboards interactifs et l'interface utilisateur.

4. Visualisation et Dashboard

    - **Technologies** : Streamlit, bibliothèques de visualisation (plotly, etc.), PowerBI.
    - **Objectif** :
    - Créer des dashboards dynamiques et interactifs comprenant :
        - Notes moyennes des restaurants.
        - Scatter plots (prix vs qualité).
        - Word clouds des commentaires.
        - Cartographie des résultats.
    - **Lien avec l’étape suivante** : Les visualisations sont intégrées dans l'interface utilisateur finale.

5. Interface Utilisateur

    - **Technologies** : Streamlit.
    - **Objectif** :
    - Développer une interface utilisateur innovante permettant :
        - Recherche personnalisée de restaurants.
        - Génération automatique de dashboards.
        - Sauvegarde des recherches et visualisations.

6. Fonctionnalités IA (Optionnelles)

    - **Technologies** : Gemini API, modèles de langage.
    - **Objectifs** :
    - Topic modeling sur les descriptions de restaurants.
    - Analyse d’images pour décrire le cadre des restaurants.
    - Traitement avancé des avis clients.

## Missions et Livrables Attendus

- Scripts Python pour la collecte et l’extraction des données via API.
- Codes de traitement et nettoyage des données JSON.
- Pipeline ETL fonctionnel déployé sur Mage AI.
- Base de données PostgreSQL contenant des données nettoyées et mises à jour.
- Dashboards interactifs présentant les analyses et visualisations des données.
- Interface utilisateur déployée sur Streamlit.

## Ressources

- [Documentation sur l’API Yelp](https://docs.developer.yelp.com/docs/fusion-intro)
- [Streamlit](https://www.youtube.com/@CodingIsFun/playlists)
- [Dash](https://www.youtube.com/@CharmingData)
