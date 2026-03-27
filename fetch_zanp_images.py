from duckduckgo_search import DDGS
import json
import urllib.request
import os
import time

zanp_dir = "c:/Users/giuse/Desktop/Bleach/assets/zanpakuto"
db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"

try:
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
except Exception as e:
    print("Errore lettura DB:", e)
    exit(1)

ddgs = DDGS()

print("Inizio rimpiazzo avatar personaggi con foto VERE delle armi Zanpakuto...")

for z in db.get("zanpakuto", []):
    z_id = z["id"]
    name = z["name"]
    shikai_path = os.path.join(zanp_dir, f"{z_id}_shikai.jpg")
    bankai_path = os.path.join(zanp_dir, f"{z_id}_bankai.jpg")
    
    # Precise query strictly for the sword
    if "Resurrecci" in name:
        query = f"Bleach {name.split(' ')[0]} espada form weapon anime"
    else:
        query = f"Bleach {name} zanpakuto sword anime"
        
    print(f"\nCercando arma vera: {query}...")
    
    try:
        results = list(ddgs.images(query, max_results=1, safesearch="off"))
        if results:
            img_url = results[0]["image"]
            print(f"Trovata: {img_url[:60]}")
            
            # Download Image
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            try:
                data = urllib.request.urlopen(req, timeout=8).read()
                # Overwrite the character fallback images with the real sword image
                with open(shikai_path, "wb") as f:
                    f.write(data)
                with open(bankai_path, "wb") as f:
                    f.write(data)
                print(f"Scaricata con successo: {z_id}")
            except Exception as e:
                print(f"URL {img_url[:30]} fallito, skip. Errore: {e}")
        else:
            print("Nessun risultato DDG trovato per", name)
    except Exception as e:
        print(f"DDG Search Error per {name}: {e}")
        
    time.sleep(2) # Prevent rate limiting block from Bing/DDG
    
print("\n!!! FINITO DOWNLOAD VERE ARMI ZANPAKUTO !!!")
print("Ricarica l'Arsenale nella Web App per vederle!")
