---
title: Processus de création de GitHub Pages
description: ''
---

# Processus de création de GitHub Pages

Ce guide vous explique comment créer des GitHub Pages à partir d'un dépôt existant, en utilisant un fichier .PDF pour générer du contenu en Markdown.

# Étapes à suivre

## 1. Cloner le dépôt `Data-Training-Resources`

Commencez par cloner le dépôt GitHub sur votre machine locale.

```bash
git clone https://github.com/wildcodeschool/Data-Training-Resources.git
```

Accédez ensuite au répertoire cloné.

```bash
cd data-training-resources
```

## 2. Récupérer le fichier original sous forme de PDF

Identifiez et téléchargez le fichier .PDF que vous souhaitez convertir en fichier Markdown.

## 3. Convertir le fichier PDF en Markdown
Utilisez ChatGPT pour générer un fichier markdown à partir du fichier .PDF. Vous pouvez lui fournir le contenu du PDF et demander la conversion en markdown.
(Création d'un GPT pour optimiser le markdown en cours.)

## 4. Créer un sous-dossier dans `docs/`
Créez un sous-dossier dans le répertoire `data-training-resources/docs/`.
Le nom de ce dossier sera utilisé comme partie de l'URL de la GitHub Page.

>Par exemple, pour le projet 1, le dossier est `data-training-resources/docs/projet/projet-1` et l'URl est donc `https://wildcodeschool.github.io/data-training-resources/projet/projet-1/`

## 5. Créer un fichier `README.md`
Dans le sous-dossier créé, ajoutez un fichier `README.md` qui contiendra le contenu markdown. Ce fichier sera la base de votre page web.

## 5.5 Créer un sous-dossier `assets` (OPTIONNEL)
Créez un sous-dossier supplémentaires appelé `assets` dans lequel vous pouvez rajouter des dossier `image` ou autre suivant les besoins de la page.

## 6. Ajouter le titre, la description et le layout
En haut du fichier `README.md`, ajoutez des métadonnées avec un titre, une description et un layout.
Voici un exemple :

```markdown
---
title: Projet 1
description: 'SQL & BI - Toys & Models'
layout: tic-tac
---
```

Vous pouvez personnaliser le titre, la description et le layout en fonction de vos besoins.

## 7. Commit et push des modifications
Une fois votre fichier `README.md`prêt et placé dans le bon dossier, il ne vous reste plus qu'à effectuer un commit et un push des modifications.

```bash
git add docs/projet/projet-1/README.md
git commit -m "Ajout du projet 1 dans GitHub Pages"
git push origin main
```

Votre page GitHub sera disponible à l'URL que vous avez définie précédemment, après quelques minutes de mise à jour.