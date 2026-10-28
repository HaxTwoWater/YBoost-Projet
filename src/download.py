import argparse
from datetime import date
from pathlib import Path

import gdown

# Dossier Google Drive public d'Oracle's Elixir (un CSV par année)
DOSSIER_ID = "1gLSw0RLjBbtaNy0dgnGQDAZOHIgCe-HH"
RAW = Path("data/raw")


def lister_fichiers():
    """Renvoie la liste des CSV présents dans le dossier Drive, sans rien télécharger."""
    fichiers = gdown.download_folder(id=DOSSIER_ID, skip_download=True, quiet=True)
    return [f for f in fichiers if f.path.endswith(".csv")]


def main():
    parser = argparse.ArgumentParser(description="Télécharge les données Oracle's Elixir.")
    parser.add_argument("--force", action="store_true", help="retélécharge tous les fichiers")
    args = parser.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    annee_en_cours = str(date.today().year)
    echecs = []

    for fichier in lister_fichiers():
        sortie = RAW / fichier.path
        # Le fichier de l'année en cours est mis à jour chaque jour : on le reprend toujours
        a_jour = sortie.exists() and not fichier.path.startswith(annee_en_cours)
        if a_jour and not args.force:
            print(f"{fichier.path} déjà là")
            continue
        try:
            gdown.download(id=fichier.id, output=str(sortie), quiet=False)
        except gdown.exceptions.FileURLRetrievalError:
            # Google Drive limite parfois les téléchargements : on passe au suivant
            echecs.append(fichier.path)

    if echecs:
        print("\nÉchec (quota Google Drive, réessayer plus tard) :")
        for nom in echecs:
            print(f"  - {nom}")


if __name__ == "__main__":
    main()
