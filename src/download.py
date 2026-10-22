import gdown
from pathlib import Path

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)

FICHIERS = {
    2025: "ID_A_REMPLIR",
}

for annee, file_id in FICHIERS.items():
    sortie = RAW / f"{annee}_LoL_esports_match_data.csv"
    if sortie.exists():
        print(f"{annee} déjà là")
        continue
    gdown.download(id=file_id, output=str(sortie), quiet=False)