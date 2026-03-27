require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

async function test() {
    try {
        console.log("Starting test...");
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: "Ciao, prova test."
        });
        console.log("Success:", response.text);
    } catch (e) {
        console.error("SDK Error:", e);
    }
}
test();
