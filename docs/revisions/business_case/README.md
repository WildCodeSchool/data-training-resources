---
title: Business Case
description: 'NYC Taxi Services'
layout: default
---

![Header](assets/header.png)
{: .text-center }

## **Contexte et Présentation de l’Entreprise**

**NYC Taxi Services** est une entreprise de transport historique opérant à New York. Forte d’une longue expérience dans le service de taxis, l’entreprise a toujours cherché à offrir un service de qualité en assurant la mobilité d’une clientèle variée dans un environnement urbain très compétitif. Pour rester en phase avec les évolutions du marché et répondre aux attentes croissantes des clients, NYC Taxi Services souhaite aujourd’hui optimiser ses opérations et renforcer son efficacité.

## **Les Besoins de l’Entreprise**

Face à la concurrence et aux enjeux d’urbanisation, NYC Taxi Services se trouve confrontée à plusieurs défis stratégiques :

* **Comprendre la demande et les comportements de déplacement :**
  L’entreprise veut savoir **quand** et **où** se concentrent les demandes de courses afin d’ajuster le déploiement de sa flotte. Par exemple, identifier les heures de forte affluence et les zones géographiques à forte demande permettra de mieux planifier les ressources.
* **Optimiser la répartition de la flotte :**
  En analysant la durée et la distance des courses ainsi que les zones de prise en charge et de dépose, l’entreprise souhaite améliorer la répartition de ses taxis. L’objectif est de réduire les temps d’attente pour les passagers et d’augmenter l’efficacité des trajets.
* **Améliorer la rentabilité des courses :**
  NYC Taxi Services désire explorer les éléments financiers de chaque course (tarif, suppléments, taxes, pourboires, etc.) pour mieux comprendre les facteurs qui influent sur la rentabilité. Cela peut aider à ajuster la tarification ou à identifier des pistes pour augmenter le revenu par course.
* **Détecter et comprendre les dysfonctionnements éventuels :**
  Par exemple, l’analyse du flag indiquant si le trajet a été stocké en mémoire (store-and-forward) pourra révéler des problèmes de connectivité ou d’autres irrégularités qui pourraient impacter la qualité du service.

Pour répondre à ces enjeux, NYC Taxi Services dispose d’un jeu de données détaillé couvrant la période de **janvier 2016 à mars 2016**. Ce dataset contient des informations précises sur chaque course, notamment :

* **Horodatages :**
  * *tpep\_pickup\_datetime* et *tpep\_dropoff\_datetime* pour connaître les dates et heures de début et fin de course.
* **Localisation géographique :**
  * *Pickup\_longitude* et *Pickup\_latitude* pour le lieu de prise en charge,
  * *Dropoff\_longitude* et *Dropoff\_latitude* pour le lieu de dépose.
* **Détails opérationnels :**
  * *Passenger\_count* pour le nombre de passagers,
  * *Trip\_distance* pour la distance parcourue,
  * *Store\_and\_fwd\_flag* pour identifier des courses avec transmission différée.
* **Informations financières :**
  * *Fare\_amount*, *Extra*, *MTA\_tax*, *Improvement\_surcharge*, *Tip\_amount*, *Tolls\_amount* et *Total\_amount*, permettant d’analyser la structure tarifaire et la rentabilité de chaque course.
* **Autres informations utiles :**
  * *VendorID*, *RateCodeID* et *Payment\_type* qui offrent des détails sur les fournisseurs, les tarifs appliqués et les modes de paiement.

## **Objectifs de l’Analyse**

En exploitant ce jeu de données, l’entreprise cherche à répondre à des questions clés telles que :

* **Quand et où la demande de courses est-elle la plus forte ?**
  (Analyse des horaires de prise en charge et des localisations géographiques)
* **Comment optimiser l’allocation de la flotte pour améliorer la réactivité et la satisfaction client ?**
  (Répartition des taxis en fonction de la demande et des zones d’activité)
* **Quels sont les facteurs impactant la rentabilité des courses ?**
  (Étude des composants financiers de chaque course)
* **Existe-t-il des anomalies ou des dysfonctionnements dans l’enregistrement des courses ?**
  (Analyse du flag « store and forward » et d’autres indicateurs opérationnels)

## **Description des Colonnes**

1. **VendorID**
   * **Description :** Code indiquant le fournisseur TPEP (Third Party Expenditure Provider) qui a fourni l'enregistrement (ex. Creative Mobile Technologies, VeriFone Inc.).
2. **tpep\_pickup\_datetime**
   * **Description :** Date et heure à laquelle le taxi a pris en charge le passager (engagement du compteur).
3. **tpep\_dropoff\_datetime**
   * **Description :** Date et heure à laquelle le taxi a déposé le passager (désengagement du compteur).
4. **Passenger\_count**
   * **Description :** Nombre de passagers présents dans le taxi (valeur saisie par le chauffeur).
5. **Trip\_distance**
   * **Description :** Distance du trajet en miles, telle que reportée par le taximètre.
6. **Pickup\_longitude** et **Pickup\_latitude**
   * **Description :** Coordonnées géographiques (longitude et latitude) du lieu où le taxi a pris en charge le passager.
7. **RateCodeID**
   * **Description :** Code tarifaire appliqué à la fin du trajet. Par exemple :
     * **Standard rate**
     * **JFK**
     * **Newark**
     * **Nassau or Westchester**
     * **Negotiated fare**
     * **Group ride**
8. **Store\_and\_fwd\_flag**
   * **Description :** Indique si l’enregistrement du trajet a été stocké dans la mémoire du véhicule avant d’être envoyé au fournisseur, en cas de connexion indisponible.
     * **Y** \= store and forward trip
     * **N** \= non
9. **Dropoff\_longitude** et **Dropoff\_latitude**
   * **Description :** Coordonnées géographiques (longitude et latitude) du lieu où le taxi a déposé le passager.
10. **Payment\_type**
    * **Description :** Code numérique indiquant le mode de paiement utilisé par le passager. Par exemple :
      * **Credit card**
      * **Cash**
      * **No charge**
      * **Dispute**
      * **Unknown**
      * **Voided trip**
11. **Fare\_amount**
    * **Description :** Tarif calculé par le taximètre en fonction du temps et de la distance.
12. **Extra**
    * **Description :** Suppléments et surcharges divers (par exemple, frais de pointe ou frais de nuit).
13. **MTA\_tax**
    * **Description :** Taxe MTA de 0,50 USD, appliquée automatiquement en fonction du tarif en vigueur.
14. **Improvement\_surcharge**
    * **Description :** Supplément d’amélioration de 0,30 USD, ajouté lors de la fin du trajet (en vigueur depuis 2015).
15. **Tip\_amount**
    * **Description :** Montant du pourboire. Pour les paiements par carte, ce champ est rempli automatiquement (les pourboires en espèces ne sont pas inclus).
16. **Tolls\_amount**
    * **Description :** Total des péages payés pendant le trajet.
17. **Total\_amount**
    * **Description :** Montant total facturé au passager (hors pourboires en espèces).

## Ressources

Lien pour les CSV : [https://drive.google.com/drive/folders/1To9yVwsC-EJrbR7roflp83-JAKfco6iX](https://drive.google.com/drive/folders/1To9yVwsC-EJrbR7roflp83-JAKfco6iX)