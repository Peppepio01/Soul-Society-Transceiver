import urllib.request
import urllib.parse
import re
import os

save_path = "c:/Users/giuse/Desktop/Bleach/assets/badge.png"

def get_badge():
    print("Cerco il Pass del Sostituto Shinigami...")
    url = "https://www.bing.com/images/search?q=" + urllib.parse.quote("Bleach Substitute Shinigami Badge Pass official transparent png high quality") + "&first=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        urls = re.findall(r'murl(?:&quot;|"):?(?:&quot;|")?(https?[^&"]+?\.(?:png))(?:&quot;|")?', html, re.IGNORECASE)
        
        for img_url in urls:
            try:
                print(f"Provo a scaricare: {img_url}")
                req2 = urllib.request.Request(img_url, headers={
                    'User-Agent': 'Mozilla/5.0',
                    'Referer': 'https://bleach.fandom.com/'
                })
                with urllib.request.urlopen(req2, timeout=5) as response:
                    with open(save_path, "wb") as f:
                        f.write(response.read())
                print("Favicon scaricata con successo!")
                return
            except Exception:
                continue
    except Exception as e:
        print("Errore globale:", e)

get_badge()
