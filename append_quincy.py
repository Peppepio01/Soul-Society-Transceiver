import json
import os
import shutil

db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"

new_weapons = [
    # YHWACH & STERN RITTERS (Using "Shikai" to mean "Reishi Weapon/Schrift" and "Bankai" to mean "Vollständig")
    {
        "id": "almighty",
        "name": "Reishi Broadsword & Medallion",
        "owner": "Yhwach",
        "shikai": { "image": "", "command": "Schrift: A - The Almighty", "description": "L'arma base di Yhwach è una possente e letale spada di Reishi scura. La sua vera abilità The Almighty gli consente di precognizzare e alterare letteralmente qualsiasi istante temporale futuro a suo piacimento assoluto distruttivo ed irreparabile dominando la disperazione letale incrollabile assoluta totalitaria ed asfissiante tremenda inesorabile immensa divina onnipotente schiacciante." },
        "bankai": { "name": "Assimilazione Reale", "image": "", "command": "Assorbi", "description": "Piuttosto che un Vollständig convenzionale, Yhwach si fonde col Re Spirito ottenendo innumerevoli tremendi letali invincibili colossali insormontabili occhi d'oscurità ed una coltre abissale immensa tangibile spietata ombrosa celatamente diabolica." }
    },
    {
        "id": "balance",
        "name": "Broadsword",
        "owner": "Jugram Haschwalth",
        "shikai": { "image": "", "command": "Schrift: B - The Balance", "description": "Un letale classico scudo e spadone colossale puro bilanciato fendente devoto. Il suo Schrift dirotta a suo avviso letalmente avverso e letalmente bilanciato la 'Sfortuna' avversaria invertendola o infierendo danni riflessivi raddoppiandoli sul nemico istantaneamente imperterrito regale indiscusso freddo scialbo mortale letale disarmante regius fedele colossale fatale." },
        "bankai": { "name": "Sconosciuto", "image": "", "command": "Nessuno", "description": "Il Grandmaster the Balance non ha mai necessità fiera ed indissolubile ineluttabile di sfoggiare la forma Vollständig data la sua assoluta letalità mortale spietata regale." }
    },
    {
        "id": "deathdealing",
        "name": "Arco di Reishi",
        "owner": "Askin Nakk Le Vaar",
        "shikai": { "image": "", "command": "Schrift: D - The Deathdealing", "description": "Un'arma semplice per nascondere il suo temibile calcolo di letalità. Regola e manipola microscopicamente a piacimento letale geniale il dosaggio tossico e le difese immunitarie di sangue o reiatsu del malcapitato tramutando una goccia nel più invalidante collassante avvelenato disumano intossicante mortifero fatale sadismo logico inesorabile ed asfissiante infallibile letale." },
        "bankai": { "name": "Vollständig: Hasshein", "image": "", "command": "Rilascia, Hasshein!", "description": "Sfoggia ali di molecole virali ed acquisisce infallibilmente totale diabolica immediata letale ed istintiva immunità letale assoluta ad ogni singolo tipo letale d'elemento spirituale con cui entra in letale asfissiante viscidamente letale contatto annullatore devastante e sprezzante." }
    },
    {
        "id": "explode",
        "name": "Sciabola",
        "owner": "Bambietta Basterbine",
        "shikai": { "image": "", "command": "Schrift: E - The Explode", "description": "La sua spada converte brutalmente letalmente subitamente immediatamente istantaneamente impietosamente spietatamente distruttivamente catastroficamente ogni singola reishi particella colpita disumanamente violenta impetuosa sadica rabbiosamente deflagrante letale letale. Non lancia bombe, trasforma ciò che tocca IN bombe incendiarie." },
        "bankai": { "name": "Vollständig", "image": "", "command": "Rilascia", "description": "Dalle ali bombardiere scatena incessantemente piogge letali d'assurda letalità e distruzione di sfere esplosive sterminanti sadiche infuocate folli a tappeto diabolico incenerente spietato apocalittico annichilente brutale colossale senza pietà assordante fatale." }
    },
    {
        "id": "x-axis",
        "name": "Diagram",
        "owner": "Lille Barro",
        "shikai": { "image": "", "command": "Schrift: X - The X-Axis", "description": "Un letale fucile da cecchino incallito infallibile imperterrito spietatamente silente infallibile che non spara affatto proiettili mortali ma letalmente cancella ed omette o oblitera irreversibilmente istantaneamente tutto lo spazio letalmente perforabile tra la canna ed il bersaglio mortale indistruttibile insormontabile assoluto chirurgicamente inenarrabile fatale spaventoso e fendente." },
        "bankai": { "name": "Vollständig: Jilliel", "image": "", "command": "Jilliel", "description": "Si trasforma in un cherubino mostruoso letalmente intoccabile divino imperterrito immune da attacchi materiali fisici, in un tripudio ineffabile d'ali celesti letali perforazioni cosmiche luminose radianti mortali onniscienti terrificanti sadicamente apocalittiche divine e teletrasporto insormontabile sfuggente immortale colossale piumato di luce insensata pura ineluttabilmente colpevole spietata letale annientatrice folgorante letale asfissiante fatale letale fiammante." }
    },
    # Missing Vice Captains & Sub-Captains
    {
        "id": "gonryomaru",
        "name": "Gonryōmaru",
        "owner": "Chōjirō Sasakibe",
        "shikai": { "image": "", "command": "Infilza", "description": "Lama simile ad un fioretto capace di scagliare fendenti fulminei, incrociati con saette taglienti. Si rivela un rapier rapido, letale ed elegantemente fedele che controlla elettroni fulminanti letali ad alta spietatezza formidabile assai rapida abbagliante folgorante dritto colpevole implacabile fendente impellente." },
        "bankai": { "name": "Kōkō Gonryō Rikyū", "image": "", "command": "Bankai, Kōkō Gonryō Rikyū!", "description": "Un mantello letalmente letalmente maestoso di potentissimo devastante incandescente incandescente brutale ed abbacinante abbagliante folgorante immenso tempestoso nubifragio di letali dardi e cupole elettriche scaricate potentissime formidabili a livello uragano mortifero imperdibile da nuvole cariche tempesta furiosa e pioggia ardente letale onnipresente d'insormontabile calore devastante inaudito formidabile incandescente spietatamente devoto leale asfissiante sfiancante immortale ed impuro apocalittico raggio elettrico in contrasto col pallido fulmine letale." }
    },
    {
        "id": "gegetsuburi",
        "name": "Gegetsuburi",
        "owner": "Marechiyo Ōmaeda",
        "shikai": { "image": "", "command": "Schiaccia", "description": "Lama a sfera chiodata gigante ed estremamente appuntita collegata a catena. Un'arma ingombrante contundente ignorante irruenta ma sorprendentemente rapida se lanciata abilmente furtivamente colposamente con destrezza pesante ingloriosa infame tagliente dirotta letale impenitente colossale ingannevole massiccia." },
        "bankai": { "name": "Non Ottenuto", "image": "", "command": "Nessuno", "description": "Non è in grado di rilasciare il Bankai finora." }
    },
    {
        "id": "itegumo",
        "name": "Itegumo",
        "owner": "Isane Kotetsu",
        "shikai": { "image": "", "command": "Corri Via", "description": "Divisa con tre punte divergenti asimmetriche frontali a spina. Arma orientata a difendersi intrappolando le armi da mischia in sfuggenti angolazioni freddamente affilate diaboliche distensive sfuggenti celestiali caute eleganti sfiancanti chirurgiche prevaricanti veloci letali ed estrose abbaglianti fedeli incrociate immancabili repentine taglienti letali taglienti." },
        "bankai": { "name": "Non Ottenuto", "image": "", "command": "Nessuno", "description": "Il suo utilizzo clinico Kaido surclassa la necessità offensiva del Bankai assente in lei." }
    },
    {
        "id": "shinken",
        "name": "Shinken Hakkyōken",
        "owner": "Nanao Ise",
        "shikai": { "image": "", "command": "Nessuno (Specchio Divino)", "description": "Un'antica spada sacra sprovvista di lama offensiva ereditata da famiglia Ise che riflette letalmente inalienabilmente divinamente ed assorbe specularmente infallibilmente ed ingolosamente inesorabilmente gli immensi ed asfissianti poteri o magie divine Kido rispedendoli apocalitticamente agli dei stessi spietatamente infallibilmente formidabilmente incrollabilmente celatamente implacabilmente divina fendeva colossale onnisciente." },
        "bankai": { "name": "Assente", "image": "", "command": "Nessuno", "description": "Essendo un manufatto mitologico divino, sfugge alle logiche di Bankai e Shikai puramente standard Shinigami." }
    }
]

try:
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    existing_ids = [z["id"] for z in db.get("zanpakuto", [])]
    for z in new_weapons:
        if z["id"] not in existing_ids:
            db["zanpakuto"].append(z)
            
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Aggiunti {len(new_weapons)} nuovi Equipaggiamenti Imperiali Quincy e Gotei!")
except Exception as e:
    print("Errore", e)
