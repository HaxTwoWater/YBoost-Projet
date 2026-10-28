# YBoost – Prédiction de matchs League of Legends

Projet Yboost B2 IA & Data (Ynov Toulouse). L'objectif est de prédire le vainqueur d'un match de League of Legends professionnel, puis de simuler une compétition à partir de ces prédictions.

## Prérequis

- Python 3.10 ou plus récent
- Environ 1 Go d'espace disque libre pour les données

## Installation

```bash
git clone https://github.com/HaxTwoWater/YBoost-Projet.git
cd YBoost-Projet
python -m venv .venv
```

Activer l'environnement virtuel :

- Windows : `.venv\Scripts\activate`
- macOS / Linux : `source .venv/bin/activate`

Puis installer les dépendances :

```bash
pip install -r requirements.txt
```

## Récupérer les données

```bash
python src/download.py
```

Le script lit le contenu du dossier Google Drive d'Oracle's Elixir et télécharge chaque CSV (un par année, depuis 2014) dans `data/raw/`. Une nouvelle année publiée par Oracle's Elixir est donc récupérée automatiquement, sans modifier le script.

- Les fichiers déjà présents ne sont pas retéléchargés.
- Le fichier de l'année en cours est toujours retéléchargé, car il est mis à jour chaque jour.
- Pour tout retélécharger : `python src/download.py --force`

Google Drive limite parfois le nombre de téléchargements d'un fichier. Dans ce cas, le script passe au fichier suivant et affiche la liste des échecs à la fin : il suffit de le relancer plus tard.

Le premier téléchargement prend quelques minutes (environ 850 Mo au total).

## Vérifier les données

```python
import pandas as pd

df = pd.read_csv("data/raw/2025_LoL_esports_match_data_from_OraclesElixir.csv", low_memory=False)
print(df.shape)
print(df.groupby("gameid").size().value_counts())
```

Résultat attendu : 165 colonnes et 12 lignes par partie (10 lignes joueurs et 2 lignes équipe, identifiées par `position == "team"`).

## Les données

| | |
|---|---|
| Source | [Oracle's Elixir](https://oracleselixir.com/tools/downloads), par Tim Sevenhuysen |
| Contenu | Matchs professionnels de League of Legends, un fichier par année |
| Période | 2014 à aujourd'hui (le fichier de l'année en cours est mis à jour quotidiennement) |
| Colonnes principales | `gameid`, `date`, `league`, `patch`, `side`, `teamname`, `teamid`, `position`, `result`, `datacompleteness` |

Les données ne sont pas versionnées (`data/` est dans le `.gitignore`) : chaque membre les récupère avec `src/download.py`.

Certaines parties sont marquées `datacompleteness = partial`, ce qui signifie que des statistiques y sont manquantes. Elles seront traitées lors de la préparation des données.

## Structure du projet

```
YBoost-Projet/
├── app.py               # dashboard Streamlit (à venir)
├── requirements.txt     # dépendances Python
├── data/
│   ├── raw/             # fichiers téléchargés, non modifiés
│   └── processed/       # tableaux préparés
├── notebooks/           # exploration
└── src/
    └── download.py      # téléchargement des données
```
