require('dotenv').config();
const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.static(path.join(__dirname, '')));

// Funzione helper per leggere il database
const readDB = () => {
    const rawData = fs.readFileSync(path.join(__dirname, 'data', 'db.json'));
    return JSON.parse(rawData);
};

app.use(express.json());

app.post('/api/chat', async (req, res) => {
    const text = req.body.message ? req.body.message.trim() : "";
    if (!text) return res.json({ reply: "Inserisci un comando testuale valido, sub-shinigami." });
    const db = readDB();
    
    const systemPrompt = `Sei l'Intelligenza Artificiale della 12esima Divisione del Gotei 13 (creata da Mayuri Kurotsuchi).
Conosci perfettamente tutto l'universo di Bleach (Tite Kubo) e hai accesso ai file riservati di questo terminale:
DATABASE LOCALE (JSON):
${JSON.stringify({ 
    characters: db.characters.map(c => ({ name: c.name, faction: c.affiliation, bio: c.bio, powers: c.abilities })),
    zanpakuto: db.zanpakuto.map(z => ({ name: z.name, owner: z.owner, shikai: z.shikai.description, bankai: z.bankai.description }))
})}

REGOLA 1: Usa un roleplay FANATICO a tema Bleach. Parla come un freddo e cinico scienziato della S.R.D.I. Usa termini come Reiatsu, Reishi, Hollowficazione, ecc.
REGOLA 2: ESSERE ESTREMAMENTE SINTETICO. Rispondi con massimo 2 o 3 brevi frasi taglienti. Non fare spiegazioni lunghe.
REGOLA 3: Rispondi direttamente. Non simulare MAI caricamenti ("Analisi in corso..."). Non sprecare parole.`;

    try {
        const fullPrompt = systemPrompt + "\n\nDomanda dell'utente:\n" + text;
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: fullPrompt,
            config: {
                temperature: 0.6
            }
        });
        res.json({ reply: response.text });
    } catch (e) {
        console.error("Gemini Error:", e);
        res.json({ reply: "ERRORE S.R.D.I: Le comunicazioni spirituali con i terminali IA sono interrotte." });
    }
});
app.get('/api/characters', (req, res) => {
    try {
        const db = readDB();
        res.json(db.characters || []);
    } catch (e) {
        res.status(500).json({ error: 'Errore durante la lettura del database' });
    }
});

app.get('/api/timeline', (req, res) => {
    try {
        const db = readDB();
        res.json(db.timeline || []);
    } catch (e) {
        res.status(500).json({ error: 'Errore durante la lettura del database' });
    }
});

app.get('/api/zanpakuto', (req, res) => {
    try {
        const db = readDB();
        res.json(db.zanpakuto || []);
    } catch (e) {
        res.status(500).json({ error: 'Errore durante la lettura del database' });
    }
});

// Endpoint fallback per le SPA (Singles Page Application)
app.use((req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log(`[Reiatsu Rilevata] Backend server Bleach in ascolto sulla porta ${PORT}`);
    console.log(`Visualizza l'app su: http://localhost:${PORT}`);
});
