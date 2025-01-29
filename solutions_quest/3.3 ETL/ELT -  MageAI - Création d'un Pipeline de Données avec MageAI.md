### Challenge
Créez un pipeline complet qui manipule des données communales françaises. Suivez les étapes ci-dessous pour réaliser ce challenge.

#### Étapes guidées

##### 1. Configuration du Data Loader
Créez un nouveau bloc Data Loader pour extraire les données :

```python
import io
import pandas as pd
import requests

@data_loader
def load_commune_data(*args, **kwargs):
    """
    Charge les données des communes françaises
    """
    url = 'https://www.data.gouv.fr/fr/datasets/r/dbe8a621-a9c4-4bc3-9cae-be1699c5ff25'
    
    # Gestion des erreurs de requête
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erreur lors de la récupération des données : {e}")
    
    # Lecture avec gestion de l'encodage
    return pd.read_csv(io.StringIO(response.text), sep=',', encoding='utf-8')

@test
def test_output(output, *args) -> None:
    """
    Vérifie la validité des données
    """
    assert output is not None, 'Données non définies'
    assert 'code_postal' in output.columns, 'Colonne code_postal manquante'
    assert 'nom_commune_complet' in output.columns, 'Colonne nom_commune_complet manquante'
    assert 'nom_region' in output.columns, 'Colonne nom_region manquante'
```

```alert-info
L'utilisation de try/except permet de gérer proprement les erreurs de requête HTTP.
```

##### 2. Création du Transformer
Créez un bloc Transformer pour nettoyer et formater les données :

```python
@transformer
def transform_commune_data(data, *args, **kwargs):
    """
    Nettoie et formate les données des communes
    """
    # Sélection des colonnes nécessaires
    df_filtered = data[['code_postal', 'nom_commune_complet', 'nom_region']]
    
    # Mise en majuscules des noms de régions
    df_filtered['nom_region'] = df_filtered['nom_region'].str.upper()
    
    # Nettoyage des valeurs nulles ou vides
    df_filtered = df_filtered.dropna()
    
    # Vérification de l'encodage des caractères spéciaux
    df_filtered['nom_commune_complet'] = df_filtered['nom_commune_complet'].apply(
        lambda x: x.encode('utf-8').decode('utf-8')
    )
    
    return df_filtered

@test
def test_transform_output(output, *args) -> None:
    """
    Vérifie la transformation
    """
    assert output['nom_region'].str.isupper().all(), 'Certaines régions ne sont pas en majuscules'
    assert output.isna().sum().sum() == 0, 'Il reste des valeurs nulles'
```

```alert-info
La méthode dropna() supprime les lignes contenant des valeurs nulles. Si vous souhaitez les conserver, vous pouvez les remplacer par une valeur par défaut avec fillna().
```

##### 3. Configuration du Data Exporter
Créez un bloc Data Exporter pour sauvegarder les données :

```python
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path

@data_exporter
def export_commune_data(df: DataFrame, **kwargs) -> None:
    """
    Exporte les données vers PostgreSQL
    """
    # Configuration
    schema_name = 'public'  # ou votre schéma personnalisé
    table_name = 'communes_france'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,
            if_exists='replace',  # 'append' si vous voulez ajouter à une table existante
        )
```

##### 4. Vérification des résultats
Pour vérifier que tout fonctionne :

1. Connectez-vous à votre base PostgreSQL
2. Exécutez la requête suivante :
```sql
SELECT count(*) as total_communes,
       count(distinct nom_region) as total_regions
FROM communes_france;
```

#### Critères d'acceptation
- Les données sont correctement formatées
  - Toutes les régions sont en majuscules
  - Aucune valeur nulle dans les colonnes requises
  - Encodage UTF-8 vérifié
- Les données sont accessibles via un SGBD
  - La table 'communes_france' existe
  - Les données peuvent être requêtées
- Le pipeline est fonctionnel et peut être exécuté à nouveau
  - Tous les tests passent
  - Le pipeline s'exécute sans erreur
