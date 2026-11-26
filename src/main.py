from datetime import datetime
import json
from pathlib import Path
import subprocess

import retirejs


file_advisories = {}
# direct files
for fichier_js in Path("/app/mnt/").rglob('*.js'):
    # On s'assure que c'est bien un fichier (et non un dossier nommé .js)
    if fichier_js.is_file():
        try:
            # Lecture du contenu du fichier
            contenu = fichier_js.read_text(encoding='utf-8', errors='ignore')
            returns = retirejs.scan_file_content(contenu)
            if returns:
                file_advisories["." + str(fichier_js)[8:]] = returns
            
        except Exception as e:
            print(f"Erreur lors de la lecture de {fichier_js}: {e}")

filename = datetime.now().strftime("/app/output/files_%Y-%m-%d_%H-%M-%S.json")
with open(filename, "w", encoding="utf-8") as f:
    json.dump(file_advisories, f, indent=2, ensure_ascii=False)


# linked files
pattern = r'https?://[^ "]+\.js'

result = subprocess.run(
    ['grep', '-rI', '-E', '-o', pattern, "/app/mnt/"],
    capture_output=True, text=True
)

urls_by_file = {}
for line in result.stdout.splitlines():
    # grep -o affiche "fichier:url"
    if ':' in line:
        filename, url = line.split(':', 1)
        relative_filename = "./" + filename[9:]
        scan = retirejs.scan_endpoint(url)
        if scan:
            if not relative_filename in urls_by_file:
                urls_by_file[relative_filename] = {}
            urls_by_file[relative_filename][url] = scan

filename = datetime.now().strftime("/app/output/linked_%Y-%m-%d_%H-%M-%S.json")
with open(filename, "w", encoding="utf-8") as f:
    json.dump(urls_by_file, f, indent=2, ensure_ascii=False)



