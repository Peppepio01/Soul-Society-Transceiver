/**
 * MAIN APP INITIALIZATION
 * Ties perfectly into the Bleach Universe concept, synchronizing 
 * the spirit particles (data) with the UI structure.
 */

document.addEventListener('DOMContentLoaded', async () => {
    
    // 1. Initialize UI Listeners (Chat, Nav)
    UIController.init();

    // 2. Fetch data (Mock network lag to allow loading screen to show)
    setTimeout(async () => {
        
        await DataManager.initialize();

        // 3. Render Views
        UIController.renderCharacters(DataManager.getCharacters());
        UIController.renderTimeline(DataManager.getTimeline());
        UIController.renderArmory(DataManager.getZanpakuto());
        
        // 4. Reveal App (Fade loading screen out)
        UIController.hideLoading();
        
    }, 1000); // Artificial 1s delay mimicking "Reishi Synchronization"
    
});
