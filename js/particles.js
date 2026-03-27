class ReiatsuParticles {
    constructor() {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.numParticles = 50;

        document.body.prepend(this.canvas);
        this.initCanvas();
        this.createParticles();
        this.animate();

        window.addEventListener('resize', () => this.initCanvas());
    }

    initCanvas() {
        this.canvas.style.position = 'fixed';
        this.canvas.style.top = '0';
        this.canvas.style.left = '0';
        this.canvas.style.width = '100vw';
        this.canvas.style.height = '100vh';
        this.canvas.style.zIndex = '0'; // Ensures it sits above the app-background but behind UI panels
        this.canvas.style.pointerEvents = 'none';
        this.canvas.style.opacity = '0.6'; // Boosted visibility
        
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    createParticles() {
        this.particles = [];
        for (let i = 0; i < this.numParticles; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                size: Math.random() * 3 + 1,
                speedX: Math.random() * 1 - 0.5,
                speedY: Math.random() * -2 - 0.5, // Float upwards
                color: Math.random() > 0.8 ? '#ff4040' : '#40e0d0', // Mostly blue, some red
                opacity: Math.random() * 0.5 + 0.1
            });
        }
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        for (let i = 0; i < this.particles.length; i++) {
            let p = this.particles[i];
            
            this.ctx.beginPath();
            this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            this.ctx.fillStyle = p.color;
            this.ctx.globalAlpha = p.opacity;
            this.ctx.fill();
            
            // Wiggle effect
            p.x += p.speedX + (Math.random() * 0.5 - 0.25);
            p.y += p.speedY;

            // Reset when off screen
            if (p.y < -10) {
                p.y = this.canvas.height + 10;
                p.x = Math.random() * this.canvas.width;
            }
        }
        
        requestAnimationFrame(() => this.animate());
    }
}

// Inizializza al caricamento
document.addEventListener('DOMContentLoaded', () => {
    new ReiatsuParticles();
});
