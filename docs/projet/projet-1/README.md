---
title: Projet 1
description: 'SQL & BI - Toys & Models'
---

![Header](assets/image/header.PNG)
{: .text-center }

## Introduction

Vous êtes mandaté par une entreprise qui vend des modèles et des maquettes.

L’entreprise possède déjà une base de données qui répertorie les employés, les produits, les commandes et bien plus encore. Vous êtes invité à explorer et découvrir cette base de données.

**Le directeur de l’entreprise souhaite avoir un tableau de bord dynamique qu’il pourrait actualiser chaque matin pour obtenir les dernières informations afin de gérer l’entreprise.**

## Objectif & Enjeux

Votre tableau de bord doit s'articuler autour de ces 4 sujets principaux : **ventes**, **finances**, **logistique**, et **ressources humaines**.

Les **indicateurs clés de performance** (**KPI**) ci-dessous sont requis pour ce tableau de bord, avec une distinction claire entre les priorités définies par le client :

- 🔴 **Rouge** : Indicateurs obligatoires  
- 🟢 **Vert** : Indicateurs complémentaires  
- ⚫ **Noir** : Indicateurs optionnels

Il est recommandé de **proposer des KPI supplémentaires**, surtout en cas d’impossibilité technique de répondre à certaines demandes. Cette partie est essentielle pour démontrer votre créativité et vos compétences en tant que data analyst.

### I. Partie 1 : Calcul des Métriques en SQL

#### 📌 Objectif de la Partie SQL
Avant de passer à la création du tableau de bord dans Power BI, vous devez calculer toutes les métriques en SQL. Cela vous permettra de :
- Valider les calculs avant de les visualiser dans Power BI.
- Structurer les données pour faciliter leur utilisation dans Power BI.
- Optimiser les performances en évitant des calculs lourds dans Power BI.

#### Calcul des KPI en SQL
Vous devez écrire des requêtes SQL pour calculer les indicateurs suivants. Vous pouvez également ajouter des indicateurs supplémentaires si vous le souhaitez.

##### 📌 Ressources humaines
- 🔴 **Performance des représentants commerciaux** : Calculer le chiffre d’affaires généré par chaque employé chargé des ventes.
- 🟢 **Ratio commandes/paiements par représentant commercial** : Identifier les écarts entre les commandes passées et les paiements reçus pour chaque représentant.
- 🟢 **Performance des bureaux** : Mesurer le chiffre d’affaires généré par chaque bureau.

##### 📌 Ventes
- 🔴 **Chiffre d’affaires par mois et par région + taux d’évolution mensuel** : Suivre les revenus générés par région et par mois pour identifier les tendances géographiques.
- 🔴 **Produits les plus/moins vendus par catégorie** : Identifier les produits les plus performants dans chaque catégorie.
- 🟢 **La marge brute par produit et par catégorie** : Mesurer la marge brute et en déduire les produits/catégories les plus/moins rentables.
- ⚫ **Taux d’évolution mensuel des ventes par catégorie** : Mesurer la performance de chaque catégorie de produit dans le temps.
- ⚫ **Panier moyen** : Mesurer le panier moyen des commandes.
- ⚫ **Taux de retour des clients (repeat customers)** : Mesurer la fidélité des clients en identifiant ceux qui passent plusieurs commandes.

##### 📌 Finances
- 🔴 **Clients générant le plus/moins de revenus** : Identifier les clients générant le plus de revenus pour mieux les fidéliser.
- 🟢 **Taux de recouvrement des créances par client** : Identifier les clients ayant un montant élevé de commandes non payées.
- ⚫ **Croissance des ventes par trimestre** : Identifier les tendances saisonnières ou les opportunités de croissance.
- ⚫ **Montant moyen des paiements + clients en dessous de la moyenne** : Évaluer la capacité de paiement des clients.
- ⚫ **Taux de paiement par délai** : Identifier combien de temps les clients mettent pour payer après une commande.

##### 📌 Logistique
- 🔴 **Stock des produits sous seuil critique** : Identifier les produits dont le stock est faible pour éviter les ruptures.
- 🟢 **Durée moyenne de traitement des commandes + commandes au-dessus de la moyenne de livraison** : Mesurer l’efficacité opérationnelle en analysant le temps entre la date de commande et la date d’expédition.
- ⚫ **Taux d’écoulement des stocks** : Mesurer la rapidité avec laquelle les stocks sont vendus pour chaque produit.
- ⚫ **Taux de commandes livrées en retard** : Identifier les problèmes logistiques et améliorer les délais de livraison.

#### 📍 **Travail à réaliser en SQL avant l’intégration dans PowerBI :**  

Une fois vos métriques validées en SQL, vous devez les modéliser dans Power BI afin de faciliter leur transformation en graphiques interactifs.
Vos requêtes représentent ce qu’on appelle **les tables de faits**. Pour analyser ces données sous différents angles, il est nécessaire d’y associer **des tables de dimensions**.

1. Créer une ou plusieurs tables de faits
Les tables de faits centralisent les informations nécessaires au calcul des indicateurs de performance.

Par exemple, une table `fact_sales` pourrait contenir :
- **Clés étrangères** : permettant de faire le lien avec les tables de dimensions (`customer_id`, `product_id`, `employee_id`, `order_date`).
- **Identifiants** : tels que order_id pour identifier chaque commande.
- **Données analytiques** : toutes les informations permettant de réaliser des mesures (ex. `quantity_sold`, `unit_price`, `total_revenue`, `delivery_status`...).
👉 Autres exemples de tables de faits :
- `fact_payments` : regroupe les informations sur les paiements effectués par les clients.
- `fact_inventory` : contient les données liées à la logistique et à la gestion des stocks.

2. Créer des tables de dimensions.  
Les tables de dimensions stockent les informations descriptives qui permettent d’analyser les faits sous différents angles.
Exemples de tables de dimensions :
- `dim_customers` : liste des clients avec leurs informations (`customer_id`, `customer_name`, `region`, `country`...).
- `dim_products` : détails des produits (`product_id`, `product_name`, `category`, `unit_price`...).
- `dim_dates` : table calendrier permettant les analyses temporelles (`date_id`, `year`, `month`, `week`, `day`...).
Autres dimensions : `dim_employees`, `dim_offices`, `dim_managers`…

3.Créer des vues SQL
Afin de faciliter leur récupération dans Power BI, vous devez créer des vues SQL qui préparent les tables de faits et de dimensions en amont. Cela permet d’optimiser la performance et de garantir des données prêtes à l’emploi.

👉 **Exemple de structure :** 
- `fact_sales` : table de fait contenant les informations de ventes : quantité commandé, chiffre d'affaires …
- `dim_customers` : Clients (Nom, Région,...)  
- `dim_products` : Produits (Nom, Catégorie …)  
- `dim_employees` : Employés (Nom, job title,...)  
- `dim_manager` :  Managers (Nom, job title…)
- `dim_office` :  Offices ( Bureau , country…)
- `dim_dates` : Dates pour les analyses temporelles  (Peut-être faite en SQL ou sur PowerBI)

Exemple de schéma en étoile possible

![Schéma en Étoile](https://drive.google.com/file/d/1Ryyz3lSvNCS0zg4Fc_anS-2neVbpjjnb/view)

💡 **Objectif** : Avoir une structure optimisée pour Power BI afin de faciliter la création des KPI sans refaire des calculs lourds dans Power BI.

### II. Partie 2 : Construction du Dashboard dans Power BI

#### 📌 Pourquoi utiliser Power BI après SQL ?
Power BI va permettre de récupérer directement les vues SQL créées et de les utiliser comme des tables liées dans un modèle de données. Cela facilite :
- ✅ La gestion des filtres et relations entre les tables
- ✅ L’actualisation automatique des données
- ✅ L’affichage rapide des indicateurs clés

#### 📍 Travail à réaliser en Power BI
- Importer les vues SQL créées depuis MySQL.
- Établir les relations entre les tables selon le schéma en étoile.
- Créer les visualisations (graphiques, tableaux, KPI) en utilisant les métriques demandées.
- Créer des filtres interactifs pour explorer les données en fonction des régions, produits, employés, etc.
- S’assurer que le tableau de bord est actualisable quotidiennement.

💡 **Livrable attendu** : Un tableau de bord Power BI complet avec les indicateurs demandés, basé sur les vues SQL créées en amont.

### Conclusion
Vous devrez structurer les données en SQL avant de les exploiter dans Power BI. Ce projet vous permettra de comprendre l’importance du Data Modeling, d’optimiser les performances des requêtes et de créer un dashboard interactif qui répond aux besoins d’un directeur d’entreprise.

🚀 À vous de jouer !

## Ressources

Requetes pour générer la dim_date :

CREATE VIEW DIM_DATES AS
WITH RECURSIVE date_series AS (
    SELECT DATE('2019-01-01') AS full_date
    UNION ALL
    SELECT DATE_ADD(full_date, INTERVAL 1 DAY)
    FROM date_series
    WHERE full_date < DATE('2025-12-31')
)
SELECT
    full_date AS order_date,
    YEAR(full_date) AS year,
    MONTH(full_date) AS month,
    QUARTER(full_date) AS quarter,
    DATE_FORMAT(full_date, '%M') AS month_name,
    WEEK(full_date, 1) AS week_number,
    DAY(full_date) AS day_of_month,
    DAYNAME(full_date) AS day_name
FROM date_series;


**Note importante** : Les stocks sont mis à jour tous les deux mois. Par conséquent, les données actuelles reflètent uniquement les deux derniers mois.
{: .alert-info }

Si des limitations techniques empêchent de répondre à certains KPI, proposez des alternatives alignées avec les objectifs métiers du client.
{: .alert-warning }

Voici le schéma de la base de données :

![Diagram](assets/image/diagram.PNG)
{: .text-center }

## Outils

Le directeur ne souhaite pas travailler avec SQL mais veut accéder aux données automatiquement et graphiquement. Vous pouvez proposer l'outil de votre choix (Power BI, Tableau, etc.), tant que le tableau de bord est pertinent.

À titre d'information, la base de données est disponible sur un serveur de l'entreprise. Vous y accédez en mode lecture seule avec un compte utilisateur fourni.

L'entreprise vous fournit également le script que vous pouvez exécuter sur votre serveur MySQL local. Les données sont identiques et s'arrêtent à la fin du mois précédent.

## Base de données SQL

Vous avez le choix entre vous connecter au serveur cloud ou déployer le script localement. Les données sont identiques dans les deux cas.

### Installation locale

Vous pouvez installer un serveur MySQL Community sur votre machine, ainsi que le client MySQL Workbench. La base de données est prête à être chargée dans un serveur MySQL. Connectez-vous à votre serveur via Workbench, et exécutez [tout le code dans ce fichier](https://drive.google.com/file/d/103Qm2gwiTkRFlHH4Sn-dOSAW97b8zX8U/view?usp=sharing).

### Serveur cloud

Vous pouvez vous connecter au serveur MariaDB (un fork de MySQL) de l'entreprise.

- **Hostname**: **51.178.25.157**
- **Port**: **23456**
- **Username**: **toyscie**
- **Password**: **WILD4Rdata!**

## Connexion avec MySQL Workbench

![MySQL_Connect](assets/image/mysql_connection.PNG)
{: .text-center }

## Livrable attendu

Vous donnerez une courte présentation de votre tableau de bord (demandez à votre formateur la durée). La présentation doit inclure :

- **Vue d'ensemble du contexte, présentation de l'équipe et des outils utilisés.**
- **Démonstration de votre tableau de bord, et interprétation des KPI métiers.**
- **Difficultés rencontrées et perspectives d'évolution.**

**N'hésitez pas à créer des KPI supplémentaires !**
