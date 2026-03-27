import json
import urllib.request
import urllib.parse
import re
import os
import time

db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"
zanp_dir = "c:/Users/giuse/Desktop/Bleach/assets/zanpakuto"
os.makedirs(zanp_dir, exist_ok=True)

with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

def fetch_bing_image_urls(query):
    # Appending hd and official to query filters to force high quality
    url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query + " high quality") + "&first=1"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    })
    urls = []
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        found = re.findall(r'murl(?:&quot;|"):?(?:&quot;|")?(https?[^&"]+?\.(?:jpg|png|jpeg))(?:&quot;|")?', html, re.IGNORECASE)
        
        # PRIORITIZE OFFICIAL WIKI/FANDOM HIGH-RES IMAGES FIRST
        for u in found:
            if "wikia.nocookie.net" in u or "fandom.com" in u:
                # Remove scale down parameters from wikia urls to get raw original size!
                u = re.sub(r'/revision/latest/scale-to-width-down/\d+', '', u)
                u = re.sub(r'/revision/latest\?cb=\d+', '', u)
                urls.append(u)
        # Add the rest
        for u in found:
            if "wikia.nocookie.net" not in u and "fandom.com" not in u:
                urls.append(u)
    except Exception as e:
        print(f"Errore connessione Bing: {e}")
    
    seen = set()
    return [x for x in urls if not (x in seen or seen.add(x))]

def download_image_robust(urls, save_path):
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': 'https://bleach.fandom.com/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site'
            })
            with urllib.request.urlopen(req, timeout=8) as response:
                if response.status == 200:
                    with open(save_path, 'wb') as out_file:
                        out_file.write(response.read())
                    return True
        except Exception:
            continue
    return False

arrancars = ["Starrk", "Baraggan", "Harribel", "Ulquiorra", "Nnoitra", "Grimmjow", "Zommari", "Szayelaporro", "Aaroniero", "Yammy", "Dordoni", "Emilou"]
quincies = ["Yhwach", "Jugram", "Askin", "Bambietta", "Lille"]

print("Inizia il recupero Immagini HD Ufficiali...")

for z in db.get("zanpakuto", []):
    z_id = z["id"]
    owner = z.get("owner", "")
    z_name = z.get("name", "")
    bankai_name = z.get("bankai", {}).get("name", "")
    
    shikai_path = os.path.join(zanp_dir, f"{z_id}_shikai.jpg")
    bankai_path = os.path.join(zanp_dir, f"{z_id}_bankai.jpg")
    
    if any(a in owner for a in arrancars):
        query_shikai = f"{owner} bleach anime official art"
        query_bankai = f"{owner} resurreccion form bleach anime official"
    elif any(q in owner for q in quincies):
        query_shikai = f"{owner} bleach anime official"
        query_bankai = f"{owner} vollstandig bleach anime form official"
    else:
        query_shikai = f"{owner} {z_name} sword blade bleach anime full"
        query_bankai = f"{owner} {bankai_name} bankai bleach anime official" if bankai_name and "Nessuno" not in bankai_name else f"{owner} bleach anime"

    print(f"[{z_name}] (HD) Cerco Shikai/Base...")
    urls_shikai = fetch_bing_image_urls(query_shikai)
    if download_image_robust(urls_shikai, shikai_path):
        print(f" -> Successo! (Alta Qualità)")
    time.sleep(0.5)
    
    if "Nessuno" not in bankai_name and "Assente" not in bankai_name and "Non Ottenuto" not in bankai_name:
        print(f"[{z_name}] (HD) Cerco Bankai/Resurrección...")
        urls_bankai = fetch_bing_image_urls(query_bankai)
        if download_image_robust(urls_bankai, bankai_path):
            print(f" -> Successo! (Alta Qualità)")
        time.sleep(0.5)

print("Scraping Alta Qualità Concluso!")
