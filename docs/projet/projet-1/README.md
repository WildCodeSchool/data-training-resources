---
title: Projet 1
description: 'SQL & BI - Toys & Models'
layout: tic-tac
---

# Introduction

![Header](assets/image/header.PNG)
{: .text-center }

Vous êtes mandaté par une entreprise qui vend des modèles et des maquettes.

L'entreprise possède déjà une base de données qui répertorie les employés, les produits, les commandes et bien plus encore. Vous êtes invité à explorer et découvrir cette base de données.

**Le directeur de l'entreprise souhaite avoir un tableau de bord qu'il pourrait actualiser chaque matin pour obtenir les dernières informations afin de gérer l'entreprise.**

# Objectif & Enjeux

Votre tableau de bord doit s'articuler autour de ces 4 sujets principaux : **ventes**, **finances**, **logistique**, et **ressources humaines**.
Les **indicateurs clés de performance** (**KPI**) ci-dessous sont requis pour ce tableau de bord, avec une distinction claire entre les priorités définies par le client :

- Rouge : <span style="color:red">Indicateurs obligatoires</span>
- Vert : <span style="color:green">Indicateurs complémentaires</span>
- Noir : <span style="color:black">Indicateur optionnels</span>

Il est recommandé de **proposer des KPI supplémentaires**, surtout en cas d’impossibilité technique de répondre à certaines demandes. Cette partie est essentielle pour démontrer votre créativité et vos compétences en tant que data analyst.

- <u><b>Ressources humaines</b></u> :
  - <span style="color:red">Performance des représentants commerciaux</span>

    <span style="color:red">Mesurer le chiffre d'affaires généré par chaque employé chargé des ventes.</span>

  - <span style="color:green">Ratio commandes/paiements par représentant commercial :</span>

    <span style="color:green">Identifier les écarts entre les commandes passées et les paiements reçus pour chaque représentant.</span>

  - <span style="color:black">Performance des bureaux</span> :

    <span style="color:black">Mesurer le chiffre d'affaire généré par chaque bureau.</span>

- <u><b>Ventes</b></u> :
  - <span style="color:red">Chiffre d'affaires par mois et par région + taux d'évolution mensuel</span> :

    <span style="color:red">Suivre les revenus générés par région et par mois pour identifier les tendances géographiques.</span>

  - <span style="color:red">Produits les plus/moins vendus par catégorie</span> :

    <span style="color:red">Identifier les produits les plus performants dans chaque catégorie.</span>

  - <span style="color:green">La marge brute par produit et par catégorie</span> :

    <span style="color:green">Mesurer la marge brute et en déduire les produits/catégories les plus/moins rentable.</span>

  - <span style="color:green">Taux d'évolution mensuel des ventes par catégorie</span> :

    <span style="color:green">Mesurer la performance de chaque catégorie de produit dans le temps.</span>

  - <span style="color:black">Panier moyen</span> :

    <span style="color:black">Mesurer le panier moyen des commandes.</span>

  - <span style="color:black">Taux de retour des clients (repeat customers)</span> :

    <span style="color:black">Mesurer la fidélité des clients en identifiant ceux qui passent plusieurs commandes.</span>

- <u><b>Finances</b></u> :
  - <span style="color:red">Clients générant le plus/moins de revenus</span> :

    <span style="color:red">Identifier les clients générant le plus de revenus pour mieux les fidéliser.</span>

  - <span style="color:green">Taux de recouvrement des créances par client</span> :

    <span style="color:green">Identifier les clients ayant un montant élevé de commandes non payées.</span>

  - <span style="color:green">Croissance des ventes par trimestre</span> :

    <span style="color:green">Identifier les tendances saisonnières ou les opportunités de croissance.</span>

  - <span style="color:black">Montant moyen des paiements + clients en dessous de la moyenne</span> :

    <span style="color:black">Évaluer la capacité de paiement des clients.</span>

  - <span style="color:black">Taux de paiement par délai</span> :

    <span style="color:black">Identifier combien de temps les clients mettent pour payer après une commande.</span>

- <u><b>Logistique</b></u> :

  - <span style="color:red">Stock des produits sous seuil critique</span> :

    <span style="color:red">Identifier les produits dont le stock est faible pour éviter les ruptures.</span>

  - <span style="color:green">Durée moyenne de traitement des commandes + commandes au-dessus de la moyenne de livraison</span> :

    <span style="color:green">Mesurer l’efficacité opérationnelle en analysant le temps entre la date de commande et la date d’expédition.</span>

  - <span style="color:green">Taux d’écoulement des stocks</span> :

    <span style="color:green">Mesurer la rapidité avec laquelle les stocks sont vendus pour chaque produit.</span>

  - <span style="color:black">Taux de commandes livrées en retard</span> :

    <span style="color:black">Identifier les problèmes logistiques et améliorer les délais de livraison.</span>

Il arrive parfois que certains indicateurs métiers ne soient pas réalisables techniquement. C'est à vous d'expliquer pourquoi et de proposer vos propres idées pour répondre aux besoins métiers.

**Note importante** : Les stocks sont mis à jour tous les deux mois. Par conséquent, les données actuelles reflètent uniquement les deux derniers mois.
{: .alert-info }

Si des limitations techniques empêchent de répondre à certains KPI, proposez des alternatives alignées avec les objectifs métiers du client.
{: .alert-warning }

# Ressources

Voici le schéma de la base de données :

![Diagram](assets/image/diagram.PNG)
{: .text-center }

# Outils

Le directeur ne souhaite pas travailler avec SQL mais veut accéder aux données automatiquement et graphiquement. Vous pouvez proposer l'outil de votre choix (Power BI, Tableau, etc.), tant que le tableau de bord est pertinent.

À titre d'information, la base de données est disponible sur un serveur de l'entreprise. Vous y accédez en mode lecture seule avec un compte utilisateur fourni.

L'entreprise vous fournit également le script que vous pouvez exécuter sur votre serveur MySQL local. Les données sont identiques et s'arrêtent à la fin du mois précédent.

# Base de données SQL

Vous avez le choix entre vous connecter au serveur cloud ou déployer le script localement. Les données sont identiques dans les deux cas.

## Installation locale

Vous pouvez installer un serveur MySQL Community sur votre machine, ainsi que le client MySQL Workbench. La base de données est prête à être chargée dans un serveur MySQL. Connectez-vous à votre serveur via Workbench, et exécutez [tout le code dans ce fichier](https://drive.google.com/file/d/103Qm2gwiTkRFlHH4Sn-dOSAW97b8zX8U/view?usp=sharing).

## Serveur cloud

Vous pouvez vous connecter au serveur MariaDB (un fork de MySQL) de l'entreprise.

- **Hostname**: **51.178.25.157**
- **Port**: **23456**
- **Username**: **toyscie**
- **Password**: **WILD4Rdata!**

# Connexion avec MySQL Workbench

![MySQL_Connect](assets/image/mysql_connection.PNG)
{: .text-center }

# Livrable attendu

Vous donnerez une courte présentation de votre tableau de bord (demandez à votre formateur la durée). La présentation doit inclure :

- **Vue d'ensemble du contexte, présentation de l'équipe et des outils utilisés.**
- **Démonstration de votre tableau de bord, et interprétation des KPI métiers.**
- **Difficultés rencontrées et perspectives d'évolution.**

**N'hésitez pas à créer des KPI supplémentaires !**