import json
import urllib.request
import urllib.parse
import os

db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"

missing_s_characters = [
    {"id": "senjumaru", "name": "Senjumaru Shutara", "zanpakuto": "Shigarami (Filo)", "abilities": ["Tessitura Illusoria", "Creazione Oken"]},
    {"id": "shinji", "name": "Shinji Hirako", "zanpakuto": "Sakanade", "abilities": ["Inversione Ottica", "Maschera Hollow"]},
    {"id": "shunsui", "name": "Shunsui Kyōraku", "zanpakuto": "Katen Kyōkotsu", "abilities": ["Giochi Mortali", "Karamatsu Shinju"]},
    {"id": "shuhei", "name": "Shūhei Hisagi", "zanpakuto": "Kazeshini", "abilities": ["Falce Rotante", "Fushi no Kōjyō"]},
    {"id": "shukuro", "name": "Shūkurō Tsukishima", "zanpakuto": "Book of the End", "abilities": ["Manipolazione dei Ricordi"]},
    {"id": "shusuke", "name": "Shūsuke Amagai", "zanpakuto": "Raika", "abilities": ["Bakkōtō Sigillante", "Fuoco"]},
    {"id": "sui-feng", "name": "Sui Feng", "zanpakuto": "Suzumebachi", "abilities": ["Nigeki Kessatsu", "Shunkō", "Jakuhō Raikōben"]},
    {"id": "szayelaporro", "name": "Szayelaporro Granz", "zanpakuto": "Fornicarás", "abilities": ["Clonazione Voodoo", "Rinascita Parassitaria"]},
    {"id": "aizen", "name": "Sōsuke Aizen", "zanpakuto": "Kyōka Suigetsu", "abilities": ["Kanzen Saimin", "Kurohitsugi", "Hōgyoku", "Reiatsu Trascendentale"]}
]

try:
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
except FileNotFoundError:
    print("Errore: db.json non trovato.")
    exit(1)

# Remove any existing versions to avoid duplicates
existing_ids = [c["id"] for c in db["characters"]]
for char in missing_s_characters:
    if char["id"] in existing_ids:
        continue
        
    # Query the MediaWiki API for the Italian Fandom
    title = urllib.parse.quote(char["name"].replace(" ", "_"))
    url = f"https://bleach.fandom.com/it/api.php?action=query&prop=extracts&exintro=true&explaintext=true&titles={title}&format=json"
    
    bio_text = "Nessuna biografia trovata sul wiki."
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data["query"]["pages"]
            page_id = list(pages.keys())[0]
            if page_id != "-1":
                extract = pages[page_id].get("extract", "")
                if extract:
                    # Take the first paragraph
                    bio_text = extract.split('\n')[0].strip()
                    if len(bio_text) > 400:
                        bio_text = bio_text[:397] + "..."
    except Exception as e:
        print(f"Impossibile connettersi a Fandom per {char['name']}: {e}")
        bio_text = "Informazione estratta dagli archivi segreti del Gotei 13 (Connessione al Wiki fallita)."

    print(f"Aggiunto: {char['name']} - {bio_text[:50]}...")
    
    db["characters"].append({
        "id": char["id"],
        "name": char["name"],
        "image": "https://i.imgur.com/8Q5YIqF.jpeg",
        "zanpakuto": char["zanpakuto"],
        "abilities": char["abilities"],
        "affiliation": "Vedi Fandom IT",
        "bio": bio_text
    })

# Sort alphabetically by name to keep it clean, as user likes alphabetized lists
db["characters"].sort(key=lambda x: x["name"])

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Aggiornamento del Database completato con successo dai server Fandom Italiani!")
