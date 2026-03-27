Realizzato da Oliva Giuseppepio email: giuseppepioliva@gmail.com e Francesca Cicciù email:francescacicciu07@gmail.com


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
   cd Soul-Society-Transceiver<img width="1886" height="982" alt="Screenshot 2026-03-27 024409" src="https://github.com/user-attachments/assets/b01fcda8-b302-4984-9e68-8f8434e78c2d" />

   ```
2. **Installa le dipendenze:** (Assicurati di avere Node.js installato)<img width="1779" height="972" alt="Screenshot 2026-03-27 024413" src="https://github.com/user-attachments/assets/48e5811d-8b38-45db-bee0-49a1621ccb7c" />

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
<img width="1755" height="932" alt="Screenshot 2026-03<img width="1755" height="932" alt="Screenshot 2026-03-27 024438" src="https://github.com/user-attachments/assets/bd975e3e-124b-425e-9c92-716b3b6e15d8" />
<img width="1779" height="972" alt="Screenshot 2026-03-27 024413" src="https://github.com/user-attachments/assets/50d8513a-b685-40a5-94a7-93f9b86d3054" />
<img width="1886" height="982" alt="Screenshot 2026-03-27 024409" src="https://github.com/user-attachments/assets/324c1a82-8100-40c2-91be-f3040db0e73d" />
<img width="1344" height="764" alt="Screenshot 2026-03-27 022643" src="https://github.com/user-attachments/assets/8591b067-7ab2-4b34-b61a-a6699a2616ef" />
<img width="1614" height="922" alt="Screenshot 2026-03-27 021100" src="https://github.com/user-attachments/assets/d54c7b33-180f-49c5-9c6b-e74c879cc09e" />
<img width="1601" height="922" alt="Screenshot 2026-03-27 021053" src="https://github.com/user-attachments/assets/2c123045-efa8-4c92-bd86-f8962f7d2ec0" />
<img width="1723" height="842" alt="Screenshot 2026-03-27 021047" src="https://github.com/user-attachments/assets/afbee6b7-867d-4589-8d26-ff091b59546a" />
<img width="1692" height="928" alt="Screenshot 2026-03-27 021041" src="https://github.com/user-attachments/assets/c62f5bfd-44ad-4372-ad42-8b939aed70d9" />
-27 024438" src="https://github.com/user-attachments/assets/c43fb4ee-7bc9-4295-92e3-c88a7f990e34" />
