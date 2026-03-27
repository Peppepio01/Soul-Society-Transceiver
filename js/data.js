/**
 * DATA MANAGER
 * Handles fetching and exposing the Bleach Lore Data from db.json
 */

const DataManager = {
    cache: null,

    async initialize() {
        try {
            // Fetching dynamically from the new Node.js Express Backend API
            const [charsRes, timelineRes, zanpakutoRes] = await Promise.all([
                fetch('/api/characters'),
                fetch('/api/timeline'),
                fetch('/api/zanpakuto')
            ]);
            
            if (!charsRes.ok || !timelineRes.ok || !zanpakutoRes.ok) {
                throw new Error('Failed to load from Soul Society API backend');
            }
            
            this.cache = {
                characters: await charsRes.json(),
                timeline: await timelineRes.json(),
                zanpakuto: await zanpakutoRes.json()
            };
            return true;
        } catch (error) {
            console.error('Data sync failed:', error);
            // Fallback mock data in case of CORS issues via local file protocol
            this.cache = this.getFallbackData();
            return false;
        }
    },

    getCharacters() {
        return this.cache?.characters || [];
    },

    getTimeline() {
        return this.cache?.timeline || [];
    },

    getZanpakuto() {
        return this.cache?.zanpakuto || [];
    },
    
    // Internal fallback if fetch fails (e.g., opened file:// directly without server)
    getFallbackData() {
         return {
            characters: [
                 {
                  id: "ichigo",
                  name: "Ichigo Kurosaki",
                  image: "https://i.imgur.com/8Q5YIqF.jpeg",
                  zanpakuto: "Zangetsu",
                  abilities: ["Getsuga Tensho", "Shunpo"],
                  affiliation: "Substitute Shinigami",
                  bio: "Substitute Shinigami who protects Karakura town."
                 }
            ],
            timeline: [
                { id: "e1", era: "Present", faction: "Gotei 13", title: "Fallback Event", description: "Data could not be loaded via fetch." }
            ],
            zanpakuto: [
                {
                    id: "z",
                    name: "Zangetsu",
                    owner: "Ichigo",
                    shikai: { image: "https://i.imgur.com/c1A1tK5.jpeg", command: "Always Released", description: "Oversized knife." },
                    bankai: { name: "Tensa Zangetsu", image: "https://i.imgur.com/j1v2h8X.jpeg", command: "Bankai", description: "Speed enhancement." }
                }
            ]
         };
    }
};
