require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');

async function testApi() {
    console.log("Chiave trovata in .env:", !!process.env.GEMINI_API_KEY);
    if(process.env.GEMINI_API_KEY) {
        console.log("Lunghezza chiave:", process.env.GEMINI_API_KEY.length);
    }
    
    try {
        const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: 'Test connection'
        });
        console.log("Risposta API OK:", response.text);
    } catch (err) {
        console.error("\n[ERRORE API DETTAGLIATO]:", err);
    }
}

testApi();
