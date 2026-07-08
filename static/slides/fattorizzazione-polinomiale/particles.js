/* particles.js — animated background canvas
   Leggero, minimalista, coerente con mathofthings design
   Parametri: count, colorLight, opacity, linkDistance
*/

class ParticlesBackground {
  constructor(options = {}) {
    this.canvas = document.getElementById('particles-canvas');
    if (!this.canvas) {
      console.warn('particles-canvas element not found');
      return;
    }

    this.ctx = this.canvas.getContext('2d');
    this.count = options.count || 40;
    this.colorLight = options.colorLight || '#ed6f5c';
    this.colorDark = options.colorDark || '#f08e7c';
    this.opacity = options.opacity || 0.15;
    this.linkDistance = options.linkDistance || 150;
    this.particles = [];
    this.bgColor = null;

    this.isDark = document.documentElement.classList.contains('dark-mode') ||
      (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);

    this.resizeCanvas();
    this.initParticles();
    this.animate();

    window.addEventListener('resize', () => this.resizeCanvas());
  }

  setTheme(colorLight, colorDark, bgColor = null) {
    this.colorLight = colorLight;
    this.colorDark = colorDark;
    this.bgColor = bgColor;
  }

  resizeCanvas() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }

  initParticles() {
    this.particles = [];
    for (let i = 0; i < this.count; i++) {
      this.particles.push({
        x: Math.random() * this.canvas.width,
        y: Math.random() * this.canvas.height,
        vx: (Math.random() - 0.5) * 1.5,
        vy: (Math.random() - 0.5) * 1.5,
        radius: Math.random() * 1.5 + 0.5,
      });
    }
  }

  animate() {
    this.isDark = document.documentElement.classList.contains('dark-mode');

    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    if (this.bgColor) {
      this.ctx.fillStyle = this.bgColor;
      this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }

    const color = this.isDark ? this.colorDark : this.colorLight;
    const activeColor = color + Math.round(this.opacity * 255).toString(16).padStart(2, '0');
    const linkColor = color + Math.round(this.opacity * 0.5 * 255).toString(16).padStart(2, '0');

    // Aggiorna e disegna particelle
    for (let i = 0; i < this.particles.length; i++) {
      const p = this.particles[i];

      // Movimento
      p.x += p.vx;
      p.y += p.vy;

      // Bounce ai bordi
      if (p.x < 0 || p.x > this.canvas.width) p.vx *= -1;
      if (p.y < 0 || p.y > this.canvas.height) p.vy *= -1;

      // Clamp alla viewport
      p.x = Math.max(0, Math.min(this.canvas.width, p.x));
      p.y = Math.max(0, Math.min(this.canvas.height, p.y));

      // Disegna particella
      this.ctx.fillStyle = activeColor;
      this.ctx.beginPath();
      this.ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      this.ctx.fill();
    }

    // Disegna linee tra particelle vicine
    for (let i = 0; i < this.particles.length; i++) {
      for (let j = i + 1; j < this.particles.length; j++) {
        const p1 = this.particles[i];
        const p2 = this.particles[j];
        const dx = p1.x - p2.x;
        const dy = p1.y - p2.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < this.linkDistance) {
          this.ctx.strokeStyle = linkColor;
          this.ctx.lineWidth = 0.5;
          this.ctx.beginPath();
          this.ctx.moveTo(p1.x, p1.y);
          this.ctx.lineTo(p2.x, p2.y);
          this.ctx.stroke();
        }
      }
    }

    requestAnimationFrame(() => this.animate());
  }
}

// Inizializza al caricamento della pagina — esposta globalmente per slide-change
document.addEventListener('DOMContentLoaded', () => {
  window.particles = new ParticlesBackground({
    count: 120,
    colorLight: '#ed6f5c',
    colorDark: '#f08e7c',
    opacity: 0.55,
    linkDistance: 150,
  });
});
