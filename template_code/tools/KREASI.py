import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# CSS LAYOUT & FIX HEADER / IFRAME FULL-WIDTH
# ==============================================================================
st.markdown(
    """
    <style>
    /* Jarak atas aman agar judul tidak terpotong navbar */
    .block-container {
        max-width: 95% !important;
        padding-top: 5rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        margin: 0 auto !important;
    }

    /* Container Streamlit untuk Iframe agar full-width & centered */
    div[data-testid="stElementContainer"]:has(.stIFrame),
    div[data-testid="stElementContainer"]:has(iframe),
    .stElementContainer:has(.stIFrame) {
        width: 100% !important;
        max-width: 100% !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 auto !important;
    }

    /* Iframe Game Full Width */
    iframe.stIFrame,
    iframe[data-testid="stIFrame"],
    .stIFrame,
    iframe {
        width: 100% !important;
        min-width: 100% !important;
        max-width: 100% !important;
        display: block !important;
        margin: 0 auto !important;
        border: none !important;
    }

    /* Judul Utama */
    .game-header {
        text-align: center;
        margin-bottom: 12px;
        padding: 4px 0;
    }
    .game-title {
        font-weight: 800;
        color: #ff5e7e;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        font-size: clamp(1.8rem, 3.2vw, 2.5rem);
        line-height: 1.4 !important;
        margin: 0 0 4px 0;
        padding: 4px 0;
    }
    .game-subtitle {
        color: #666;
        font-size: 0.98rem;
        margin: 0 auto;
        max-width: 700px;
        line-height: 1.4;
    }
    </style>

    <div class="game-header">
        <h1 class="game-title">
            <span>🐍</span> <span>Jacobi Cyber Snake</span> <span>🌸</span>
        </h1>
        <p class="game-subtitle">
            Jelajahi arena digital Jacobi, santap <b>Kelopak Sakura & Bintang Berkilau</b>, dan cetak skor tertinggi!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# GAME ENGINE (HTML5 Canvas Widescreen + Vanilla JS)
# ==============================================================================
game_html = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<style>
  * {
    box-sizing: border-box;
    user-select: none;
    -webkit-user-select: none;
    margin: 0;
    padding: 0;
  }
  html, body {
    width: 100%;
    background: transparent;
    color: #f1f1f1;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    overflow: hidden;
    padding: 4px 8px 16px 8px;
  }

  .game-wrapper {
    width: 100%;
    max-width: 1200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 auto;
  }

  /* HUD HEADER (PAPAN SKOR ATAS) */
  .hud {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 8px;
    background: #141722;
    padding: 8px 20px;
    border-radius: 12px;
    border: 1px solid rgba(255, 107, 139, 0.3);
    box-shadow: 0 4px 15px rgba(0,0,0,0.35);
  }
  .scores-group {
    display: flex;
    gap: 30px;
    align-items: center;
  }
  .score-box {
    display: flex;
    flex-direction: column;
  }
  .score-label {
    font-size: 0.68rem;
    color: #8f9bb3;
    text-transform: uppercase;
    letter-spacing: 1.3px;
    font-weight: 600;
  }
  .score-val {
    font-size: 1.45rem;
    font-weight: 800;
    color: #ff6b8b;
    text-shadow: 0 0 10px rgba(255, 107, 139, 0.5);
  }
  .high-val {
    color: #f6c90e;
    text-shadow: 0 0 10px rgba(246, 201, 14, 0.5);
  }

  .options-group {
    display: flex;
    gap: 10px;
    align-items: center;
  }
  .speed-select {
    background: #202434;
    color: #fff;
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 8px;
    padding: 6px 12px;
    font-size: 0.85rem;
    cursor: pointer;
    outline: none;
    transition: 0.2s;
  }
  .speed-select:hover {
    border-color: #ff6b8b;
  }
  .speed-select option {
    background: #191c28;
    color: #fff;
  }
  .sound-btn {
    background: #202434;
    border: 1px solid rgba(255,255,255,0.18);
    color: #fff;
    border-radius: 8px;
    padding: 6px 12px;
    cursor: pointer;
    font-size: 0.85rem;
    transition: 0.2s;
  }
  .sound-btn:hover {
    background: rgba(255, 107, 139, 0.35);
    border-color: #ff6b8b;
  }

  /* KANVAS WIDESCREEN PRESISI PIXEL: 1100 x 360 (55 baris x 18 kolom @ 20px) */
  .canvas-container {
    position: relative;
    width: 100%;
    border-radius: 14px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 24px rgba(255, 107, 139, 0.2);
    border: 2px solid rgba(255, 107, 139, 0.35);
    background: #0f1118;
    overflow: hidden;
  }
  canvas {
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 1100 / 360;
  }

  /* OVERLAY GAME OVER */
  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(14, 16, 24, 0.92);
    backdrop-filter: blur(5px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.25s ease;
  }
  .overlay.active {
    opacity: 1;
    pointer-events: auto;
  }
  .overlay h2 {
    font-size: 2.3rem;
    color: #ff4757;
    margin-bottom: 6px;
    font-weight: 900;
    letter-spacing: 1.2px;
  }
  .overlay p {
    font-size: 1.1rem;
    color: #d1d8e0;
    margin-bottom: 18px;
  }
  .btn-play {
    background: linear-gradient(135deg, #ff6b8b, #ff4757);
    color: #fff;
    border: none;
    padding: 10px 28px;
    font-size: 1rem;
    font-weight: 700;
    border-radius: 30px;
    cursor: pointer;
    box-shadow: 0 4px 16px rgba(255, 71, 87, 0.45);
    transition: transform 0.15s ease;
  }
  .btn-play:hover {
    transform: scale(1.05);
  }
  .btn-play:active {
    transform: scale(0.96);
  }

  /* BOTTOM BAR (PETUNJUK JELAS & TOMBOL MANUAL TERLIHAT UTUH 100%) */
  .bottom-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    margin-top: 10px;
    padding: 6px 4px 12px 4px;
    flex-wrap: nowrap;
    gap: 12px;
  }
  .tips {
    font-size: 0.92rem;
    color: #3e2632;
    font-weight: 500;
  }
  .badge {
    background: #ffe6ee;
    color: #c93b66;
    border: 1px solid #f7b4c8;
    padding: 3px 9px;
    border-radius: 6px;
    font-family: monospace;
    font-size: 0.88rem;
    font-weight: 700;
    box-shadow: 0 1px 3px rgba(200, 50, 100, 0.1);
  }

  /* D-PAD TOMBOL MANUAL (BINGKAI PINK & JELAS DIKLIK) */
  .controls-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    flex-shrink: 0;
  }
  .dpad-row {
    display: flex;
    gap: 6px;
  }
  .dpad-btn {
    width: 46px;
    height: 34px;
    background: #1e2230;
    border: 1.5px solid #ff6b8b;
    color: #ffffff;
    font-size: 0.95rem;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: 0.1s;
    user-select: none;
    box-shadow: 0 3px 8px rgba(0,0,0,0.35);
  }
  .dpad-btn:active {
    background: #ff6b8b;
    color: #fff;
    transform: scale(0.92);
  }
</style>
</head>
<body>

<div class="game-wrapper">
  <!-- Papan Skor Atas -->
  <div class="hud">
    <div class="scores-group">
      <div class="score-box">
        <span class="score-label">POIN SAAT INI</span>
        <span class="score-val" id="score">0</span>
      </div>
      <div class="score-box">
        <span class="score-label">REKOR TERTINGGI</span>
        <span class="score-val high-val" id="highScore">0</span>
      </div>
    </div>

    <div class="options-group">
      <label style="font-size:0.75rem; color:#8f9bb3; text-transform:uppercase; font-weight:600;">Kecepatan:</label>
      <select id="speedSelect" class="speed-select">
        <option value="210" selected>🐢 Santai (Pelan)</option>
        <option value="160">🚶 Normal</option>
        <option value="115">⚡ Cepat</option>
      </select>
      <button class="sound-btn" id="soundToggle" title="Nyalakan/Matikan Suara">🔊 On</button>
    </div>
  </div>

  <!-- Arena Landscape Tepat 1100 x 360 (55 x 18 sel penuh tanpa potongan) -->
  <div class="canvas-container">
    <canvas id="gameCanvas" width="1100" height="360"></canvas>
    <div class="overlay" id="overlay">
      <h2 id="overlayTitle">GAME OVER</h2>
      <p id="overlaySub">Skor kamu: <span id="finalScore" style="color: #ff6b8b; font-weight:bold;">0</span></p>
      <button class="btn-play" id="btnRestart">Main Lagi 🌸</button>
    </div>
  </div>

  <!-- Kontrol Manual & Tips Keyboard -->
  <div class="bottom-bar">
    <div class="tips">
      🎮 Kendalikan cacing dengan <span class="badge">WASD</span> atau <span class="badge">Tombol Panah</span> di keyboard, atau klik tombol manual di samping:
    </div>

    <div class="controls-wrapper">
      <div class="dpad-row">
        <button class="dpad-btn" id="btnUp">▲</button>
      </div>
      <div class="dpad-row">
        <button class="dpad-btn" id="btnLeft">◀</button>
        <button class="dpad-btn" id="btnDown">▼</button>
        <button class="dpad-btn" id="btnRight">▶</button>
      </div>
    </div>
  </div>
</div>

<script>
// ==========================================
// 1. AUDIO SYNTHESIZER
// ==========================================
let audioEnabled = true;
const soundToggle = document.getElementById('soundToggle');
soundToggle.addEventListener('click', () => {
  audioEnabled = !audioEnabled;
  soundToggle.textContent = audioEnabled ? '🔊 On' : '🔇 Off';
});

let audioCtx = null;
function initAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
}

function playBeep(freq, type = 'sine', duration = 0.08) {
  if (!audioEnabled) return;
  try {
    initAudio();
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  } catch (e) {}
}

function playEatSound() {
  playBeep(580, 'sine', 0.06);
  setTimeout(() => playBeep(880, 'triangle', 0.1), 50);
}

function playGameOverSound() {
  playBeep(260, 'sawtooth', 0.15);
  setTimeout(() => playBeep(180, 'sawtooth', 0.25), 120);
}

// ==========================================
// 2. LOGIKA PERMAINAN (Presisi 55 Kolom x 18 Baris @ 20px)
// ==========================================
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreEl = document.getElementById('score');
const highScoreEl = document.getElementById('highScore');
const overlay = document.getElementById('overlay');
const finalScoreEl = document.getElementById('finalScore');
const btnRestart = document.getElementById('btnRestart');
const speedSelect = document.getElementById('speedSelect');

// Grid Landscape Presisi: 55 Kolom (55 * 20 = 1100px) x 18 Baris (18 * 20 = 360px)
const COLS = 55;
const ROWS = 18;
const CELL_SIZE = 20;

let snake = [];
let dir = { x: 1, y: 0 };
let nextDir = { x: 1, y: 0 };
let food = { x: 27, y: 9, icon: '🌸' };
let score = 0;
let highScore = parseInt(localStorage.getItem('jacobi_snake_high') || '0', 10);
highScoreEl.textContent = highScore;

let isGameOver = false;
let isRunning = false;

let gameSpeed = parseInt(speedSelect.value, 10);
speedSelect.addEventListener('change', (e) => {
  gameSpeed = parseInt(e.target.value, 10);
});

let lastTickTime = 0;
let particles = [];

// Objek Pengganti Apel: Sakura & Bintang Berkilau
const FOOD_ICONS = ['🌸', '✨', '⭐', '🌸'];

function spawnFood() {
  let valid = false;
  let newFood = {};
  while (!valid) {
    newFood.x = Math.floor(Math.random() * COLS);
    newFood.y = Math.floor(Math.random() * ROWS);
    valid = !snake.some(seg => seg.x === newFood.x && seg.y === newFood.y);
  }
  newFood.icon = FOOD_ICONS[Math.floor(Math.random() * FOOD_ICONS.length)];
  food = newFood;
}

function createBurst(x, y, color = '#ff6b8b') {
  for (let i = 0; i < 8; i++) {
    const angle = (Math.PI * 2 / 8) * i + Math.random() * 0.2;
    const speed = 1.5 + Math.random() * 2;
    particles.push({
      x: x * CELL_SIZE + CELL_SIZE / 2,
      y: y * CELL_SIZE + CELL_SIZE / 2,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed,
      alpha: 1,
      size: 3 + Math.random() * 2,
      color: color
    });
  }
}

function resetGame() {
  const startX = 14;
  const startY = 9;
  snake = [
    { x: startX, y: startY },
    { x: startX - 1, y: startY },
    { x: startX - 2, y: startY },
    { x: startX - 3, y: startY }
  ];
  dir = { x: 1, y: 0 };
  nextDir = { x: 1, y: 0 };
  score = 0;
  scoreEl.textContent = score;
  isGameOver = false;
  isRunning = true;
  particles = [];
  spawnFood();
  overlay.classList.remove('active');
}

function setDirection(dx, dy) {
  if (isGameOver) return;
  if (!isRunning) {
    resetGame();
    return;
  }
  if (dx !== 0 && dir.x === -dx) return;
  if (dy !== 0 && dir.y === -dy) return;
  nextDir = { x: dx, y: dy };
  initAudio();
}

window.addEventListener('keydown', (e) => {
  const k = e.key.toLowerCase();
  if (k === 'arrowup' || k === 'w') {
    e.preventDefault();
    setDirection(0, -1);
  } else if (k === 'arrowdown' || k === 's') {
    e.preventDefault();
    setDirection(0, 1);
  } else if (k === 'arrowleft' || k === 'a') {
    e.preventDefault();
    setDirection(-1, 0);
  } else if (k === 'arrowright' || k === 'd') {
    e.preventDefault();
    setDirection(1, 0);
  } else if (k === ' ' && isGameOver) {
    e.preventDefault();
    resetGame();
  }
});

document.getElementById('btnUp').onclick = () => setDirection(0, -1);
document.getElementById('btnDown').onclick = () => setDirection(0, 1);
document.getElementById('btnLeft').onclick = () => setDirection(-1, 0);
document.getElementById('btnRight').onclick = () => setDirection(1, 0);
btnRestart.onclick = () => resetGame();

function updateGame() {
  dir = { ...nextDir };
  const head = { x: snake[0].x + dir.x, y: snake[0].y + dir.y };

  if (head.x < 0 || head.x >= COLS || head.y < 0 || head.y >= ROWS) {
    triggerGameOver();
    return;
  }

  for (let i = 0; i < snake.length; i++) {
    if (head.x === snake[i].x && head.y === snake[i].y) {
      triggerGameOver();
      return;
    }
  }

  snake.unshift(head);

  if (head.x === food.x && head.y === food.y) {
    score += 10;
    scoreEl.textContent = score;
    if (score > highScore) {
      highScore = score;
      highScoreEl.textContent = highScore;
      localStorage.setItem('jacobi_snake_high', highScore);
    }
    createBurst(food.x, food.y, food.icon === '⭐' ? '#ffd32a' : '#ff758c');
    playEatSound();
    spawnFood();
  } else {
    snake.pop();
  }
}

function triggerGameOver() {
  isGameOver = true;
  isRunning = false;
  playGameOverSound();
  finalScoreEl.textContent = score;
  overlay.classList.add('active');
}

// ==========================================
// 3. RENDER LOOP
// ==========================================
function draw() {
  ctx.fillStyle = '#0f1118';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = 'rgba(255, 255, 255, 0.025)';
  ctx.lineWidth = 1;
  for (let x = 0; x < canvas.width; x += CELL_SIZE) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, canvas.height);
    ctx.stroke();
  }
  for (let y = 0; y < canvas.height; y += CELL_SIZE) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(canvas.width, y);
    ctx.stroke();
  }

  const fx = food.x * CELL_SIZE + CELL_SIZE / 2;
  const fy = food.y * CELL_SIZE + CELL_SIZE / 2;
  const pulse = Math.sin(Date.now() / 250) * 2;
  ctx.save();
  ctx.font = `${CELL_SIZE - 2 + pulse}px sans-serif`;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(food.icon, fx, fy);
  ctx.restore();

  for (let i = 0; i < snake.length; i++) {
    const seg = snake[i];
    const px = seg.x * CELL_SIZE;
    const py = seg.y * CELL_SIZE;

    if (i === 0) {
      ctx.fillStyle = '#ff6b8b';
      ctx.beginPath();
      ctx.roundRect(px + 1, py + 1, CELL_SIZE - 2, CELL_SIZE - 2, 6);
      ctx.fill();

      ctx.fillStyle = '#ffffff';
      let eye1 = { x: px + 6, y: py + 6 };
      let eye2 = { x: px + 14, y: py + 6 };
      if (dir.y === 1) {
        eye1 = { x: px + 6, y: py + 14 };
        eye2 = { x: px + 14, y: py + 14 };
      } else if (dir.x === -1) {
        eye1 = { x: px + 6, y: py + 6 };
        eye2 = { x: px + 6, y: py + 14 };
      } else if (dir.x === 1) {
        eye1 = { x: px + 14, y: py + 6 };
        eye2 = { x: px + 14, y: py + 14 };
      }
      ctx.beginPath();
      ctx.arc(eye1.x, eye1.y, 2.3, 0, Math.PI * 2);
      ctx.arc(eye2.x, eye2.y, 2.3, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#111';
      ctx.beginPath();
      ctx.arc(eye1.x, eye1.y, 1.1, 0, Math.PI * 2);
      ctx.arc(eye2.x, eye2.y, 1.1, 0, Math.PI * 2);
      ctx.fill();
    } else {
      const ratio = i / Math.max(snake.length, 20);
      const r = Math.round(255 - ratio * 150);
      const g = Math.round(107 + ratio * 80);
      const b = Math.round(139 + ratio * 90);
      ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;

      ctx.beginPath();
      ctx.roundRect(px + 2, py + 2, CELL_SIZE - 4, CELL_SIZE - 4, 5);
      ctx.fill();
    }
  }

  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    p.alpha -= 0.035;
    if (p.alpha <= 0) {
      particles.splice(i, 1);
      continue;
    }
    ctx.save();
    ctx.globalAlpha = p.alpha;
    ctx.fillStyle = p.color;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }
}

function gameLoop(timestamp) {
  if (isRunning && timestamp - lastTickTime > gameSpeed) {
    updateGame();
    lastTickTime = timestamp;
  }
  draw();
  requestAnimationFrame(gameLoop);
}

resetGame();
requestAnimationFrame(gameLoop);
</script>
</body>
</html>
"""

# Render komponen HTML dengan tinggi 630px
components.html(game_html, height=630, scrolling=False)

# ==============================================================================
# DESKRIPSI GAME RINGKAS & MENARIK (KOTAK RAMPING & TIDAK MELEBAR TINGGI)
# ==============================================================================
st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="background: rgba(255, 240, 245, 0.75); border: 1px solid #F5C2D7; border-radius: 10px; padding: 10px 14px; height: 100%; box-shadow: 0 2px 6px rgba(216, 90, 127, 0.05);">
            <div style="font-size: 0.95rem; font-weight: 700; color: #9E3356; margin-bottom: 2px;">🌸 Legenda Cyber Snake</div>
            <p style="font-size: 0.82rem; color: #555; line-height: 1.4; margin: 0;">
                Kendalikan Ular Cyber di taman digital Jacobi. Setiap kelopak <b>Sakura</b> & <b>Bintang</b> yang disantap membuat tubuhmu kian panjang!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div style="background: rgba(240, 248, 255, 0.75); border: 1px solid #BDD8F1; border-radius: 10px; padding: 10px 14px; height: 100%; box-shadow: 0 2px 6px rgba(70, 130, 180, 0.05);">
            <div style="font-size: 0.95rem; font-weight: 700; color: #1E3A5F; margin-bottom: 2px;">🎯 Misi & Aturan Main</div>
            <p style="font-size: 0.82rem; color: #555; line-height: 1.4; margin: 0;">
                Gunakan <b>WASD / Panah</b>. Kumpulkan poin sebanyak-banyaknya dan hindari menabrak dinding batas maupun tubuhmu sendiri!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div style="background: rgba(255, 250, 235, 0.75); border: 1px solid #F5DEB3; border-radius: 10px; padding: 10px 14px; height: 100%; box-shadow: 0 2px 6px rgba(200, 155, 60, 0.05);">
            <div style="font-size: 0.95rem; font-weight: 700; color: #8A6D1C; margin-bottom: 2px;">💡 Trik Meraih Skor Tinggi</div>
            <p style="font-size: 0.82rem; color: #555; line-height: 1.4; margin: 0;">
                Saat tubuhmu semakin panjang, bermanuverlah merayap di sepanjang tepian dinding agar ruang tengah tetap aman dan lapang.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div style="text-align: center; margin-top: 12px; padding: 8px 12px; background: rgba(255, 255, 255, 0.6); border-radius: 8px; border: 1px dashed #F5C2D7; color: #8C5368; font-size: 0.82rem; font-style: italic;">
        "Kendalikan setiap pergerakan layaknya seorang Data Scientist: tenang, terukur, dan penuh presisi!"
    </div>
    """,
    unsafe_allow_html=True,
)
