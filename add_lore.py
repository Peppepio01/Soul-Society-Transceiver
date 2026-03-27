import json
import os

db_path = "c:/Users/giuse/Desktop/Bleach/data/db.json"

timeline = [
    {
        "id": "t1",
        "era": "Era Antica",
        "faction": "Divinità / Nobili",
        "title": "La Creazione dei Tre Mondi",
        "description": "Il Re delle Anime originario viene mutilato e sigillato dai capi delle Cinque Famiglie Nobili per creare l'equilibrio tra la Soul Society, il Mondo Umano e l'Hueco Mundo."
    },
    {
        "id": "t2",
        "era": "1000 Anni Fa",
        "faction": "Shinigami vs Quincy",
        "title": "La Guerra Sanguinosa e la Sconfitta di Yhwach",
        "description": "Genryūsai Shigekuni Yamamoto, alla guida dell'originario e spietato Gotei 13, sconfigge Yhwach, Re dei Quincy, costringendo l'Impero Wandenreich a ritirarsi nell'ombra del Seireitei."
    },
    {
        "id": "t3",
        "era": "200 Anni Fa",
        "faction": "Quincy",
        "title": "Lo Sterminio dei Quincy",
        "description": "La Soul Society lancia una campagna di sterminio preventivo contro quasi tutti i restanti Quincy nel Mondo Umano per prevenire il collasso delle anime causato dalla loro distruzione totale degli Hollow."
    },
    {
        "id": "t4",
        "era": "101 Anni Fa",
        "faction": "Vaizard",
        "title": "L'Incidente della Hollowificazione",
        "description": "Sōsuke Aizen conduce esperimenti segreti di Hollowificazione su diversi Capitani e Luogotenenti (divenuti poi i Vaizard). Kisuke Urahara viene ingiustamente incastrato ed esiliato sulla Terra insieme a Yoruichi e Tessai."
    },
    {
        "id": "t5",
        "era": "20 Anni Fa",
        "faction": "Famiglia Kurosaki",
        "title": "L'Incontro tra Essenze Rifiutate",
        "description": "Il Capitano della Decima Divisione, Isshin Shiba, salva la Quincy Masaki da un Hollow artificiale di Aizen ('White'). Per fermare l'infezione Hollow di Masaki, Isshin rinuncia permanentemente ai suoi poteri di Shinigami, stabilendosi sulla Terra."
    },
    {
        "id": "t6",
        "era": "Oggi (Inizio Storia)",
        "faction": "Ichigo",
        "title": "L'Agente Sostituto Shinigami",
        "description": "Ichigo Kurosaki ottiene i poteri di Shinigami da Rukia Kuchiki per proteggere la sua famiglia da un Hollow avido. Diviene lo Shinigami Sostituto della città di Karakura."
    },
    {
        "id": "t7",
        "era": "Infiltrazione nel Seireitei",
        "faction": "Gotei 13",
        "title": "Il Tradimento di Aizen",
        "description": "Aizen inscena la sua stessa morte, manipola le esecuzioni segrete e recupera l'Hōgyoku dall'anima di Rukia, prima di tradire definitivamente il Gotei 13 ritarandosi nell'Hueco Mundo insieme a Gin e Tōsen."
    },
    {
        "id": "t8",
        "era": "Guerra di Karakura",
        "faction": "Espada",
        "title": "La Battaglia Falsa di Karakura (FKT)",
        "description": "Gli Espada attaccano la finta Karakura. Dopo durissimi scontri, Aizen si fonde con l'Hōgyoku, ma Ichigo domina la forma suprema del Getsuga Tensho finale perdendo i suoi poteri ma garantendo alla Soul Society di sigillare il Dio traditore."
    },
    {
        "id": "t9",
        "era": "17 Mesi Dopo",
        "faction": "Fullbringer",
        "title": "L'Arco del Sostituto Smarrito",
        "description": "Kūgo Ginjō manipola Ichigo per rubargli i poteri Fullbring, ma grazie ad una spada spiritualizzata fornita da tutto il Gotei 13, Ichigo riacquista interamente la sua carica leggendaria e annienta l'organizzazione Xcution."
    },
    {
        "id": "t10",
        "era": "La Guerra dei Mille Anni",
        "faction": "Stern Ritter",
        "title": "Il Risveglio del Re Quincy",
        "description": "Yhwach si risveglia ed ordina l'eliminazione totale del Gotei 13. Il Seireitei viene raso al suolo in pochi minuti, il Comandante Yamamoto è abbattuto ferocemente, e Yhwach invade il Palazzo del Re delle Anime puntando ad assorbire l'universo intero."
    }
]

zanpakuto = [
    {
        "id": "zangetsu",
        "name": "Zangetsu",
        "owner": "Ichigo Kurosaki",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Nessun Comando (Sempre Rilasciata) / Doppia Lama", "description": "Un letale mannaione gigantesco oppure due lame nere bilanciate per assalti rapidi ed il letale Getsuga Tenshō." },
        "bankai": { "name": "Tensa Zangetsu", "image": "https://i.imgur.com/j1v2h8X.jpeg", "command": "Bankai!", "description": "Compressione estrema della Reiatsu, fornisce ad Ichigo una velocità iper-sonica, riflessi istantanei e tremendi fendenti nerastri in grado di lacerare l'orizzonte (e il destino stesso)." }
    },
    {
        "id": "ryujin-jakka",
        "name": "Ryūjin Jakka",
        "owner": "Genryūsai Shigekuni Yamamoto",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Riduci l'Universo in Cenere", "description": "La Zanpakuto infuocata più antica e devastante; genera un'immensa e apocalittica ondata di fiamme inestinguibili che brucia qualsiasi cosa tocchi il cielo o la terra." },
        "bankai": { "name": "Zanka no Tachi", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai: Zanka no Tachi", "description": "Le fiamme spariscono confinate dentro la lama singola; la temperatura del calore raggiunge 15 milioni di gradi. Lacerando, cancella dall'esistenza i bersagli e risorge le ceneri infuocate dei defunti passati sottomessi." }
    },
    {
        "id": "kyoka-suigetsu",
        "name": "Kyōka Suigetsu",
        "owner": "Sōsuke Aizen",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Spezza (Kudakero)", "description": "Il Kanzen Saimin: ipnosi totale sui cinque sensi, la massa o la statura dell'oggetto ed entità controllati. Infrangibile, infallibile, e perpetua una volta che se ne osserva il rilascio incantato perfido." },
        "bankai": { "name": "Sconosciuto", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Sconosciuto", "description": "Aizen non ha mai mostrato la necessità materiale di avvalersene. L'Ipnosi Completa fu ed è sufficiente per soverchiare Divinità." }
    },
    {
        "id": "senbonzakura",
        "name": "Senbonzakura",
        "owner": "Byakuya Kuchiki",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Disperditi", "description": "La lama deflagra in microscopiche schegge letali affilate che riflettendo la luce paiono miriadi di rosevoli e silenziosi petali di ciliegio in balia delle folate fatali." },
        "bankai": { "name": "Senbonzakura Kageyoshi", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai: Senbonzakura Kageyoshi", "description": "Vengono evocate innumerevoli ed enormi lame giganti dal pavimento che mutano instantaneamente in fantastici miliardi di lame-petali letali. La forma difensiva perfetta fusa unita ad un'offensiva diabolica distruttiva (Gōkei / Hakuteiken)." }
    },
    {
        "id": "hyorinmaru",
        "name": "Hyōrinmaru",
        "owner": "Tōshirō Hitsugaya",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Siedi sui Cieli Ghiacciati", "description": "Zanpakuto di elemento ghiaccio suprema: controlla il meteo circostante, emanando un mortale drago di puro ghiaccio glaciale atmosferico implacabile e tenace." },
        "bankai": { "name": "Daiguren Hyōrinmaru", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai... Forma Adulta", "description": "Il Capitano assume le sembianze di un Angelo Ghiacciato dotato di ali congelanti. Nella padronanza perfetta maturata (forma adulta prolungata temporale) basta scorrere l'elsa per ibernare concettualmente funzioni elementari totali magiche avversarie." }
    },
    {
        "id": "katen-kyokotsu",
        "name": "Katen Kyōkotsu",
        "owner": "Shunsui Kyōraku",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Il Vento dei Fiori è Inquieta e il Demone Zampilla...", "description": "Doppie daghe massicce piratesche che 'trasformano i giochi di bambini nella terribile realtà fatale'. Ombre letali (Kageoni), colori (Irooni), passaggi letali ad una taglia insormontabile di abilità tattica." },
        "bankai": { "name": "Karamatsu Shinjū", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai", "description": "Nero dolore, oscurità raggelante disperata, una tragica fiaba teatrale di 4 atti infusi alle ferite recirpoche ed all'affogamento abissale marino fatale recidente l'essenza sanguinaria del fato medesimo incrociato indiscusso." }
    },
    {
        "id": "benihime",
        "name": "Benihime",
        "owner": "Kisuke Urahara",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Svegliati", "description": "Padroneggia fasci, reti sanguinanti ed elusivi Kido schermanti (Nake, Chikasumi no Tate). Plasma onde Reiatsu d'ingegneria rossa ed esplosiva perfetta chirurgica." },
        "bankai": { "name": "Kannonbiraki Benihime Aratame", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai!", "description": "Una figura femminile mastodontica la cui essenza 'Ricuce, Disseziona e Ricompone' concetti o materie stesse. Rende un braccio ceco nuovo vivo e taglia la carne onnipotente solo modificandone l'essenza architettonica base." }
    },
    {
        "id": "ashisogi",
        "name": "Ashisogi Jizō",
        "owner": "Mayuri Kurotsuchi",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Strappa le Membra", "description": "Un bizzarro tridente neonato che instilla immediatamente tossine bio-paralitiche anestetizzando perversamente le sinapsi nervose impedendo reazioni motorie letali ma accatastando dolore lucido intatto avvilente sibilante sadico." },
        "bankai": { "name": "Konjiki Ashisogi Jizō", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai... Modificato", "description": "Millepiedi colossale tossico dal muso neonato capace di nebulizzare un gas tossico biologico mortale autorigenerante a base sanguigna sperimentale chimica geniale e divoratrice." }
    },
    {
        "id": "sode-shirayuki",
        "name": "Sode no Shirayuki",
        "owner": "Rukia Kuchiki",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Danza", "description": "La spada più intonsa della storia. Non congela la condensa circostante bensì l'essenza motoria della medesima Rukia rallutandola letalmente temporaneamente fino al fatale congelamento dello Zero Assoluto inumano indescrivibile." },
        "bankai": { "name": "Hakka no Togame", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai!", "description": "Zero Assoluto istantaneo in un'area titanica raggelante. Il bersaglio diventa fragile statua gelata che s'infrange alla minima corrente spazzaneve maestosa ed estasiante." }
    },
    {
        "id": "suzumebachi",
        "name": "Suzumebachi",
        "owner": "Sui Feng",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Pungi tutti i Nemici a Morte", "description": "Dito pungiglione a stiletto: incide un fiore crestato letale sul nemico (Hōmonka). Se viene punzecchiato sulla medesima cresta formale due volte, sopraggiunge la morte fatale fulminea istantanea inevitabile infallibile letale." },
        "bankai": { "name": "Jakuhō Raikōben", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai...", "description": "Paradossalmente ed ironicamente assai pesante, è nientemeno che un missile di testata balistica anti-carro spiritronico dorato enorme che disintegra a detonazione catastrofica termica il difensore indissolubile in scaglie incenerite totali fragorose assordanti." }
    },
    {
        "id": "zabimaru",
        "name": "Zabimaru",
        "owner": "Renji Abarai",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Ruggisci", "description": "Lama composita a scaglie frammentate che allunga i suoi segmenti osseani e letali con estensione e destrezza a frusta, spezzando la difesa ignara tramite assalti flessuosi taglienti animaleschi violenti." },
        "bankai": { "name": "Sōō Zabimaru", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Bankai, Sōō Zabimaru", "description": "La Vera forma (Zaga Teppō): Un cannone dentato scimmiesco serpentino devastante focalizzato interamente e mortalmente sull'abbattimento energetico frontale massivo ed incandescente esplosivo scimmiesco fiammante." }
    },
    {
        "id": "pantera",
        "name": "Pantera (Resurrección)",
        "owner": "Grimmjow Jaegerjaques",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Forma Base", "description": "La Katana posseduta costringe Grimmjow alla fisionomia umanoide sebbene contenga un potere istintivo ed animalesco letale sferzante furente scattante furbo disarmante orgoglioso istintivo Cero." },
        "bankai": { "name": "Desgarrón", "image": "https://i.imgur.com/P5b2c8v.jpeg", "command": "Digrigna, Pantera!", "description": "Velocità bestiale inesplicabile, corazza felina letale con onde d'urto fendente massiccio turbolente letali indomite. Lancio di saette ed artigli giganti cerulei energetici che annientano grattacieli o roccaforti celarsi colpevoli distruttive aspre decise letali feroci furiose spietate formidabili e regali felini." }
    },
    {
        "id": "murcielago",
        "name": "Murciélago (Resurrección)",
        "owner": "Ulquiorra Cifer",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Forma Base", "description": "Arma sottile verde pallida capace di riflettere Cero oscuri devastanti puritani stoici apatici potenti invulnerabili solidi malinconici immoti passivi letali veloci." },
        "bankai": { "name": "Segunda Etapa", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Incatenali, Murciélago", "description": "Una disperata seconda e maestosa fase diabolica alata (Segunda Etapa). Rigenerazione estrema istantanea, forza insuperabile abissale letale infinita opprimente, evocatrice della Lanza del Relámpago che detona oceani desertici nucleari rovinosi." }
    },
    {
        "id": "loslobos",
        "name": "Los Lobos (Resurrección)",
        "owner": "Coyote Starrk",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Forma Base", "description": "Anima scissa eternamente infusa nel corpo della fedele compitina e minuscola Lilynette. Nessuna vera Zanpakuto apparente poiché le loro esistenze fondative sono l'arma ed il possessore gemellare sincrono solipsistico letale infallibile invincibile annoiato letale formidabile formidabile." },
        "bankai": { "name": "Cero Metralleta", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Dagli Addosso, Los Lobos!", "description": "Pistole Gemelle letali colme del Cero mitragliatrice più folgorante insensatamente esteso inafferrabile fulmineo letale infallibile letale scattante letale scoppiettante, unitamente all'evocazione di lupi spirituali d'anime detonanti fatali furiose che braccano impetuosi ed illimitati solitari i bersagli." }
    },
    {
        "id": "ichimonji",
        "name": "Ichimonji",
        "owner": "Ichibē Hyōsube",
        "shikai": { "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Tingi di Nero", "description": "Un enorme pennello letale per la calligrafia in grado di sprigionare tutto il 'nero' dell'universo infinito stellare notturno mortale. Ogni entità ed abilità inchiostrata sfuma interamente perdendo nome ed esistenza o potere sovrastrutturale vitale etereo divino mortale insensato insuperabile annichilente onnipotente letale." },
        "bankai": { "name": "Shirafude Ichimonji (Shin'uchi)", "image": "https://i.imgur.com/8Q5YIqF.jpeg", "command": "Vera Forma...", "description": "Tinge di Bianco letale assegnando i nuovi nomi incrociati alle entità dipinte spietatamente onniscientemente letale divinamente indiscusso sovrano. Se rinomina un Dio Quincy 'Formica Nera', esso muore pestato fatalmente e spietatamente irrevocabilmente impotente." }
    }
]

try:
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    db["timeline"] = timeline
    db["zanpakuto"] = zanpakuto
    
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print("Timeline e Zanpakuto popolate con successo con la Lore Estesa!")
except Exception as e:
    print(f"Errore: {e}")
