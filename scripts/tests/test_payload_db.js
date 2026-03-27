require('dotenv').config();
const fs = require('fs');
const path = require('path');
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const readDB = () => {
    const rawData = fs.readFileSync(path.join(__dirname, 'data', 'db.json'));
    return JSON.parse(rawData);
};

async function testPayload() {
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

    const fullPrompt = systemPrompt + "\n\nDomanda dell'utente:\nCiao";
    
    console.log("Lunghezza prompt:", fullPrompt.length);
    
    try {
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: fullPrompt,
            config: {
                temperature: 0.6
            }
        });
        console.log("Success:", response.text);
    } catch (e) {
        console.error("\n[DETTAGLI ERRORE GEMINI SDK]:");
        console.error(e.message);
        console.error(e);
    }
}

testPayload();
