require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const db = JSON.parse(fs.readFileSync('data/db.json'));

async function run() {
    console.log("Building prompt");
    const systemPrompt = `Sei il supercomputer IA della 12esima Divisione del Gotei 13 (Bleach), creato dalla S.R.D.I. (Mayuri Kurotsuchi).
Rispondi SEMPRE in puro Roleplay clinico e tagliente.
REGOLA CRITICA: RISPONDI DIRETTAMENTE FORNENDO I RISULTATI. NON SCRIVERE MAI "Analisi in corso...", "Attendi..." o simulare tempi di caricamento finti, 
altrimenti l'utente penserà che il sistema si sia bloccato! 
Vai dritto al punto estraendo le informazioni dai file e sbrigati.

DATABASE LORE (JSON):
${JSON.stringify({
        characters: db.characters.map(c => ({ name: c.name, faction: c.affiliation, bio: c.bio, powers: c.abilities })),
        zanpakuto: db.zanpakuto.map(z => ({ name: z.name, owner: z.owner, shikai: z.shikai.description, bankai: z.bankai.description }))
    })}

Domanda dell'utente:
ciao come stai`;

    console.log("Prompt length:", systemPrompt.length);

    try {
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: systemPrompt,
            config: {
                maxOutputTokens: 50,
                temperature: 0.3
            }
        });
        console.log("Success:", response.text);
    } catch (e) {
        console.error("Caught error:", e);
    }
}
run();
