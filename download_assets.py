import json
import urllib.request
import urllib.parse
import os
import time

db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"
char_dir = "c:/Users/giuse/Desktop/Bleach/assets/characters"
zanp_dir = "c:/Users/giuse/Desktop/Bleach/assets/zanpakuto"

os.makedirs(char_dir, exist_ok=True)
os.makedirs(zanp_dir, exist_ok=True)

with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

# Fallback reliable image (A cool Bleach generic logo/background)
FALLBACK_IMG = "https://i.imgur.com/8Q5YIqF.jpeg"

def download_image(url, save_path):
    if os.path.exists(save_path):
        return True # Già scaricata
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(save_path, 'wb') as out_file:
                out_file.write(response.read())
        return True
    except Exception as e:
        print(f"Errore download {url}: {e}")
        return False

def get_wiki_image_url(query_title):
    title = urllib.parse.quote(query_title.replace(" ", "_"))
    api_url = f"https://bleach.fandom.com/it/api.php?action=query&titles={title}&prop=pageimages&pithumbsize=600&format=json"
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data["query"]["pages"]
            page_id = list(pages.keys())[0]
            if page_id != "-1" and "thumbnail" in pages[page_id]:
                return pages[page_id]["thumbnail"]["source"]
    except Exception:
        pass
    
    # Try English Wiki as fallback if Italian wiki lacks the image
    api_url_en = f"https://bleach.fandom.com/api.php?action=query&titles={title}&prop=pageimages&pithumbsize=600&format=json"
    try:
        req = urllib.request.Request(api_url_en, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data["query"]["pages"]
            page_id = list(pages.keys())[0]
            if page_id != "-1" and "thumbnail" in pages[page_id]:
                return pages[page_id]["thumbnail"]["source"]
    except Exception:
        pass

    return FALLBACK_IMG

print("Inizio il recupero automatico delle immagini. Questa operazione richiederà qualche minuto...")

# 1. Download Characters
print("\n--- Download Personaggi ---")
for char in db.get("characters", []):
    c_id = char["id"]
    save_path = os.path.join(char_dir, f"{c_id}.jpg")
    
    # Check if already done
    if os.path.exists(save_path):
        continue
        
    img_url = get_wiki_image_url(char["name"])
    print(f"[{char['name']}] -> Trovata: {img_url[:40]}...")
    
    success = download_image(img_url, save_path)
    if not success and img_url != FALLBACK_IMG:
        download_image(FALLBACK_IMG, save_path)
    time.sleep(0.1) # Be gentle to API

# 2. Download Zanpakuto (We search the owner to get a cool image, or the Zanpakuto name itself)
print("\n--- Download Zanpakuto ---")
for zanp in db.get("zanpakuto", []):
    z_id = zanp["id"]
    z_name = zanp["name"]
    owner = zanp.get("owner", "")
    
    shikai_path = os.path.join(zanp_dir, f"{z_id}_shikai.jpg")
    bankai_path = os.path.join(zanp_dir, f"{z_id}_bankai.jpg")
    
    # Try fetching the specific Zanpakuto spirit/sword from Wiki English (usually structured better)
    img_url_shikai = get_wiki_image_url(z_name)
    if img_url_shikai == FALLBACK_IMG:
        # Fallback to owner's image if specific sword image isn't found
        img_url_shikai = get_wiki_image_url(owner)
        
    # We will just duplicate the image for Bankai if we can't search specifically for Bankai forms easily
    # Users can manually replace the Bankai images later if they want a specific frame.
    img_url_bankai = img_url_shikai 
    
    print(f"[{z_name} (Shikai)] -> Trovata: {img_url_shikai[:40]}...")
    download_image(img_url_shikai, shikai_path)
    
    print(f"[{z_name} (Bankai)] -> Trovata: {img_url_bankai[:40]}...")
    download_image(img_url_bankai, bankai_path)
    
    time.sleep(0.1)

print("\n!!! TUTTE LE IMMAGINI SONO STATE SCARICATE E SALVATE LOCALMENTE !!!")
