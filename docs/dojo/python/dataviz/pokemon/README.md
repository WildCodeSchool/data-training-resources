---
title: Dojo Pokémon
description: 'Analyse de données Pokémon - Matplotlib & Seaborn'
layout: default
---

# Introduction

![Header](assets/header.PNG)
{: .text-center }

Dans cet exercice, vous allez travailler avec [un dataset](https://drive.google.com/file/d/1SJMVSAIc-5TevEW8zXkh8DN6ccqXWjXL/view?usp=drive_link) contenant des informations sur les Pokémon. Le but est d’analyser ce dataset, d’identifier des KPI (Indicateurs Clés de Performance) pertinents, et de créer des visualisations claires et informatives à l’aide des bibliothèques **Matplotlib** ou **Seaborn**.

# Objectif & Enjeux

Votre objectif est de répondre à des questions spécifiques sur les Pokémon en utilisant les données et de proposer des indicateurs clés à travers des visualisations.

## Dataset

Le dataset comprend les colonnes suivantes :

- **nom** : Le nom du Pokémon
- **type1** et **type2** : Les types principaux et secondaires du Pokémon (ex. : Feu, Eau)
- **total** : La somme des statistiques du Pokémon
- **hp** : Points de vie du Pokémon
- **attack** : Statistique d’attaque physique
- **defense** : Statistique de défense physique
- **attack spe** : Statistique d’attaque spéciale
- **def spe** : Statistique de défense spéciale
- **speed** : Vitesse du Pokémon
- **generation** : Génération à laquelle appartient le Pokémon
- **legendary** : Si le Pokémon est légendaire ou non (booléen)

# Étapes de l'exercice

## 1. Analyse des données

- Explorez les données et familiarisez-vous avec les colonnes et statistiques.
- Identifiez les éléments intéressants à analyser en fonction de la question à répondre (ex: Quels sont les Pokémon les plus puissants ? Comment la génération influence-t-elle les statistiques ?)

## 2. Identification des KPI

En fonction de la question ou problématique chosiie, identifiez des KPI pertinents. Quelques exemples :

- La moyenne des statistiques par type de Pokémon
- Le pourcentage de Pokémon légendaires par génération.
- La répartition des types de Pokémon
- Comparaison des statistiques d'attaque et de défense selon les générations.

## 3. Visualisations

Utilisez **Matplotlib** ou **Seaborn** pour créer des graphiques mettant en évidence vos KPI. Exemples de visualisations possibles :

- **Boxplot** pour comparer les attaques ou défenses des Pokémon légendaires et non légendaires.
- **Barplot** pour visualiser la distribution des types de Pokémon par génération.
- **Heatmap** pour analyser les corrélations entre les différentes statistiques.
- **Histogramme** pour visualiser la répartition des Pokémon selon leurs points de vie.

# Interprétation des résultat

- Une fois les KPI identifiés et les graphiques réalisés, interprétez vos résultats en fonction de la problématique choisie.
- Expliquez comment vos visualisations aident à comprendre les tendances ou particularités des données.