import gdown
from pathlib import Path

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)

FICHIERS = {
    2014: "12syQsRH2QnKrQZTQQ6G5zyVeTG2pAYvu",
    2015: "1qyckLuw0-hJM8XqFhlV9l1xAbr3H78T_",
    2016: "1muyfpaIqk8_0BFkgLCWXDGNgWSXoPBwG",
    2017: "11fx3nNjSYB0X8vKxLAbYOrS2Bu6avm9A",
    2018: "1GsNetJQOMx0QJ6_FN8M1kwGvU_GPPcPZ",
    2019: "11eKtScnZcpfZcD3w3UrD7nnpfLHvj9_t",
    2020: "1dlSIczXShnv1vIfGNvBjgk-thMKA5j7d",
    2021: "1fzwTTz77hcnYjOnO9ONeoPrkWCoOSecA",
    2022: "1EHmptHyzY8owv0BAcNKtkQpMwfkURwRy",
    2023: "1XXk2LO0CsNADBB1LRGOV5rUpyZdEZ8s2",
    2024: "1IjIEhLc9n8eLKeY-yh_YigKVWbhgGBsN",
    2025: "1v6LRphp2kYciU4SXp0PCjEMuev1bDejc",
}

for annee, file_id in FICHIERS.items():
    sortie = RAW / f"{annee}_LoL_esports_match_data.csv"
    if sortie.exists():
        print(f"{annee} déjà là")
        continue
    gdown.download(id=file_id, output=str(sortie), quiet=False)