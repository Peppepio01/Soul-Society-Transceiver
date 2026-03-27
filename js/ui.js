/**
 * USER INTERFACE CONTROLLER
 * Handles all DOM manipulation, rendering, and event listeners.
 */

const UIController = {
    // DOM Elements
    elements: {
        loading: document.getElementById('loading-screen'),
        appMain: document.getElementById('main-app'),
        navLinks: document.querySelectorAll('.nav-links li'),
        sections: document.querySelectorAll('.app-section'),
        
        chatMessages: document.getElementById('chat-messages'),
        chatInput: document.getElementById('chat-input'),
        sendBtn: document.getElementById('send-btn'),
        
        charGrid: document.getElementById('character-grid'),
        
        timelineContainer: document.getElementById('timeline-container'),
        eraFilter: document.getElementById('era-filter'),
        
        armoryGrid: document.getElementById('armory-grid')
    },

    init() {
        this.setupNavigation();
        this.setupChat();
        this.setupFilters();
    },

    hideLoading() {
        setTimeout(() => {
            this.elements.loading.classList.add('fade-out');
            this.elements.appMain.style.display = 'flex';
        }, 1500); // 1.5s delay for dramatic effect
    },

    setupNavigation() {
        this.elements.navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                // Update active link class
                this.elements.navLinks.forEach(l => l.classList.remove('active'));
                const target = e.currentTarget;
                target.classList.add('active');

                // Update active section
                const targetId = target.getAttribute('data-target');
                this.elements.sections.forEach(sec => sec.classList.remove('active-section'));
                document.getElementById(targetId).classList.add('active-section');
            });
        });
    },

    /* --- Chat functionality --- */
    setupChat() {
        this.elements.sendBtn.addEventListener('click', () => this.handleSendMessage());
        this.elements.chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.handleSendMessage();
        });
    },

    async handleSendMessage() {
        const text = this.elements.chatInput.value.trim();
        if (!text) return;

        // Add user message
        this.appendMessage(text, 'user');
        this.elements.chatInput.value = '';

        try {
            const botRes = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });
            const data = await botRes.json();
            
            setTimeout(() => {
                this.appendTypewriterMessage(data.reply, 'bot');
                this.speak(data.reply);
            }, 600); // Artificial terminal processing lag
        } catch (e) {
            this.appendTypewriterMessage("Errore critico di comunicazione col terminale Dipartimento Ricerca.", "bot");
        }
    },
    
    speak(text) {
        if (!window.speechSynthesis) return;
        // Interrompe l'audio precedente
        window.speechSynthesis.cancel();
        
        // Pulisce asterischi del markdown per la lettura vocale
        const cleanText = text.replace(/[*_#]/g, '');
        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = 'it-IT';
        utterance.pitch = 0.8; // Voce leggermente robotica/profonda
        utterance.rate = 1.1;
        window.speechSynthesis.speak(utterance);
    },

    appendTypewriterMessage(text, sender) {
        const div = document.createElement('div');
        div.className = `message ${sender}-message shunpo-in`;

        const contentDiv = document.createElement('div');
        contentDiv.className = `message-content reiatsu-${sender}`;
        
        div.appendChild(contentDiv);
        this.elements.chatMessages.appendChild(div);
        
        // Typewriter effect
        let i = 0;
        const speed = 25; // ms per carattere
        
        const typeWriter = () => {
            if (i < text.length) {
                // Supporto basico al markdown nei messaggi per il bold
                if(text.substring(i, i+2) === '**') {
                    // Trova la fine del bold
                    const end = text.indexOf('**', i+2);
                    if(end !== -1) {
                        contentDiv.innerHTML += `<strong>${text.substring(i+2, end)}</strong>`;
                        i = end + 2;
                    } else {
                        contentDiv.innerHTML += text.charAt(i);
                        i++;
                    }
                } else if(text.charAt(i) === '\n') {
                    contentDiv.innerHTML += '<br>';
                    i++;
                } else {
                    contentDiv.innerHTML += text.charAt(i);
                    i++;
                }
                this.elements.chatMessages.scrollTop = this.elements.chatMessages.scrollHeight;
                setTimeout(typeWriter, speed);
            }
        };
        
        typeWriter();
    },

    appendMessage(text, sender) {
        const div = document.createElement('div');
        div.className = `message ${sender}-message shunpo-in`;

        const contentDiv = document.createElement('div');
        contentDiv.className = `message-content reiatsu-${sender}`;
        contentDiv.textContent = text;
        
        div.appendChild(contentDiv);
        this.elements.chatMessages.appendChild(div);
        
        // Auto scroll to bottom
        this.elements.chatMessages.scrollTop = this.elements.chatMessages.scrollHeight;
    },

    /* --- Render Character Archives --- */
    renderCharacters(characters) {
        this.elements.charGrid.innerHTML = '';
        characters.forEach((char, index) => {
            const delay = index * 0.1;
            const card = document.createElement('div');
            card.className = 'character-card fade-in-up';
            card.style.animationDelay = `${delay}s`;
            
            const abilitiesHtml = char.abilities.map(ab => `<span class="ability-tag">${ab}</span>`).join('');
            
            card.innerHTML = `
                <img src="${char.image}" alt="${char.name}" class="card-image" loading="lazy">
                <div class="card-content">
                    <h3 class="card-title">${char.name}</h3>
                    <div class="card-affiliation">${char.affiliation}</div>
                    <div class="card-zanpakuto">
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 100 100"><use href="#icon-guard"></use></svg>
                        <span>${char.zanpakuto}</span>
                    </div>
                    <p class="card-bio">${char.bio}</p>
                    <div class="card-abilities">${abilitiesHtml}</div>
                </div>
            `;
            this.elements.charGrid.appendChild(card);
        });
    },

    /* --- Render Timeline --- */
    setupFilters() {
        this.elements.eraFilter.addEventListener('change', (e) => {
            const era = e.target.value;
            const allEvents = DataManager.getTimeline();
            const filtered = era === 'all' ? allEvents : allEvents.filter(ev => ev.era === era);
            this.renderTimeline(filtered);
        });
    },

    renderTimeline(events) {
        this.elements.timelineContainer.innerHTML = '';
        events.forEach((ev, index) => {
            const delay = index * 0.15;
            const item = document.createElement('div');
            item.className = 'timeline-item fade-in-up';
            item.style.animationDelay = `${delay}s`;
            
            item.innerHTML = `
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                    <div class="timeline-meta">
                        <span>Era: ${ev.era}</span>
                        <span>|</span>
                        <span>${ev.faction}</span>
                    </div>
                    <h4 class="timeline-title">${ev.title}</h4>
                    <p class="timeline-desc">${ev.description}</p>
                </div>
            `;
            this.elements.timelineContainer.appendChild(item);
        });
    },

    /* --- Render Zanpakuto Armory --- */
    renderArmory(zanpakutos) {
        this.elements.armoryGrid.innerHTML = '';
        zanpakutos.forEach((z, index) => {
            const delay = index * 0.2;
            const containerId = `armory-item-${z.id}`;
            const item = document.createElement('div');
            item.className = 'armory-item fade-in-up';
            item.style.animationDelay = `${delay}s`;
            item.id = containerId;
            
            item.innerHTML = `
                <div class="armory-visuals">
                    <!-- Images overlayed, Bankai hidden initially -->
                    <img src="${z.bankai.image}" alt="${z.bankai.name}" class="armory-img bankai-img hidden" id="bankai-img-${z.id}">
                    <img src="${z.shikai.image}" alt="${z.name}" class="armory-img shikai-img" id="shikai-img-${z.id}">
                </div>
                <div class="armory-details">
                    <h3 class="armory-name" id="name-${z.id}">${z.name}</h3>
                    <div class="armory-owner">Wielder: ${z.owner}</div>
                    
                    <!-- The Interactive Switch -->
                    <div class="release-switch" id="switch-${z.id}">
                        <div class="switch-highlight"></div>
                        <button class="switch-btn active" data-state="shikai">Shikai</button>
                        <button class="switch-btn" data-state="bankai">Bankai</button>
                    </div>

                    <div class="armory-command" id="command-${z.id}">"${z.shikai.command}"</div>
                    <p class="armory-desc" id="desc-${z.id}">${z.shikai.description}</p>
                </div>
            `;
            this.elements.armoryGrid.appendChild(item);

            // Setup Switch Listener
            const switchContainer = document.getElementById(`switch-${z.id}`);
            const buttons = switchContainer.querySelectorAll('.switch-btn');
            
            buttons.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const state = e.target.getAttribute('data-state');
                    if(e.target.classList.contains('active')) return;
                    
                    // Update Switch UI
                    buttons.forEach(b => b.classList.remove('active'));
                    e.target.classList.add('active');
                    
                    if (state === 'bankai') {
                        switchContainer.classList.add('bankai-mode');
                        this.toggleZanpakutoState(z.id, z.bankai, 'bankai');
                    } else {
                        switchContainer.classList.remove('bankai-mode');
                        this.toggleZanpakutoState(z.id, { name: z.name, ...z.shikai }, 'shikai');
                    }
                });
            });
        });
    },

    toggleZanpakutoState(id, data, mode) {
        // DOM targets
        const nameEl = document.getElementById(`name-${id}`);
        const commandEl = document.getElementById(`command-${id}`);
        const descEl = document.getElementById(`desc-${id}`);
        
        const shikaiImg = document.getElementById(`shikai-img-${id}`);
        const bankaiImg = document.getElementById(`bankai-img-${id}`);

        // Update Text Content
        nameEl.textContent = data.name;
        commandEl.textContent = `"${data.command}"`;
        descEl.textContent = data.description;
        
        if (mode === 'bankai') {
             // Reiatsu text effect on Bankai
             nameEl.style.textShadow = '0 0 15px var(--hollow-red)';
             commandEl.style.color = 'var(--hollow-red)';
             commandEl.style.borderColor = 'var(--hollow-red)';
             
             // Crossfade images
             shikaiImg.classList.add('hidden');
             bankaiImg.classList.remove('hidden');
        } else {
             nameEl.style.textShadow = 'none';
             commandEl.style.color = 'var(--reiatsu-blue)';
             commandEl.style.borderColor = 'var(--reiatsu-blue)';
             
             bankaiImg.classList.add('hidden');
             shikaiImg.classList.remove('hidden');
        }
    }
};
