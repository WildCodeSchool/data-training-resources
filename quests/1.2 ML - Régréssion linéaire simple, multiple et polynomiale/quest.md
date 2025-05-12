# Régression linéaire simple, multiple et polynomiale

### Introduction

La régression linéaire est l'un des algorithmes les plus fondamentaux et les plus utilisés en apprentissage automatique et en statistiques. Elle permet de modéliser la relation entre une variable dépendante (ou cible) et une ou plusieurs variables indépendantes (ou caractéristiques) **en supposant que cette relation soit linéaire**.

```alert-infos
**Concept clé** :  
La régression linéaire cherche à trouver la "meilleure" droite (ou hyperplan en plusieurs dimensions) qui passe au plus près de l'ensemble des points de données. Cette droite peut ensuite être utilisée pour prédire de nouvelles valeurs.
```

![](https://media.licdn.com/dms/image/D5622AQGZroNaN4DhDw/feedshare-shrink_1280/0/1720409710564?e=1723075200&v=beta&t=XUSF9gawWlgP-NOU7opaJxYo71nVG1VaPAvSrRM4rCI)

### Objectifs

✅ Comprendre les principes de la régression linéaire simple et multiple  
✅ Maîtriser l'utilisation de scikit-learn pour l'implémentation des modèles de régression  
✅ Savoir transformer un problème non linéaire en problème linéaire grâce à la régression polynomiale  
✅ Apprendre à évaluer la performance des modèles de régression  
✅ Mettre en pratique ces concepts à travers des exemples concrets

### Sommaire

### 1. Scikit-learn : la boîte à outils ultime pour le Machine Learning

```alert-infos
**Scikit-learn** est une bibliothèque Python open-source qui fournit des outils simples et efficaces pour l'analyse prédictive des données. Elle inclut de nombreux algorithmes de classification, régression et clustering ainsi que des outils pour la préparation des données, l'évaluation de modèle, etc.
```

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7IJhNVZ2UNFUlsJoPlVH3I_xuPqBVTa1GRA&s)

```alert-success
**Pourquoi utiliser scikit-learn ?**
- Interface cohérente et bien documentée
- Grande variété d'algorithmes disponibles
- Excellente intégration avec l'écosystème Python (NumPy, Pandas, Matplotlib)
- Communauté active et nombreuses ressources disponibles
- Performances optimisées pour les calculs scientifiques
```

### 2. Les fonctions essentielles de scikit-learn

Le fonctionnement de scikit-learn repose sur quelques fonctions fondamentales : `fit()`, `predict()` et `score()`. Comprendre ces fonctions est essentiel pour utiliser efficacement la bibliothèque.

#### 2.1 Création d'un modèle

```alert-infos
La première étape consiste à créer une instance de la classe correspondant à l'algorithme que vous souhaitez utiliser. Dans le cas de la régression linéaire, il s'agit de la classe `LinearRegression`.
```

```python
from sklearn.linear_model import LinearRegression

# Création d'un objet de régression linéaire
model = LinearRegression()
```

#### 2.2 La fonction `fit()`

```alert-warning
La fonction `fit()` est utilisée pour **entraîner** le modèle sur un ensemble de données. Durant cette étape, le modèle va apprendre les relations entre les features X et les valeurs cibles y.

C'est lors de cette phase que le modèle détermine les paramètres optimaux (comme les coefficients de la droite de régression) qui permettront de faire les meilleures prédictions possibles.
```

```python
# Entraînement d'un modèle sur des données d'apprentissage
X = ...  # Vos données d'entrée (caractéristiques)
y = ...  # Votre colonne de valeurs cibles

model.fit(X, y)
```

```alert-error
**Attention au format des données !**

Scikit-learn attend des données d'entrée sous une forme spécifique :
* Une matrice bidimensionnelle pour les features (X)
* Pas de valeurs manquantes (ni dans X, ni dans y)

Si votre jeu de données ne contient qu'une seule feature, vous devrez le transformer en matrice 2D avec `reshape` :
- `X.reshape(-1, 1)` : Transforme un array 1D en une matrice 2D avec une seule colonne
- `X.reshape(1, -1)` : Transforme un array 1D en une matrice 2D avec une seule ligne

Cette mise en forme est nécessaire tant pour `fit()` que pour `predict()`.
```

#### 2.3 La fonction `predict()`

```alert-infos
Une fois le modèle entraîné, la fonction `predict()` permet de faire des **prédictions** sur de nouvelles données. Le modèle utilise les paramètres déterminés lors de la phase d'entraînement pour estimer les valeurs cibles correspondantes.
```

```python
# Faire des prédictions sur de nouvelles données
X_new = np.array([34, 67, 99])  # Nouvelles données d'entrée

# Pensez à remodeler les données si nécessaire
X_new = X_new.reshape(-1, 1)  

# Obtention des prédictions
y_pred = model.predict(X_new)
```

#### 2.4 La fonction `score()`

```alert-infos
La fonction `score()` permet d'**évaluer la performance** du modèle sur un ensemble de données. Pour les modèles de régression, elle renvoie le coefficient de détermination R² qui mesure la qualité de l'ajustement du modèle.
```

![](https://miro.medium.com/v2/resize:fit:1400/1*_HbrAW-tMRBli6ASD5Bttw.png)

```alert-warning
**Le coefficient R²** :
- Varie généralement entre 0 et 1 (peut être négatif dans certains cas)
- R² = 1 : Le modèle explique parfaitement la variabilité des données
- R² = 0 : Le modèle n'explique pas mieux les données que la simple moyenne
- R² < 0 : Le modèle est moins performant que la simple moyenne (rare)

En pratique, un R² supérieur à 0.7 est souvent considéré comme bon, mais cela dépend fortement du domaine d'application.
```

```python
# Évaluer la performance du modèle sur les données de test
X_test = ...  # Vos données de test (features)
y_test = ...  # Vos valeurs cibles de test

score = model.score(X_test, y_test)
print(f"Le R² de mon modèle est de {score*100:.2f}%")
```

```alert-success
**Conseil pratique** : La documentation officielle de scikit-learn est une excellente ressource pour comprendre en détail le fonctionnement de ces fonctions. N'hésitez pas à la consulter régulièrement !
```

### 3. Régression linéaire simple

```alert-infos
Une régression linéaire est dite **simple** lorsqu'elle utilise une seule variable indépendante (feature) pour prédire la variable dépendante (target). Le modèle recherche alors l'équation de la droite `y = ax + b` qui s'ajuste le mieux aux données.
```

```alert
**Équation de la régression linéaire simple** :
y = β₀ + β₁x + ε

Où :
- y est la variable à prédire
- x est la variable explicative
- β₀ est l'ordonnée à l'origine (intercept)
- β₁ est le coefficient directeur (pente)
- ε est le terme d'erreur
```

```alert-infos
**Illustration graphique** :

![](https://miro.medium.com/v2/resize:fit:1400/1*Ug_tjOL5u_z-ZjKTgX_kMw.png)

Dans ce graphique :
- Les points bleus représentent les données observées
- La ligne rouge représente la droite de régression (y = β₀ + β₁x)
- β₀ est le point où la droite coupe l'axe des y (quand x = 0)
- β₁ détermine l'inclinaison de la droite (une augmentation de 1 unité en x produit une augmentation de β₁ unités en y)
- Les lignes verticales vertes représentent les erreurs (ε) entre les valeurs observées et les valeurs prédites par le modèle
- L'algorithme de régression cherche à minimiser la somme des carrés de ces erreurs
```

Voici un exemple complet d'implémentation d'une régression linéaire simple avec scikit-learn :

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Création de données simulées avec une relation linéaire
nombre_valeurs = 200
X = np.linspace(0, 10, nombre_valeurs).reshape(-1, 1)  # Reshape pour obtenir une matrice 2D
y = 2*X + 1 + np.random.randn(nombre_valeurs, 1)  # y = 2x + 1 + bruit aléatoire

# Affichage du coefficient de corrélation de Pearson
df = pd.DataFrame({"X": X.flatten(), "y": y.flatten()})
correlation = df.corr().iloc[0, 1]
print(f"La corrélation de Pearson entre X et y est de {correlation:.3f}")

# Visualisation des données
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label="Données")
plt.title("Relation entre X et y")
plt.xlabel("Variable X")
plt.ylabel("Variable y")

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X, y)

# Affichage des paramètres du modèle
print(f"Coefficient directeur (pente) : {model.coef_[0][0]:.3f}")
print(f"Ordonnée à l'origine : {model.intercept_[0]:.3f}")
print(f"Équation de la droite : y = {model.coef_[0][0]:.3f}x + {model.intercept_[0]:.3f}")

# Évaluation du modèle
r2 = model.score(X, y)
print(f"Coefficient de détermination (R²) : {r2:.3f}")

# Prédiction pour une nouvelle valeur
valeur_test = 12
prediction = model.predict([[valeur_test]])[0][0]
print(f"Prédiction pour X = {valeur_test} : y = {prediction:.3f}")

# Ajout de la droite de régression au graphique
X_plot = np.linspace(0, 12, 100).reshape(-1, 1)
y_plot = model.predict(X_plot)
plt.plot(X_plot, y_plot, color='red', linewidth=2, label="Droite de régression")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

```alert-success
**Interprétation des résultats** :
- Le coefficient directeur (pente) indique comment la variable y change en moyenne lorsque x augmente d'une unité.
- L'ordonnée à l'origine représente la valeur moyenne de y lorsque x est égal à zéro.
- Le R² nous indique la proportion de la variance de y qui est expliquée par le modèle.
```

### 4. Régression linéaire multiple

```alert-infos
Une régression linéaire est dite **multiple** lorsqu'elle utilise plusieurs variables indépendantes (features) pour prédire la variable dépendante. Le modèle recherche alors un hyperplan dans un espace à plusieurs dimensions.
```

```alert
**Équation de la régression linéaire multiple** :
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε

Où :
- y est la variable à prédire
- x₁, x₂, ..., xₙ sont les variables explicatives
- β₀, β₁, β₂, ..., βₙ sont les coefficients du modèle
- ε est le terme d'erreur
```

```alert-infos
**Illustration graphique** :

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRajJEe7Tqp3uGhVkmjX7xNAzxC-aJ69W6VmtMuPoYuJxYlYfMmxl5TH0j8eX0zjg1ZUlg&usqp=CAU)

Dans ce graphique (cas simplifié avec 2 variables explicatives) :
- L'axe vertical représente la variable y à prédire
- Les deux autres axes représentent les variables explicatives x₁ et x₂
- Le plan bleu représente le modèle de régression linéaire multiple
- β₀ est l'ordonnée à l'origine (valeur de y quand toutes les variables x sont nulles)
- β₁ et β₂ représentent l'impact de chaque variable sur y (une augmentation d'une unité de x₁ entraîne une variation de β₁ unités de y, si toutes les autres variables restent constantes)
- Les tiges verticales représentent les erreurs (ε) entre les points observés et le plan de régression
- Avec plus de 2 variables explicatives, le modèle devient un hyperplan dans un espace à n+1 dimensions
```

Voici un exemple d'implémentation d'une régression linéaire multiple :

```python
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Chargement d'un jeu de données d'accidents de voiture
accidents = sns.load_dataset("car_crashes")

# Sélection des features et de la target
X = accidents[["speeding", "alcohol", "not_distracted", "no_previous"]]
y = accidents["total"]

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Affichage des coefficients du modèle
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})
print("Coefficients du modèle :")
print(coefficients)
print(f"Ordonnée à l'origine : {model.intercept_:.3f}")

# Prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluation du modèle
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Erreur quadratique moyenne : {mse:.3f}")
print(f"Coefficient de détermination (R²) : {r2:.3f}")

# Visualisation des prédictions vs valeurs réelles
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.title("Prédictions vs Valeurs réelles")
plt.xlabel("Valeurs réelles")
plt.ylabel("Prédictions")
plt.grid(True, alpha=0.3)
plt.show()
```

```alert-warning
**Points importants à noter** :
- En régression multiple, il n'est pas nécessaire de remodeler les données avec `reshape()` car les features forment déjà une matrice 2D (plusieurs colonnes).
- L'interprétation des coefficients est plus complexe : chaque coefficient représente la variation moyenne de y lorsque la feature correspondante augmente d'une unité **et que toutes les autres features restent constantes**.
- Il est essentiel de vérifier la multicolinéarité (forte corrélation entre les variables explicatives) qui peut affecter la stabilité et l'interprétation du modèle.
```

### 5. Régression polynomiale

```alert-infos
La **régression polynomiale** permet de modéliser des relations non linéaires entre les variables en utilisant des polynômes. Plutôt que de chercher une droite, le modèle cherche une courbe de degré n qui s'ajuste au mieux aux données.
```

![](https://gbhat.com/assets/gifs/polynomial_regression_fit.gif)

```alert
**Équation de la régression polynomiale (degré 2)** :
y = β₀ + β₁x + β₂x² + ε

Pour un polynôme de degré plus élevé :
y = β₀ + β₁x + β₂x² + β₃x³ + ... + βₙxⁿ + ε
```

```alert-infos
**Illustration graphique** :

![](https://miro.medium.com/v2/resize:fit:1400/1*wMjdWdLkIkAViRoQzJvfVQ.png)

Dans ce graphique :
- Les points bleus représentent les données observées
- La courbe rouge représente un modèle de régression polynomiale
- β₀ est l'ordonnée à l'origine (valeur de y quand x = 0)
- Les coefficients β₁, β₂, etc. déterminent la forme de la courbe :
  * β₁ influence la tendance linéaire
  * β₂ influence la courbure quadratique
  * Les coefficients d'ordre supérieur influencent des formes plus complexes
- Les lignes verticales vertes représentent les erreurs (ε) entre les valeurs observées et les valeurs prédites
- Contrairement à la régression linéaire simple qui ne peut modéliser qu'une tendance linéaire, la régression polynomiale peut capturer des relations non linéaires entre les variables
- Plus le degré du polynôme est élevé, plus la courbe peut être flexible, mais attention au risque de surapprentissage !
```

```alert-success
**Astuce** : En réalité, la régression polynomiale est toujours une régression linéaire ! La différence est que nous transformons d'abord nos données en créant de nouvelles features qui sont des puissances de la feature originale (x², x³, etc.). Ensuite, nous appliquons une régression linéaire standard sur ces nouvelles features.
```

Voici comment implémenter une régression polynomiale avec scikit-learn :

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

# Création de données non linéaires
X = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]).reshape(-1, 1)
y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100])

# Visualisation des données
plt.figure(figsize=(12, 7))
plt.scatter(X, y, s=50, alpha=0.8, label="Données originales")
plt.title("Comparaison des modèles de régression", fontsize=15)
plt.xlabel("Variable X", fontsize=12)
plt.ylabel("Variable y", fontsize=12)

# Régression linéaire simple
model_lin = LinearRegression()
model_lin.fit(X, y)
y_lin_pred = model_lin.predict(X)

# Calcul et affichage du R²
r2_lin = r2_score(y, y_lin_pred)
print(f"R² du modèle linéaire : {r2_lin:.3f}")

# Tracé de la régression linéaire
X_plot = np.linspace(0, 25, 100).reshape(-1, 1)
plt.plot(X_plot, model_lin.predict(X_plot), 'r-', label=f"Régression linéaire (R² = {r2_lin:.3f})", linewidth=2)

# Test de différents degrés polynomiaux
for degree in [2, 3, 10]:
    # Création et entraînement du modèle polynomial
    model_poly = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )
    model_poly.fit(X, y)
    
    # Prédictions et calcul du R²
    y_poly_pred = model_poly.predict(X)
    r2_poly = r2_score(y, y_poly_pred)
    print(f"R² du modèle polynomial de degré {degree} : {r2_poly:.3f}")
    
    # Tracé de la courbe polynomiale
    colors = ['g-', 'b-', 'm-']
    plt.plot(X_plot, model_poly.predict(X_plot), colors[min(degree-2, 2)], 
             label=f"Régression polynomiale (degré {degree}, R² = {r2_poly:.3f})", 
             linewidth=2)

plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

```alert-warning
**Attention au surapprentissage !**

Un polynôme de degré élevé peut s'ajuster parfaitement aux données d'entraînement (R² proche de 1), mais généraliser très mal sur de nouvelles données. C'est ce qu'on appelle le **surapprentissage** ou **overfitting**.

Pour éviter ce problème :
- Divisez toujours vos données en ensembles d'entraînement et de test
- Utilisez la validation croisée pour évaluer la performance du modèle
- Choisissez le degré du polynôme avec précaution (compromis biais-variance)
- Considérez l'utilisation de techniques de régularisation (Ridge, Lasso)
```

### 6. Évaluation des connaissances

```alert-infos
**Testez vos connaissances** :  
Ce quiz vous permettra de vérifier votre compréhension des concepts fondamentaux de la régression linéaire et de l'utilisation de scikit-learn.
```

```quiz
true|||true|||true
# Qu'est-ce que la régression linéaire ?
[x] Un algorithme qui modélise la relation linéaire entre des variables indépendantes et une variable dépendante
[] Un algorithme qui classe des données en catégories
[] Une technique de réduction de dimensionnalité

# Dans scikit-learn, quelle fonction est utilisée pour entraîner un modèle ?
[x] fit()
[] train()
[] learn()

# Quelle est la différence entre la régression linéaire simple et multiple ?
[x] La régression simple utilise une seule variable explicative, tandis que la régression multiple en utilise plusieurs
[] La régression simple est plus précise que la régression multiple
[] La régression simple peut seulement prédire des valeurs binaires

# Quelle méthode de scikit-learn permet d'obtenir le coefficient de détermination (R²) d'un modèle ?
[x] score()
[] evaluate()
[] r2_score()

# Comment transformer une régression linéaire en régression polynomiale avec scikit-learn ?
[x] En utilisant PolynomialFeatures pour créer de nouvelles features, puis en appliquant LinearRegression
[] En utilisant directement la classe PolynomialRegression
[] En ajoutant le paramètre polynomial=True à la classe LinearRegression

# Si votre modèle de régression a un R² de 0.85, cela signifie que :
[x] Le modèle explique 85% de la variance de la variable cible
[] Le modèle a une précision de 85%
[] 85% des prédictions sont exactes

# Pourquoi faut-il utiliser reshape(-1, 1) sur un tableau NumPy à une dimension avant de l'utiliser avec scikit-learn ?
[x] Parce que scikit-learn attend des données sous forme de matrice 2D, même avec une seule feature
[] Pour trier les données dans l'ordre croissant
[] Pour normaliser les données entre 0 et 1

# Dans une régression linéaire multiple, comment interpréter le coefficient d'une feature ?
[x] Il représente la variation moyenne de la variable cible lorsque cette feature augmente d'une unité et que toutes les autres restent constantes
[] Il représente l'importance relative de cette feature par rapport aux autres
[] Il indique la corrélation entre cette feature et la variable cible

# Quel est le principal risque lié à l'utilisation d'un polynôme de degré trop élevé ?
[x] Le surapprentissage (overfitting) : le modèle s'ajuste trop bien aux données d'entraînement mais généralise mal
[] Le sous-apprentissage (underfitting) : le modèle ne capture pas la complexité des données
[] Une augmentation du temps de calcul sans amélioration des performances

# Comment diviser vos données en ensembles d'entraînement et de test avec scikit-learn ?
[x] En utilisant train_test_split()
[] En utilisant data_split()
[] En utilisant divide_data()
```

### 7. Conclusion et ressources

```alert-success
La régression linéaire est une technique fondamentale en Machine Learning qui constitue souvent le premier pas dans l'apprentissage de la modélisation prédictive. Malgré sa simplicité, elle reste un outil puissant et interprétable qui peut servir de base à des modèles plus complexes.

Dans les prochaines quêtes, nous explorerons d'autres algorithmes de Machine Learning et approfondirons nos connaissances sur l'évaluation et l'optimisation des modèles.
```

```alert-info
**Ressources pour approfondir** :
- [Documentation officielle de scikit-learn sur la régression linéaire](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares)
- [Tutoriel scikit-learn sur la régression polynomiale](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html)
- [Cours en ligne "Machine Learning" d'Andrew Ng sur Coursera](https://www.coursera.org/learn/machine-learning)
- [Introduction à la régression linéaire avec Python](https://realpython.com/linear-regression-in-python/)
```

### 8. Challenge

```alert-infos
**Mettez en pratique ce que vous avez appris !**  

Pour consolider vos connaissances, relevez le défi proposé dans le notebook suivant : [Introduction au Machine Learning - Régression linéaire simple, multiple et polynomiale](https://colab.research.google.com/drive/1g3XXFaWC2mMzx_LA1GK-u5sqirKF8bts?usp=sharing)

Créez une copie du notebook et travaillez sur les exercices proposés.
```

```alert-warning
**Conseils pour réussir le challenge** :
- Prenez le temps de bien comprendre les données avant de commencer à modéliser
- Visualisez les relations entre les variables pour choisir le type de régression approprié
- N'oubliez pas de vérifier la qualité de votre modèle à l'aide de métriques adaptées
- Comparez les performances des différents modèles (simple, multiple, polynomiale)
- Interprétez les résultats et tirez-en des conclusions pertinentes
```

### Critères de validation

```alert-success
**Pour valider cette quête, assurez-vous que** :
- Votre code est accessible dans un notebook en ligne
- Vous avez correctement implémenté les différents types de régression
- Vous avez analysé et interprété les résultats de vos modèles
- Vous avez comparé les performances des différentes approches
- Vous avez respecté les bonnes pratiques de modélisation
```
