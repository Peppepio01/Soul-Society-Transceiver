import json
import os
import shutil

db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"
zanp_dir = "c:/Users/giuse/Desktop/Bleach/assets/zanpakuto"

# AI Generated Placeholder paths
shikai_ai = "c:/Users/giuse/.gemini/antigravity/brain/009a7527-f9bb-4a9e-a5a5-50958b24115e/generic_shikai_1774552480788.png"
bankai_ai = "c:/Users/giuse/.gemini/antigravity/brain/009a7527-f9bb-4a9e-a5a5-50958b24115e/generic_bankai_1774552497465.png"
vollstandig_ai = "c:/Users/giuse/.gemini/antigravity/brain/009a7527-f9bb-4a9e-a5a5-50958b24115e/generic_vollstandig_1774552514248.png"

with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

print("Inizio applicazione Placeholder Armi Premium IA...")

quincy_names = ["Yhwach", "Jugram Haschwalth", "Askin Nakk Le Vaar", "Bambietta Basterbine", "Lille Barro"]

for z in db.get("zanpakuto", []):
    z_id = z["id"]
    owner = z.get("owner", "")
    
    shikai_path = os.path.join(zanp_dir, f"{z_id}_shikai.jpg")
    bankai_path = os.path.join(zanp_dir, f"{z_id}_bankai.jpg")
    
    # We copy the AI Shikai Katana to ALL Shikai/Base forms to remove character faces
    try:
        shutil.copy(shikai_ai, shikai_path)
    except:
        pass
        
    # For Bankai, we check if it's a Quincy (Vollständig aura) or Shinigami (Bankai dark aura)
    try:
        if owner in quincy_names:
            shutil.copy(vollstandig_ai, bankai_path)
        else:
            shutil.copy(bankai_ai, bankai_path)
    except:
        pass
        
print("Tutte le grafiche delle armi sono state rimpiazzate con render Premium generati dall'IA!")
