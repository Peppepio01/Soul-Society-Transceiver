Realizzato da Oliva Giuseppepio, email: giuseppepioliva@gmail.com


# Soul Society Transceiver 🦋 (12th Division Archives)
**Soul Society Transceiver** è un'applicazione web moderna e totalmente immersiva progettata per la simulazione e l'esplorazione autonoma del database classificato della Seireitei (Bleach). Ispirata ai terminali asettici dell'ufficio S.R.D.I. (Istituto di Ricerca e Sviluppo), l'app unisce un'interfaccia elegante a un'intelligenza artificiale reattiva con pieno controllo della fedeltà visiva. Con grafiche vettoriali mozzafiato, automazione sui media originali e controllo vocale, il Transceiver rende il mondo di Bleach reale sul tuo schermo.

---

## ✨ Funzionalità Principali

### 📊 Archivi della Seireitei
* **Profili Completi:** Consulta affiliazioni storiche, nomi delle singole Zanpakuto e l'arsenale intero di tecniche e Kido associate a oltre 60 personaggi canonici, dagli Shinigami ai Quincy ed Arrancar.
* **Layout Interattivo:** Griglie esplorative dal design oscuro ("Deep Night"), modellate con effetti blur e bordi in vetro fuso (Glassmorphism). 

### 🗡️ Armeria Zanpakuto Interattiva
* Immagini ad Altissima Definizione delle forme base, Shikai, Bankai (o Resurrección) recuperate tramite algoritmi automatizzati che evitano placeholder IA scadenti in favore degli originali anime/manga ufficiali.
* **Interactive Switch:** Premi l'interruttore sull'UI per assistere alla transizione istantanea dell'animazione tra la forma "Shikai" della spada e il suo rispettivo "Rilascio/Bankai" per decine di capitani e nemici mortali!

### ⏳ Linea Temporale Storica 
* **Chronicle Logs:** Esplora gli eventi cruciali del mondo di Bleach filtrandoli per epoche ("Il Passato", "Il Presente", "Il Futuro/Guerra Millenaria").

---

## 🤖 Assistente AI (Powered by Gemini RAG)
Il fulcro pulsante dell'applicazione è la Chatbox dell'S.R.D.I.
* **Intelligenza Aumentata dal Database (RAG):** Gemini non indovina le risposte basandosi su addestramenti vecchi, bensì legge in diretta il file `db.json` locale per rispondere ad ogni tua query col millimetro della precisione tattica.
* **Roleplay Assoluto:** L'IA prende le sembianze (e il carattere) di un impiegato cinico e geniale della Dodicesima Divisione, in stile Mayuri Kurotsuchi. Usa gergo militare e si riferisce all'utente come "Sostituto Shinigami".
* **Voce Integrata:** Ogni responso dell'IA viene scandito a voce lata e con tono robotico dal tuo computer usando la **Web Speech API** in accoppiata al suggestivo **Effetto Macchina da Scrivere** testuale.
* *Nota: Richiede una chiave API di Google Gemini Flash (ottenibile gratuitamente).*

---

## 🔄 Automazioni
* **Python Web Scraper Integrato:** L'applicazione include uno script Python (`fetch_badge.py` e `fetch_authentic_weapon_images.py`) che risolve da solo i blocchi server Wiki/Fandom (errore 403), usando Spoofing di intestazioni di rete falsificate per scaricare e popolare automaticamente le tue icone e la tua galleria fotografica delle armi in HD (che l'IA generativa sbaglia sempre a disegnare).

---

## 🌙 Interfaccia Personalizzabile & Estetica
* **Sistema Particellare di Reiatsu:** Nessuno sfondo vuoto. Sotto tutta l'UI è attivo un sistema `particles.js` che genera un flusso costante in 3D di energia spirituale luminosa (rossa e blu) verso l'alto (Particelle ambientali di "Reishi").
* **Loghi Vettoriali Matematicamente Perfetti:** Il simbolo a forma di rombo (l'insegna dei Capitani del Gotei 13) non è un'immagine sgranata, ma una geometria tracciata fedelmente in punti e tracciati SVG `evenodd` per ri-scalarsi in 4K adimensionale e brillare di bianco sul menu laterale della navbar e nella schermata di caricamento.

---

## 🚀 Come avviare il progetto

Essendo l'applicazione spinta da un server backend Node.js locale necessario per gestire privatamente l'SDK di Gemini senza far trapelare la chiave API nell'HTML sul browser dell'utente finale, l'avvio è semplicissimo:

1. **Clona la repository o scarica il codice sorgente:** 
   ```bash
   git clone https://github.com/Peppepio01/Soul-Society-Transceiver.git
   cd Soul-Society-Transceiver
   ```
2. **Installa le dipendenze:** (Assicurati di avere Node.js installato)
   ```bash
   npm install
   ```
3. **Imposta il file protetto (Environment):**
   Crea un file chiamato esattamente `.env` nella radice del progetto al livello di `server.js` ed incollaci la tua chiave:
   `GEMINI_API_KEY=La-tua-chiave-api-qui`
4. **Avvia il server di rete S.R.D.I.:**
   ```bash
   node server.js
   ```
5. **Entra nell'app:** L'applicazione sarà visibile ed utilizzabile aprendo il tuo browser alla pagina `http://localhost:3000`.

---

## 🛠 Tecnologie Utilizzate
* **Frontend Core:** HTML5, CSS3, Vanilla JavaScript.
* **Backend:** Node.js, framework Express.js.
* **Componenti Estetici:** Particelle in Canvas 2D (`js/particles.js`), Typewriter Effect, font regali Google (`Cinzel`, `Inter`), icone vettoriali ricostruite in path SVG assoluto.
* **Database Strutturale:** `data/db.json` (per latenza zero senza database remoti farraginosi).
* **Motore AI:** Official Google `@google/genai` (modello `gemini-2.5-flash`).
* **Micro-Data Extraction:** `python` e librerie HTTP native per raschiare risorse immagine ad alta risoluzione in maniera stealth.

Progetto e Database costruiti interamente come devota simulazione tecnica e narrativa del Gotei 13 e delle opere di Bleach.
