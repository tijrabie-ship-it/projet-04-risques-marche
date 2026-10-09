# Projet 04 — Risques de marché liés à la mourabaha

Projet académique développé en Python pour estimer les prix automobiles et illustrer les risques de marché liés au financement par mourabaha.

## Composantes du projet

### 1. Notebook d’analyse : so9.ipynb

Le notebook utilise le fichier `car_market_data.csv`, qui contient 1 000 observations et les variables suivantes :

- Marque du véhicule.
- Année de fabrication.
- Kilométrage.
- Type de carburant.
- Prix actuel du marché, utilisé comme variable cible.

Les variables catégorielles sont transformées par One-Hot Encoding. Un modèle Random Forest de 100 arbres est entraîné sur 80 % des observations et évalué sur les 20 % restantes à l’aide du MAE et du R².

Le notebook comprend également :

- Une fonction comparant le prix d’achat proposé au prix prédit.
- Une simulation de baisse des prix de marché, illustrée par un scénario de baisse de 20 %.

### 2. Application interactive : app.py

L’application Streamlit entraîne un modèle Random Forest sur 12 exemples automobiles intégrés directement dans le code.

L’utilisateur renseigne la marque, le modèle, l’année, le kilométrage et le prix d’achat proposé. Il sélectionne également un scénario économique appliquant un coefficient au prix prédit :

- Récession forte : 0,80.
- Récession légère : 0,90.
- Marché stable : 1,00.
- Inflation légère : 1,05.
- Inflation élevée : 1,15.

L’application compare ensuite le prix proposé à l’estimation ajustée et affiche un niveau de risque selon les seuils définis dans le code.

L’application et le notebook utilisent des données d’entraînement et des seuils de décision distincts. L’application ne charge pas le modèle entraîné dans le notebook ni le fichier CSV.

## Fichiers

- `app.py` : application interactive Streamlit.
- `so9.ipynb` : entraînement, évaluation et simulation de stress.
- `car_market_data.csv` : données utilisées par le notebook.
- `requirements.txt` : dépendances nécessaires.

## Installation

Depuis le dossier du projet :

```bash
python -m pip install -r requirements.txt
```

## Lancement de l’application

```bash
python -m streamlit run app.py
```

## Exécution du notebook

Depuis le même dossier :

```bash
jupyter notebook
```

Ouvrir `so9.ipynb` et exécuter les cellules dans leur ordre. Le fichier `car_market_data.csv` doit rester dans le même dossier que le notebook.

## Portée

Ce projet constitue une démonstration académique. Les scénarios économiques reposent sur des coefficients prédéfinis. Les résultats de l’application, entraînée sur un échantillon limité, nécessitent une validation sur des données représentatives avant toute utilisation opérationnelle.
