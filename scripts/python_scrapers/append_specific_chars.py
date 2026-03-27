import json

db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"

new_chars = [
    {
      "id": "don_kanonji",
      "name": "Don Kanonji",
      "image": "assets/characters/don_kanonji.jpg",
      "zanpakuto": "Nessuna",
      "abilities": ["Kanonball", "Spiriti Are Always With You"],
      "affiliation": "Umano",
      "bio": "Un bizzarro e celebre medium televisivo adorato dalle folle, diventato alleato degli Shinigami grazie all'incontro stramparato con Ichigo. Anche se goffo e pittoresco, nasconde un coraggio insospettabile."
    },
    {
      "id": "dordoni",
      "name": "Dordoni Alessandro Del Socaccio",
      "image": "assets/characters/dordoni.jpg",
      "zanpakuto": "Giralda",
      "abilities": ["Cero", "Bala", "Resurrección: Giralda"],
      "affiliation": "Privaron Espada (Arrancar No. 103)",
      "bio": "Un ex-Espada degradato ai Privaron. Veste come un nobile ed ha una mentalità molto eccentrica e galante. Usa il vento ciclonico in battaglia coi calcagni per devastare l'avversario."
    },
    {
      "id": "emilou_apacci",
      "name": "Emilou Apacci",
      "image": "assets/characters/emilou_apacci.jpg",
      "zanpakuto": "Cierva",
      "abilities": ["Cero", "Quimera Parca"],
      "affiliation": "Arrancar (Fracción di Harribel)",
      "bio": "Una delle tre Fracción della Tercera Espada Tia Harribel. Testa calda, aggressiva e leale fino alla morte, indossa un copricapo d'osso che ricorda un corno letale e veloce."
    },
    {
      "id": "ran_tao",
      "name": "Ran Tao",
      "image": "assets/characters/ran_tao.jpg",
      "zanpakuto": "N/D",
      "abilities": ["Kido di altissimo livello", "Ricerca spirituale"],
      "affiliation": "S.R.D.I (Ex Ricercatrice Shinigami)",
      "bio": "Brillante e pentita ricercatrice della Soul Society e creatrice dei Bount. Possiede un intelletto acuto e un sigillo mistico che le impedisce di usare liberamente i suoi massimi poteri spirituali."
    },
    {
      "id": "rangiku_matsumoto",
      "name": "Rangiku Matsumoto",
      "image": "assets/characters/rangiku_matsumoto.jpg",
      "zanpakuto": "Haineko",
      "abilities": ["Shunpo", "Kido", "Bakuhatsu Haineko"],
      "affiliation": "Gotei 13 (Luogotenente Decima Divisione)",
      "bio": "La bellissima, pigra ma letalmente fiera Luogotenente del Capitano Hitsugaya. Usa la sua spada che si sbriciola in letali ceneri taglienti volanti per danzare tra orde di nemici sfiancandoli."
    },
    {
      "id": "soul_king",
      "name": "Il Re delle Anime (Reiō)",
      "image": "assets/characters/soul_king.jpg",
      "zanpakuto": "Il Potere Assoluto",
      "abilities": ["The Almighty (Ancestrale)", "Chiave dei Mondi"],
      "affiliation": "Deità della Soul Society",
      "bio": "Il misterioso e apatico dio reggente attorno a cui è imperniato l'equilibrio dei Tre Mondi (Soul Society, Hueco Mundo, Mondo Umano). È tenuto incapsulato in letargo dai Capitani Generali e dalla Squadra 0."
    },
    {
      "id": "reiryoku_concept",
      "name": "Reiryoku (Potere Spirituale)",
      "image": "assets/characters/reiryoku_concept.jpg",
      "zanpakuto": "Concetto Energetico",
      "abilities": ["Manipolazione Reiatsu", "Alimentazione Kido"],
      "affiliation": "Energia Base",
      "bio": "Non è un vero spirito bensì l'unità fondamentale del cosmo spirituale, la forza intrinseca dell'anima che permette agli Shinigami e agli Hollow di trascendere lo spazio e impiegare arti sovrumane distruttive."
    }
]

new_weapons = [
    {
        "id": "giralda",
        "name": "Giralda",
        "owner": "Dordoni",
        "shikai": { "image": "", "command": "Forma Base", "description": "Spada bastone Arrancar. Molto elegante." },
        "bankai": { "name": "Resurrecciòn: Giralda", "image": "", "command": "Gira!", "description": "Trasforma le gambe in colossali stivali di tornado cicloni letali vorticosi d'aria solida contundente capaci di disintegrare massi ed acciaio." }
    },
    {
        "id": "cierva",
        "name": "Cierva",
        "owner": "Emilou Apacci",
        "shikai": { "image": "", "command": "Forma Base", "description": "Bracciali muniti d'anelli letali estrosi." },
        "bankai": { "name": "Resurrecciòn: Cierva", "image": "", "command": "Infilza", "description": "Una veste di pelle ferrea armata, veloce contundente scattante rapace e mortifera. Può sacrificare il braccio con i compagni per evocare Ayon, la viverna bestiale apocalittica inarrestabile." }
    },
    {
        "id": "haineko",
        "name": "Haineko",
        "owner": "Rangiku Matsumoto",
        "shikai": { "image": "", "command": "Ringhia", "description": "La lama si scompone disperdendosi nell'aria come polvere o cenere invisibile fatale acuta e scattante. Rangiku usa il pomello per scatenare graffi multipli letali contundenti di cenere ferrea affilata da ogni direzione disperdendo nemici a stormi interi infami." },
        "bankai": { "name": "Non Ottenuto", "image": "", "command": "Nessuno", "description": "Rangiku confida nella versatilità del suo Shikai." }
    }
]

try:
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    existing_chars = [c["id"] for c in db.get("characters", [])]
    for c in new_chars:
        if c["id"] not in existing_chars:
            db["characters"].append(c)
            
    existing_z_ids = [z["id"] for z in db.get("zanpakuto", [])]
    for z in new_weapons:
        if z["id"] not in existing_z_ids:
            db["zanpakuto"].append(z)
            
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Aggiunti {len(new_chars)} nuovi Profili (Personaggi/Entità) e le rispettive Armi/Attributi!")
except Exception as e:
    print("Errore", e)
