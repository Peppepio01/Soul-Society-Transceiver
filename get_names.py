import json

with open('c:/Users/giuse/Desktop/Bleach/data/db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

targets = ["Marechiyo", "Isane", "Nanao", "Dordoni", "Emilou", "Rangiku", "Yhwach", "Jugram", "Askin", "Bambietta", "Lille", "Sasakibe", "Chojiro", "Chōjirō"]
out = []

for z in db.get("zanpakuto", []):
    # Check if the owner matches one of the targets
    if any(t.lower() in z.get("owner", "").lower() for t in targets):
        out.append(f"{z.get('name', 'Sconosciuto')}:\n -> Shikai: {z['id']}_shikai.jpg\n -> Bankai/Rilascio: {z['id']}_bankai.jpg\n")

with open('c:/Users/giuse/Desktop/Bleach/names_output.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))
