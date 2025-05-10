# Introduction au Machine Learning

### Introduction

Le Machine Learning (ou apprentissage automatique) est une branche de l'intelligence artificielle qui permet aux ordinateurs d'**apprendre sans être explicitement programmés**.

```alert-infos
**Concept clé** :  
Le Machine Learning permet de contourner le paradoxe de Polanyi, qu'Isaac Asimov résumait ainsi : "Ne sachant pas comment je fais [certaines choses avec mon esprit], il m'est impossible de programmer un ordinateur pour qu'il reproduise ce que je ne connais pas".
```

![](https://www.dilepix.com/hs-fs/hubfs/blog/schema-IA-machine-learning-deep-learning-Dilepix-1.png?width=600&name=schema-IA-machine-learning-deep-learning-Dilepix-1.png)

### Objectifs

✅ Comprendre le fonctionnement et le vocabulaire de l'intelligence artificielle  
✅ Comprendre pourquoi et comment utiliser le Machine Learning  
✅ Connaître les différents types d'apprentissage (supervisé, non supervisé, par renforcement)  
✅ Se familiariser avec les principales catégories d'algorithmes (régression, classification, clustering)  
✅ Acquérir les bases méthodologiques pour mener un projet de Machine Learning  
✅ Connaître les fonctions de base de Scikit-learn

### Sommaire

### 1. Les réalisations possibles en Machine Learning

```alert-infos
L'idée du Machine Learning tourne autour du processus permettant aux machines d'apprendre à partir des données pour faire des prédictions, des classifications, ou découvrir des patterns, sans être explicitement programmées pour chaque tâche.
```

```alert-warning
**Avant de vous lancer dans le Machine Learning, vous devez** :    
1. Avoir des données en quantité suffisante
2. Avoir un objectif clair
```

### 2. Les types d'apprentissages et leurs utilités

Il existe trois grandes catégories d'apprentissage en Machine Learning :

#### Le Machine Learning supervisé

```alert-infos
**Machine Learning supervisé** :  
L'algorithme apprend à partir d'un ensemble de données où chaque exemple est étiqueté avec la bonne réponse.

**Utilisations principales** :
- Prédire une valeur numérique (régression) : probabilité, consommation, âge, chiffre d'affaires...
- Prédire une classe (classification) : passager vivant/mort, type de fleur, genre de film, spam/non spam...
```

```alert
**Exemple concret** :  
Imaginez que vous souhaitez prédire le prix d'une maison. Vous disposez d'un ensemble de données contenant des informations sur des maisons déjà vendues (surface, nombre de chambres, localisation) et leur prix de vente. En utilisant l'apprentissage supervisé, vous pouvez entraîner un modèle qui apprendra à prédire le prix d'une nouvelle maison en fonction de ses caractéristiques.
```

#### Le Machine Learning non supervisé

```alert-infos
**Machine Learning non supervisé** :  
Les modèles sont entraînés sur des données non étiquetées, c'est-à-dire sans réponses ou catégories prédéfinies. L'objectif est de découvrir des structures, des motifs ou des regroupements et créer les étiquettes en conséquence.

**Utilisations principales** :
- Segmentation de clientèle (personas marketing)
- Analyse de séquences génétiques
- Regroupement par caractéristiques minérales
```

```alert
**Exemple concret** :  
Supposons que vous dirigez une boutique en ligne et que vous souhaitez segmenter vos clients pour mieux cibler vos campagnes marketing. Avec l'apprentissage non supervisé, vous pouvez regrouper automatiquement vos clients en fonction de leurs habitudes d'achat, sans avoir défini préalablement les groupes. Le modèle pourrait, par exemple, identifier naturellement les "acheteurs fréquents à petit budget", les "acheteurs occasionnels à gros budget", etc.
```

#### L'apprentissage par renforcement

```alert-warning
**Apprentissage par renforcement** :  
Permet à un agent autonome d'apprendre par lui-même en interagissant avec un environnement au travers d'une succession d'actions récompensées positivement ou négativement.

Cette forme d'apprentissage est très coûteuse en puissance de calcul puisque l'environnement peut engendrer un nombre très grand de combinaisons d'actions possibles. On parle [d'explosion combinatoire](https://fr.wikipedia.org/wiki/Explosion_combinatoire).
```

```alert
**Exemple concret** :  
Un exemple fascinant est celui d'une IA entraînée à exécuter une manœuvre spécifique afin de gagner une course de voiture dans le jeu vidéo TrackMania. Au début, l'IA ne sait pas conduire, mais à force d'essais-erreurs et de récompenses (progresser dans la course), elle apprend non seulement à conduire efficacement mais aussi à exploiter les particularités du jeu pour obtenir des performances surhumaines.

[AI learns to exploit a glitch in Trackmania](https://youtu.be/NUl6QikjR04)
```

![](https://i0.wp.com/deeplylearning.fr/wp-content/uploads/2018/09/type-of-learning.png?resize=781%2C558&ssl=1)

### 3. Les algorithmes classiques du Machine Learning

```alert-infos
**Scikit-learn** est une bibliothèque Python open-source spécialisée dans le Machine Learning. Elle fournit des implémentations efficaces de nombreux algorithmes ainsi que des outils pour la préparation des données, l'évaluation des modèles et l'optimisation des paramètres. C'est l'outil de référence pour les data scientists débutants et confirmés grâce à son API cohérente et sa documentation de qualité.
```

#### 3.1 Régression

```alert-infos
**La régression** est un type d'apprentissage supervisé qui vise à **prédire une valeur numérique continue**. Par exemple, prédire le prix d'une maison en fonction de sa superficie, du nombre de chambres, etc., ou prédire la demande en électricité en fonction de différents facteurs comme la température.
```

```alert
**Quelques algorithmes de régression courants dans Scikit-learn** :
- **Régression linéaire** : Modèle simple qui établit une relation linéaire entre les variables d'entrée et la variable de sortie
- **Régression polynomiale** : Extension de la régression linéaire qui permet de capturer des relations non linéaires
- **Régression Ridge et Lasso** : Variantes de la régression linéaire avec des techniques de régularisation pour éviter le surajustement
```

```alert-warning
Les algorithmes de régression et leurs spécificités mathématiques seront abordés en profondeur dans les prochaines quêtes. Vous apprendrez notamment comment sélectionner le bon algorithme selon la nature de vos données et comment interpréter les coefficients des modèles pour en tirer des insights métier.
```

#### 3.2 Classification

```alert-infos
**La classification** est un autre type d'apprentissage supervisé qui vise à **classifier des données dans des catégories prédéfinies (étiquetées)**. Elle est utilisée pour identifier à quelle classe appartient une nouvelle observation en fonction de ses caractéristiques. Par exemple, déterminer si un email est un spam ou non, ou identifier des images de chats et de chiens.
```

```alert
**Quelques algorithmes de classification courants dans Scikit-learn** :
- **K-Nearest Neighbors (KNN)** : Classe une nouvelle observation selon les classes des k observations les plus proches
- **Régression logistique** : Malgré son nom, c'est un algorithme de classification qui estime la probabilité d'appartenance à une classe
- **Arbres de décision** : Modèle qui prend des décisions basées sur une série de questions
- **Random Forest** : Ensemble d'arbres de décision dont les résultats sont combinés
- **Naive Bayes** : Algorithme probabiliste basé sur le théorème de Bayes
- **Support Vector Machines (SVM)** : Cherche à trouver un hyperplan qui sépare au mieux les classes
```

```alert-warning
Les algorithmes de classification et leurs cas d'usage seront détaillés dans les prochaines quêtes. Vous y découvrirez comment gérer des problèmes de classification multiclasse, comment traiter les déséquilibres de classes, et comment utiliser les probabilités de prédiction pour prendre des décisions métier plus nuancées.
```

#### 3.3 Clustering

```alert-infos
**Le clustering** est un type d'apprentissage non supervisé qui vise à **regrouper des données en fonction de leurs similarités**. Il est utilisé pour automatiquement identifier des structures récurrentes (patterns) dans les données sans avoir à définir de classes au préalable. Par exemple, segmenter des clients en fonction de leurs habitudes d'achat, ou identifier des groupes de gènes qui s'expriment de manière similaire.
```

```alert
**Quelques algorithmes de clustering courants dans Scikit-learn** :
- **K-means** : Divise les données en k groupes en minimisant la distance entre les points et le centre de leur cluster
- **Hierarchical Clustering** : Construit une hiérarchie de clusters, soit en regroupant progressivement les points (approche ascendante), soit en divisant récursivement l'ensemble (approche descendante)
- **DBSCAN** : Identifie des clusters de densité variable et peut détecter des outliers
- **Spectral Clustering** : Utilise les propriétés du spectre de la matrice de similarité pour réduire la dimensionnalité avant le clustering
```

```alert-warning
Les techniques de clustering et leurs applications métier seront approfondies dans les prochaines quêtes. Vous apprendrez notamment comment déterminer le nombre optimal de clusters, comment interpréter les résultats de clustering, et comment utiliser ces insights pour orienter vos stratégies marketing ou vos analyses exploratoires.
```

```alert-success
**Aide au choix d'un algorithme** :  
Scikit-learn propose un "cheat sheet" très pratique pour vous aider à choisir l'algorithme le plus adapté à votre problème en fonction de la taille de vos données, de leur nature et de votre objectif.
```

![](https://scikit-learn.org/1.3/_static/ml_map.png)

### 4. Fonctionnement et méthodologie

```alert-infos
Nous pouvons résumer le processus commun à tous ces algorithmes de la manière suivante. Cette méthodologie s'applique que vous utilisiez Scikit-learn ou toute autre bibliothèque de Machine Learning, et constitue un cadre essentiel pour structurer vos projets d'analyse prédictive.
```

#### 4.1 Définition du besoin

```alert-warning
Avant de commencer, posez-vous les bonnes questions :
- Quel est l'objectif de mon projet ?
- Souhaité-je prédire une valeur numérique ?
- Cherché-je à classer des observations dans des catégories ?
- Ai-je besoin de regrouper des observations similaires ?
```

#### 4.2 Exploration des données

```alert-infos
Cette étape consiste à utiliser des méthodes de statistiques descriptives, des visualisations et des outils d'exploration comme Numpy et Pandas, dans le but de mieux comprendre ce qu'il vous sera possible de faire avec les données actuelles.

La quantité mais aussi la qualité des données sont importantes pour que le modèle apprenne correctement.
```

```alert
**Actions typiques lors de l'exploration** :
- Visualiser la distribution des variables
- Identifier les corrélations entre les variables
- Détecter les valeurs aberrantes et manquantes
- Analyser les tendances et patterns visuels
```

#### 4.3 Préparation des données

```alert-warning
Nous avons fait un état des lieux lors de l'exploration, place au nettoyage à travers divers traitements relatifs aux données :

- **Typage de données** : Conversion des variables au type approprié (int, float, categorical, etc.)
- **Gestion des valeurs manquantes** : Imputation ou suppression selon le contexte
- **Standardisation** : Mise à l'échelle des variables pour qu'elles aient une moyenne de 0 et un écart-type de 1
- **Normalisation** : Mise à l'échelle des variables pour qu'elles soient comprises entre 0 et 1
- **Encodage** : Transformation des variables catégorielles en variables numériques
```

```alert-error
**Attention** :  
Cette étape est généralement considérée comme la plus longue (et la plus fastidieuse 😮‍💨) d'un projet de data science, pouvant représenter jusqu'à 80% du temps total. Ne la négligez pas, car la qualité de vos données détermine directement la qualité de vos résultats !
```

```alert-success
Le but final de cette étape est de définir quelles "features" (colonnes) seront les caractéristiques déterminantes pour notre objectif. Ces colonnes sélectionnées seront, par convention, notre X.

Il sera peut-être nécessaire de *créer de nouvelles colonnes* (feature engineering) à partir de features existantes en fonction des besoins.
```

```alert-info
**Avec un algorithme supervisé**, nous définirons également une cible à prédire, par convention notre "y".

Nous diviserons ensuite nos données en un jeu d'entraînement, sur lequel notre algorithme apprendra, et un jeu de "test" qui servira à évaluer la différence entre la prédiction et la réalité => `train_test_split()`
```

#### 4.4 Choix & Entraînement du modèle

```alert-infos
La création du modèle sera l'étape où l'on va décider, en fonction des étapes précédentes, quels algorithmes seront les plus adaptés à nos données pour atteindre l'objectif défini.

Nous procèderons ensuite à l'entraînement de l'algorithme choisi, en définissant certains paramètres, relatifs à l'algorithme choisi (tous les algorithmes n'ont pas les mêmes paramètres).
```

```alert
**En pratique avec Scikit-learn** :
1. Instancier le modèle : `model = Algorithm(param1=value1, param2=value2)`
   - `Algorithm` est remplacé par l'algorithme choisi (ex: `LinearRegression`, `RandomForestClassifier`, etc.)
   - `param1`, `param2` sont des hyperparamètres spécifiques à l'algorithme (ex: `n_estimators=100` pour Random Forest)

2. Entraîner le modèle : `model.fit(X_train, y_train)`
   - `X_train` : jeu de données d'entraînement (features) obtenu après `train_test_split()`
   - `y_train` : cibles d'entraînement correspondantes (valeurs à prédire)

3. Faire des prédictions : `y_pred = model.predict(X_test)`
   - `X_test` : jeu de données de test (features) obtenu après `train_test_split()`
   - `y_pred` : prédictions générées par le modèle à comparer avec les vraies valeurs `y_test`

**Exemple concret** :
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Chargement des données
data = pd.read_csv('house_prices.csv')

# Définition des features (X) et de la cible (y)
X = data[['surface', 'bedrooms', 'bathrooms', 'age']]  # Variables explicatives
y = data['price']  # Variable à prédire

# Division en jeux d'entraînement et de test (75% entraînement, 25% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Instanciation et entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)
```

```alert-warning
Nous explorerons de façon beaucoup plus approfondie ces concepts dans les prochaines quêtes. Vous apprendrez notamment comment choisir les bons hyperparamètres, comment manipuler différents types de données, et comment évaluer précisément vos modèles.
```
#### 4.5 Interprétation des résultats & Évaluation du modèle

```alert-infos
Dans cette étape, on mesure à quel point le modèle arrive à prédire correctement les choses de différentes manières grâce à des métriques d'évaluation.

Ces métriques sont spécifiques en fonction du contexte de régression ou de classification. On mesure ainsi sa capacité de généralisation !
```

```alert-warning
**La généralisation garantit que le modèle ne se contente pas de mémoriser les données d'entraînement, mais qu'il apprend des patterns sous-jacents qui lui permettent de faire des prédictions précises sur de nouvelles données.**
```

```alert
**Métriques courantes en régression** :
- MAE (Mean Absolute Error) : Erreur absolue moyenne
- MSE (Mean Squared Error) : Erreur quadratique moyenne
- RMSE (Root Mean Squared Error) : Racine carrée de l'erreur quadratique moyenne
- R² (coefficient de détermination) : Proportion de la variance expliquée par le modèle

**Métriques courantes en classification** :
- Accuracy (précision) : Proportion de prédictions correctes
- Precision : Proportion des prédictions positives qui sont réellement positives
- Recall (rappel) : Proportion des cas positifs réels qui sont correctement prédits
- F1-score : Moyenne harmonique de la précision et du rappel
- Matrice de confusion : Tableau qui montre les prédictions correctes et incorrectes pour chaque classe
```

```alert-error
L'interprétation correcte des métriques d'évaluation est cruciale pour juger de la qualité de votre modèle. 

Dans les prochaines quêtes, vous apprendrez à choisir les métriques les plus pertinentes selon votre contexte métier, à interpréter les différentes métriques et à détecter les problèmes classiques comme le sous-apprentissage (underfitting) ou le sur-apprentissage (overfitting).
```

#### 4.6 Optimisation des paramètres

```alert-success
Les résultats obtenus avec ces algorithmes de Machine Learning peuvent s'améliorer grâce à l'optimisation des paramètres. Le but est d'arriver à minimiser l'écart entre la prédiction et les valeurs réelles.
```

```alert-infos
**Techniques d'optimisation courantes** :
- **Grid Search** : Teste toutes les combinaisons possibles de paramètres spécifiés
- **Random Search** : Teste aléatoirement des combinaisons de paramètres dans un espace défini
- **Cross-validation** : Divise les données en plusieurs sous-ensembles pour valider la robustesse du modèle
```

#### NOTE BENE

```alert-success
Ces étapes nous permettent de créer et optimiser un modèle de prédiction.

Celui qui utilise ce genre d'algorithme (ou modèle) n'est pas un concepteur mais **un entraîneur d'algorithmes**.

On vous inclut ce schéma synthétique qui résume les étapes les plus importantes dans le **Machine Learning**.
```
![](https://www.dilepix.com/hs-fs/hubfs/blog/schema-IA-machine-learning-deep-learning-Dilepix-1.png?width=600&name=schema-IA-machine-learning-deep-learning-Dilepix-1.png)


### 5. Quiz de connaissances

```quiz
true|||true|||true
# Qu'est-ce que le Machine Learning ?
[x] Une branche de l'intelligence artificielle qui permet aux ordinateurs d'apprendre sans être explicitement programmés
[] Un langage de programmation spécialisé dans le traitement des données
[] Une méthode pour programmer des ordinateurs de manière plus efficace

# Quel type d'apprentissage utilise des données étiquetées ?
[x] L'apprentissage supervisé
[] L'apprentissage non supervisé
[] L'apprentissage par renforcement

# Dans un contexte de Machine Learning, que représente généralement "X" ?
[x] Les features (caractéristiques) utilisées pour faire des prédictions
[] La cible à prédire
[] Le nombre d'itérations d'entraînement

# Quelle technique est utilisée pour diviser les données en jeu d'entraînement et jeu de test ?
[x] train_test_split()
[] K-means
[] Random Forest

# Quelle métrique d'évaluation est particulièrement adaptée aux problèmes de régression ?
[x] RMSE (Root Mean Squared Error)
[] Accuracy
[] F1-score

# Quelle étape du processus de Machine Learning est généralement considérée comme la plus longue ?
[x] La préparation des données
[] L'entraînement du modèle
[] L'optimisation des paramètres

# Quel algorithme est le plus adapté pour regrouper des clients en segments sans catégories prédéfinies ?
[] Régression linéaire
[] Régression logistique
[x] K-means

# Lequel des algorithmes suivants est un exemple d'apprentissage supervisé ?
[x] Random Forest
[] DBSCAN
[] K-means

# Qu'est-ce que l'overfitting (sur-apprentissage) ?
[x] Le modèle apprend trop bien les données d'entraînement et perd en capacité de généralisation
[] Le modèle n'arrive pas à capturer la complexité des données
[] Le modèle requiert trop de puissance de calcul

# Quel type d'algorithme utiliseriez-vous pour prédire si un email est un spam ou non ?
[] Algorithme de régression
[x] Algorithme de classification
[] Algorithme de clustering

# Dans l'apprentissage par renforcement, qu'est-ce qu'une récompense ?
[x] Un signal qui indique si l'action de l'agent est bonne ou mauvaise
[] Le temps nécessaire pour que l'agent accomplisse sa tâche
[] Le nombre d'erreurs commises par l'agent

# À quoi sert la validation croisée (cross-validation) ?
[x] À évaluer la performance d'un modèle sur différents sous-ensembles de données
[] À nettoyer les données avant l'entraînement
[] À visualiser les données avant la modélisation

# Qu'est-ce qu'une matrice de confusion ?
[x] Un tableau qui montre les prédictions correctes et incorrectes pour chaque classe
[] Une visualisation des corrélations entre différentes variables
[] Une technique pour réduire la dimensionnalité des données

# Quelle technique est utilisée pour trouver les meilleurs paramètres d'un modèle ?
[] Data cleaning
[x] Grid Search ou Random Search
[] Feature engineering

# Quel est l'objectif de la standardisation des données ?
[x] Transformer les variables pour qu'elles aient une moyenne de 0 et un écart-type de 1
[] Convertir toutes les variables en variables catégorielles
[] Supprimer les valeurs aberrantes

# Qu'est-ce que le coefficient de détermination (R²) mesure ?
[x] La proportion de la variance de la variable cible qui est expliquée par le modèle
[] Le nombre d'erreurs commises par le modèle
[] Le temps nécessaire pour entraîner le modèle
```

### 6. Conclusion et ressources

```alert-success
Ces étapes nous permettent de créer et optimiser un modèle de prédiction.
Celui qui utilise ce genre d'algorithme (ou modèle) n'est pas un concepteur mais **un entraîneur d'algorithmes**.

Dans les prochaines quêtes, vous mettrez en pratique ces concepts à travers des projets concrets et vous approfondirez vos connaissances sur chaque type d'algorithme.
```

```alert-info
**Ressources pour approfondir** :
- [Wikipedia - Machine Learning](https://en.wikipedia.org/wiki/machine_learning)
- [Mr. Mint - Tutoriels sur le ML](https://mrmint.fr/)
- [Introduction au machine learning avec Python](https://brightcape.co/introduction-au-machine-learning-avec-python/)
- [Documentation officielle de Scikit-learn](https://scikit-learn.org/stable/documentation.html)
```
