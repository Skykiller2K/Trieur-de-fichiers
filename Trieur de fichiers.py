from pathlib import Path

CUR_DIR = Path(__file__).parent

CLASSEMENT = {".mp3":"Musique",".wav":"Musique",".flac":"Musique",
".avi":"Videos",".mp4":"Videos",".gif":"Videos",
".bmp":"Images",".png":"Images",".jpg":"Images",
".txt":"Documents",".pptx":"Documents",".csv":"Documents",".xls":"Documents",".odp":"Documents",".pages":"Documents"}

for key in CLASSEMENT:
    for item in CUR_DIR.iterdir():
        if item.is_file() and item.suffix != ".py":
            if item.suffix == key:
                dossier = CUR_DIR / CLASSEMENT[key]
                dossier.mkdir(exist_ok=True)
                item.rename(dossier / item.name)  
for item in CUR_DIR.iterdir():
    if item.is_file() and item.suffix != ".py":                    
        dossier = CUR_DIR / "Divers"
        dossier.mkdir(exist_ok=True)
        item.rename(dossier / item.name)