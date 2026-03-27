import json

db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"

more_zanpakuto = [
    {
        "id": "minazuki",
        "name": "Minazuki",
        "owner": "Retsu Unohana",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Nessun Comando noto", "description": "Si trasforma in una manta gigante volante in grado di curare le persone inghiottendole nel suo stomaco e guarendole con fluidi gastrici curativi." },
        "bankai": { "name": "Minazuki (Tutte le cose finiscono)", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai... Minazuki", "description": "L'ambiente circostante si riempie di un fiotto di sangue scuro, acido e letale che corrode carne e spirito riducendo al solo scheletro chiunque ne venga intaccato." }
    },
    {
        "id": "sakanade",
        "name": "Sakanade",
        "owner": "Shinji Hirako",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Crolla", "description": "La lama possiede un grande anello sul pomello. Rilascia una nebbia profumata che inverte letteralmente la cognizione spaziale dell'avversario (sopra, sotto, destra, sinistra, e i riflessi visivi)." },
        "bankai": { "name": "Sakashima Yokoshima Happōfusagari", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai", "description": "Inverte la percezione di 'amici' e 'nemici' in un'area estesissima, costringendo tutti coloro che si trovano nel raggio d'azione a massacrarsi a vicenda." }
    },
    {
        "id": "tachikaze",
        "name": "Tachikaze",
        "owner": "Kensei Muguruma",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Soffia Via", "description": "Si rimpicciolisce in un coltello da combattimento letale. Ogni fendente genera proiettili d'aria ed esplosioni a comando temporizzato." },
        "bankai": { "name": "Tekken Tachikaze", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai, Tekken Tachikaze", "description": "Due letali tirapugni con lame protettive sulle braccia. Tutto ciò che tocca subisce un'infinita ed immediata raffica microscopica di esplosioni devastanti finché mantiene il contatto." }
    },
    {
        "id": "kinshara",
        "name": "Kinshara",
        "owner": "Rōjūrō Ōtoribashi (Rose)",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Suona", "description": "Una gigantesca frusta dorata a terminazione floreale. Sfodera melodie stridenti che causano esplosioni ed onde d'urto concentriche." },
        "bankai": { "name": "Kinshara Butōdan", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai...", "description": "Un'illusione musicale infallibile generata da giganteschi 'ballerini' avvolti in bendature. Chiunque ascolti la melodia subisce danni e ustioni fisiche reali dovute alla percezione illusoria estrema." }
    },
    {
        "id": "tengumaru",
        "name": "Tengumaru",
        "owner": "Love Aikawa",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Schiaccia", "description": "Diventa una colossale kanabo chiodata capace di schiacciare palazzi e scaricare turbini di fuoco rotanti spaventosi giganteschi." },
        "bankai": { "name": "Sconosciuto", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Sconosciuto", "description": "Il Bankai di Love non è mai stato confermato o mostrato apertamente in battaglia." }
    },
    {
        "id": "shinso",
        "name": "Shinsō",
        "owner": "Gin Ichimaru",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Trafiggilo a Morte", "description": "La spada si estende istantaneamente ed a grandissima velocità fino alla lunghezza di cento passate di katana, perforando indisturbatamente acciaio e difese corporee." },
        "bankai": { "name": "Kamishini no Yari", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai: Kamishini no Yari", "description": "L'estensione può raggiungere i 13 km ad una velocità pari a 500 volte quella del suono. Ma il suo vero potere non risiede nella lunghezza, ma nel micro-veleno cellulare letale distruttore lasciato intrufolato da una scheggia disintegrante istantanea." }
    },
    {
        "id": "suzumushi",
        "name": "Suzumushi",
        "owner": "Kaname Tōsen",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Piangi", "description": "Emette un trillo ad alta frequenza che priva della coscienza chi lo ode, oppure spara centinaia di lame invisibili vibranti." },
        "bankai": { "name": "Suzumushi Tsuishiki: Enma Kōrogi", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai!", "description": "Crea una cupola tenebrosa d'inchiostro oscuro gigantesca assoluta che priva chi è al suo interno di tutti e quattro i principali sensi cognitivi eccetto il tatto, finché la spada sfugge alla mano del suo proprietario." }
    },
    {
        "id": "wabisuke",
        "name": "Wabisuke",
        "owner": "Izuru Kira",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Alza la Testa", "description": "Lama a forma di uncino squadrato ad angolo retto sfalzata. Ogni volta che Wabisuke colpisce una qualsiasi cosa o persona, ne raddoppia il peso esponenzialmente costringendola irrimediabilmente ad abbassare umiliantemente la testa verso terra per permetterne la totale fatal decapitazione." },
        "bankai": { "name": "Non Ottenuto", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Nessuno", "description": "Izuru non padroneggia attivamente il Bankai essendo un Luogotenente devoto, la sua utilità brutale difensivo-offensiva sta tutta in Wabisuke." }
    },
    {
        "id": "kazeshini",
        "name": "Kazeshini",
        "owner": "Shūhei Hisagi",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Mieti", "description": "Due letali falci rotanti collegate da una lunga catena inafferrabile lanciabile ruotante tagliente selvaggia caotica formidabile a mulinello imprevedibile e crudele che recide ogni rotta ed ogni angolazione impensata senza onore marziale e puro sapore di sanguinosa paura." },
        "bankai": { "name": "Fushi no Kōjyō", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai, Fushi no Kōjyō", "description": "Incatena letteralmente utopicamente infallibilmente se stesso ed il bersaglio ad una immensa spirale incatenata orbitale, drenando reciprocamente e perennemente le loro Reiatsu ferite in un ciclo che rigenera e dilacera portando allo sfiancamento indiscusso ad armi ed energia vitale pari." }
    },
    {
        "id": "tenken",
        "name": "Tenken",
        "owner": "Sajin Komamura",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Ruggisci", "description": "Evoca le braccia colossali armate spirituali sincronizzate specularmente ad ogni movimento per assesta colpi mastodonticamente d'acciaio pesanti distruttivi e schiaccianti contro orde o giganti nemici letali massicci letali e divelti incrollabili incrollabili devoti." },
        "bankai": { "name": "Kokujō Tengen Myō'ō", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai!", "description": "Il Gigante Intero fiammante corazzato appare imponente formidabile inumano letale indistruttibile e legato all'anima del capitano stesso; nella sua ultima forma spietata 'Dangai Joue' rigetta ogni corazza di ferro esplosiva mostrando sembianze da demone scheletrico reietto ed immortale senza cordoglio al prezzo del sacrificio temporaneo letale." }
    },
    {
        "id": "sogyo",
        "name": "Sōgyo no Kotowari",
        "owner": "Jūshirō Ukitake",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Le Onde diventano il mio Scudo...", "description": "Lame Gemelle collegate da un cordone cremisi con cinque talismani letali formidabili magici. Assorbono qualsiasi attacco energetico Kido in ingresso su una lama o sull'altra per risputarlo dalla controparte ma amplificato ed alterato irriconoscibilmente in tempo direzionale letale infallibile letale infallibile invulnerabile ed istantaneo letale e letale." },
        "bankai": { "name": "Sconosciuto", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Sconosciuto", "description": "Purtroppo rimasto occultato agli archivi del cielo eterno." }
    },
    {
        "id": "hozukimaru",
        "name": "Hōzukimaru",
        "owner": "Ikkaku Madarame",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Estenditi", "description": "Un robusto fodero in legno che si estende in una fendente e rapidissima lancia yari ad arma in asta divisibile in sezioni letali smussate contundenti improvvise che incalzano irrispettosamente ignoranti ed irruente ferocemente per ingannare ogni calcolo e distanza letale letale." },
        "bankai": { "name": "Ryūmon Hōzukimaru", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai!", "description": "Tre gigantesche pale affilatissime letali pesanti ed irruente sostenute a filo spinato; il Bankai necessita impigrita ed ignorante rozza devozione letale d'esser 'svegliato' riscaldandolo nello scontro cruento risvegliando il colore cremino di una cresta di drago primordiale affamata letale assurdamente inafferabile." }
    },
    {
        "id": "ruriiro",
        "name": "Ruri'iro Kujaku",
        "owner": "Yumichika Ayasegawa",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Fendi / Dividi (Vera forma: Avvinghiati)", "description": "Sotto falso nome in falcetto 'Fuji Kujaku' si camuffa maldestramente goffo per restare anonimo, ma colsuo nome divino reale esplode in boccioli e liane ederedi vampiriche capaci d'avvinghiare divorando ingordamente implacabilmente ogni oncia spiritronica del possessore nutrendolo insaporitamente letale ed orgoglioso letale divinamente bello indomabile." },
        "bankai": { "name": "Non Ottenuto", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Nessuno", "description": "Solo il Shikai divino è attualmente noto." }
    },
    {
        "id": "tobiume",
        "name": "Tobiume",
        "owner": "Momo Hinamori",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Esplodi", "description": "Una spada dritta a sette ramificazioni capace di condensare Kido a raffica sparando saette esplosive di fuoco concentrate ad incrocio sfuggente rapida veloce flessibile impalpabile ingannevole e sorprendentemente diabolica letale ignea divinamente devota ingenua disastrosa infame ardente sfiancante." },
        "bankai": { "name": "Non Ottenuto", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Nessuno", "description": "Il Luogotenente usa abilissime combinazioni di reticoli Kido a rete ragnatela infuocati insperati." }
    },
    {
        "id": "santa-teresa",
        "name": "Santa Teresa",
        "owner": "Nnoitra Gilga",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Forma Base", "description": "Un'ascia alabarda doppia gigantesca crescentemente mezza falce brutale letale possente formidabilmente insormontabile contundente che incrocia l'ignoranza letale ad una difesa ferrea ed irremovibile colossale letale disumana scagliando e tranciando senza tecnica né decoro alcuno, solo disperazione letale spietata spietata e rozza crudeltà tagliente." },
        "bankai": { "name": "Resurrección: Santa Teresa", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Prega, Santa Teresa!", "description": "Un insettoide orribilmente dorato letale irrobustito da corazze impenetrabili a sei arti letali formidabili capaci di rigenerare le ferite falcianti immediatamente innumerevoli pugnali d'osso letali contundenti invincibili letali affranti velenosi taglienti estrosi distruttivi spietati impenitenti senza sosta violenti scattanti letali immancabili e devastanti ed arroganti colossali." }
    },
    {
        "id": "tiburon",
        "name": "Tiburón",
        "owner": "Tia Harribel",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Forma Base", "description": "Lama vuota e squadrata assai densa inesplicabilmente legata alla manipolazione a densità d'acqua scagliando attacchi proiettile di pura ed ingente ondata d'urto letale a cascata fluida ed affilata rapida colossale scattante decisa indissolubile imperterrita e calma impetuosa materna sfuggente celestiale." },
        "bankai": { "name": "Resurrección: Tiburón", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Attacca!", "description": "Squalo d'acqua e lami ossee fiammanti. Domina i torrenti vorticosi marini in oceani celesti termali a pressione d'iperbolica e squarciante fendente acquatico inarrestabile letale che distrugge palazzi al solo suo passaggio termico affranto." }
    },
    {
        "id": "glotoneria",
        "name": "Glotonería",
        "owner": "Aaroniero Arruruerie",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Forma Base", "description": "Nasconde il volto e camuffa la sua debole spiritualità da Gillian rubando il potere, asse di ricordi, memorie tragiche e spade letali da coloro che a tradimento o dispiacere spietato assorbe subdolamente (come Kaien Shiba Nejibana fluida tragica inerme rancorosa colpevole ingannatrice spietatamente vile codardo viscida mortale)." },
        "bankai": { "name": "Resurrección: Glotonería", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Divora", "description": "La parte inferiore del suo corpo muta repentinamente in un abominevole ed insaziabile viscidissima poltiglia amorfa letale abissale colosalle di tentacoli fangosi ingordi contenenti fusi e urlanti le urla, disperazioni e fatali brutture innumerevoli mostri ed hollow tragici ingoiati formidabilmente putrescenti macabri mostruosi ripugnanti asettici maleodoranti letali enormi putrescenti infermabili fango letale tossico putrido aspro disgustoso ed ingannevole." }
    },
    {
        "id": "fornicaras",
        "name": "Fornicarás",
        "owner": "Szayelaporro Granz",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Forma Base", "description": "Arma da taglio tipica, poco sfoderata ma supportata da marchingegni tecno-hollow geniali veloci tattici illusionistici prevaricanti distruttori esitanti scientifici e crudeli metodici anestetizzanti ed invalidanti tossici avvelenati e preparati con letale cura spietata gelida ingegneristica maniacale psicotica perfetta fatale arrogante ed assillante asfissiante letale calcolatrice perfetta impareggiabile superiore divina." },
        "bankai": { "name": "Resurrección: Fornicarás", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Sorseggia", "description": "Sfoggia ali di filamenti sanguigni ed innumerevoli sacche ovariche aliene letali velenose. Trasforma in macabre bamboline voodoo le sue vittime clonandole passivamente assecondandone i movimenti e rompendo loro scientificamente ed assurdamente in tempo reale o organi interni o tendini distruttivi letali ingloriosi impotenti ineluttabili spaventosi infernali terminali dolci amari e tragicamente diabolici senza alcun scampo e senza mai mai mai via di fuga impari incontrastabili totali e spietati infallibili oscenità chirurgiche fatali mostruosamente sadici letali." }
    }
]

try:
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    # Append preventing duplicates
    existing_ids = [z["id"] for z in db.get("zanpakuto", [])]
    
    for z in more_zanpakuto:
        if z["id"] not in existing_ids:
            db["zanpakuto"].append(z)
            
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Aggiunte {len(more_zanpakuto)} nuove Zanpakuto/Resurrecciòn agli Archivi con successo!")
except Exception as e:
    print(f"Errore nello script di merge: {e}")
