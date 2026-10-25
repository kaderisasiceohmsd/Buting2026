"""
game_helper.py
Mini games untuk bagian "Kreasi Tensor!!" – Buku Kating Digital TENSOR 2026
Dark Violet Theme · dimainkan langsung di browser (HTML5 canvas di dalam st.components)

Pemakaian:
    from tools.ui_helper import load_image
    from tools.game_helper import render_flappy

    TIM = {"Ahmad Fadylah": "https://drive.google.com/...", ...}
    render_flappy({nama: load_image(url, fallback_name=nama) for nama, url in TIM.items()})
"""

import base64
import json
from io import BytesIO

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageOps


def face_data_uri(img: Image.Image, size: int = 128, centering=(0.5, 0.3)) -> str:
    """Potong foto jadi persegi (fokus ke bagian atas/wajah) dan ubah ke data-URI JPEG kecil."""
    img = ImageOps.fit(
        img.convert("RGB"), (size, size), method=Image.Resampling.LANCZOS, centering=centering
    )
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=85)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def _characters_json(characters: dict) -> str:
    """characters: {nama: PIL.Image | data-URI str} -> JSON aman untuk disisipkan ke <script>."""
    items = []
    for name, src in characters.items():
        uri = src if isinstance(src, str) and src.startswith("data:") else face_data_uri(src)
        items.append({"name": str(name), "img": uri})
    return json.dumps(items, ensure_ascii=False).replace("</", "<\\/")


# ─────────────────────────────────────────────────────────────────────────────
# FLAPPY TENSOR
# ─────────────────────────────────────────────────────────────────────────────

_FLAPPY_HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
  html, body {
    height: 100%; overflow: hidden; background: transparent;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    color: #f1f5f9;
    -webkit-user-select: none; user-select: none;
  }
  .app { height: 100%; display: flex; flex-direction: column; gap: 6px; padding: 4px; }
  .stage { flex: 1 1 auto; min-height: 0; display: flex; align-items: center; justify-content: center; }
  .frame {
    border-radius: 16px; overflow: hidden; line-height: 0;
    border: 1px solid rgba(139, 92, 246, 0.4);
    box-shadow: 0 12px 36px rgba(139, 92, 246, 0.25);
    background: #0c0a17;
  }
  canvas { display: block; touch-action: manipulation; cursor: pointer; outline: none; }
  .bar { flex: 0 0 auto; }
  .row { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 2px 2px 0; }
  .label { font-size: 11px; font-weight: 700; letter-spacing: .09em; text-transform: uppercase; color: #a78bfa; }
  .picker { display: flex; gap: 10px; overflow-x: auto; padding: 6px 2px 2px; scrollbar-width: thin; }
  .av { flex: 0 0 auto; width: 52px; text-align: center; cursor: pointer; opacity: .6; transition: opacity .2s, transform .2s; }
  .av:hover { opacity: .9; transform: translateY(-2px); }
  .av img {
    width: 42px; height: 42px; border-radius: 50%; object-fit: cover; display: block; margin: 0 auto;
    border: 2px solid rgba(139, 92, 246, .35);
  }
  .av span { display: block; font-size: 10px; margin-top: 3px; color: #94a3b8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .av.on { opacity: 1; }
  .av.on img { border-color: #c4b5fd; box-shadow: 0 0 0 3px rgba(167, 139, 250, .35); }
  .av.on span { color: #e9d5ff; font-weight: 700; }
</style>
</head>
<body>
<div class="app">
  <div class="stage" id="stage"><div class="frame"><canvas id="c" tabindex="0"></canvas></div></div>
  <div class="bar">
    <div class="row"><span class="label">Pilih karakter</span></div>
    <div class="picker" id="picker"></div>
  </div>
</div>

<script>
(function () {
  var CHARS = __CHARACTERS__;
  var DEFAULT_NAME = __DEFAULT__;

  // ───────── konstanta ─────────
  var W = 360, H = 560, GROUND = 70, PX = 96, R = 19, PW = 62;   // W menyesuaikan lebar layar
  var GAP0 = 158, GAP_MIN = 128, SPACING = 200;

  var canvas = document.getElementById('c');
  var ctx = canvas.getContext('2d');
  var stage = document.getElementById('stage');
  var dpr = Math.min(window.devicePixelRatio || 1, 2);

  // ───────── state ─────────
  var state = 'ready', score = 0, best = 0, shake = 0, overAt = 0, groundX = 0, tick = 0;
  try { best = +localStorage.getItem('tensorFlappyBest') || 0; } catch (e) {}
  var bird = { y: H / 2 - 20, vy: 0, rot: 0, sprite: null, name: '' };
  var pipes = [];
  var bits = [];
  function newBit() {
    return { x: Math.random() * W, y: Math.random() * (H - GROUND), s: 10 + Math.random() * 14,
             v: 0.15 + Math.random() * 0.35, c: Math.random() < 0.5 ? '0' : '1' };
  }

  // Dunia game selalu setinggi H; lebarnya mengikuti rasio area yang tersedia (layar lebar = dunia lebih lebar)
  function fit() {
    var cw = stage.clientWidth - 4, ch = stage.clientHeight - 4;
    if (cw < 60 || ch < 60) return;
    var oldW = W;
    W = Math.max(320, Math.min(1500, Math.round(H * cw / ch)));
    var sc = Math.min(cw / W, ch / H);
    canvas.style.width = Math.floor(W * sc) + 'px';
    canvas.style.height = Math.floor(H * sc) + 'px';
    canvas.width = Math.round(W * sc * dpr);
    canvas.height = Math.round(H * sc * dpr);
    ctx.setTransform(canvas.width / W, 0, 0, canvas.height / H, 0, 0);
    PX = Math.max(96, Math.round(W * 0.25));
    if (W !== oldW) { for (var i = 0; i < bits.length; i++) bits[i].x = bits[i].x / oldW * W; }
    while (bits.length < Math.round(W / 16)) bits.push(newBit());
  }

  function gapNow()   { return Math.max(GAP_MIN, GAP0 - score * 2); }
  function speedNow() { return Math.min(4, 2.3 + score * 0.04); }
  function addPipe(x) {
    var gap = gapNow(), minTop = 60, maxTop = H - GROUND - 60 - gap;
    pipes.push({ x: x, top: minTop + Math.random() * (maxTop - minTop), gap: gap, passed: false });
  }
  function reset() { pipes = []; score = 0; bird.y = H / 2 - 20; bird.vy = 0; bird.rot = 0; state = 'ready'; }
  function flap()  { bird.vy = -7.4; }
  function start() { state = 'play'; addPipe(PX + 340); flap(); }
  function die() {
    state = 'over'; shake = 9; overAt = Date.now(); bird.vy = -3;
    if (score > best) { best = score; try { localStorage.setItem('tensorFlappyBest', String(best)); } catch (e) {} }
  }
  function action() {
    if (state === 'ready') start();
    else if (state === 'play') flap();
    else if (state === 'over' && Date.now() - overAt > 500) reset();
  }

  // ───────── collision ─────────
  function circleRect(cx, cy, r, rx, ry, rw, rh) {
    var nx = Math.max(rx, Math.min(cx, rx + rw)), ny = Math.max(ry, Math.min(cy, ry + rh));
    var dx = cx - nx, dy = cy - ny;
    return dx * dx + dy * dy < r * r;
  }
  function hit(p) {
    var r = R - 3, y2 = p.top + p.gap;
    return circleRect(PX, bird.y, r, p.x, 0, PW, p.top) ||
           circleRect(PX, bird.y, r, p.x, y2, PW, H) ||
           circleRect(PX, bird.y, r, p.x - 5, p.top - 22, PW + 10, 22) ||
           circleRect(PX, bird.y, r, p.x - 5, y2, PW + 10, 22);
  }

  // ───────── update (60 Hz tetap) ─────────
  function update() {
    tick++;
    var sp = state === 'play' ? speedNow() : (state === 'ready' ? 1.6 : 0);
    groundX = (groundX + sp) % 24;
    for (var i = 0; i < bits.length; i++) {
      var b = bits[i];
      if (state !== 'over') b.x -= b.v;
      if (b.x < -20) { b.x = W + 20; b.y = Math.random() * (H - GROUND); }
    }
    shake *= 0.88;

    if (state === 'ready') { bird.y = H / 2 - 20 + Math.sin(tick / 14) * 8; bird.rot = 0; return; }

    if (state === 'play') {
      bird.vy = Math.min(bird.vy + 0.42, 10);
      bird.y += bird.vy;
      bird.rot = Math.max(-0.45, Math.min(1.1, bird.vy * 0.07));
      for (var k = 0; k < pipes.length; k++) pipes[k].x -= sp;
      if (pipes.length && pipes[0].x < -PW - 12) pipes.shift();
      var last = pipes[pipes.length - 1];
      if (!last) { addPipe(W + 20); last = pipes[pipes.length - 1]; }
      while (last.x + SPACING < W + 20) { addPipe(last.x + SPACING); last = pipes[pipes.length - 1]; }
      for (var m = 0; m < pipes.length; m++) {
        var p = pipes[m];
        if (!p.passed && p.x + PW < PX - R) { p.passed = true; score++; }
      }
      if (bird.y - R < 0) { bird.y = R; bird.vy = 0; }
      if (bird.y + R >= H - GROUND) { bird.y = H - GROUND - R; die(); return; }
      for (var n = 0; n < pipes.length; n++) { if (hit(pipes[n])) { die(); return; } }
    } else if (state === 'over') {
      if (bird.y + R < H - GROUND) {
        bird.vy = Math.min(bird.vy + 0.5, 12); bird.y += bird.vy;
        bird.rot = Math.min(1.5, bird.rot + 0.08);
        if (bird.y + R > H - GROUND) bird.y = H - GROUND - R;
      }
    }
  }

  // ───────── gambar ─────────
  function rrect(x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
  }
  function text(str, x, y, size, color, weight) {
    ctx.font = (weight || 800) + ' ' + size + 'px Inter, system-ui, sans-serif';
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.lineWidth = Math.max(3, size / 7); ctx.strokeStyle = 'rgba(12,10,23,.85)'; ctx.lineJoin = 'round';
    ctx.strokeText(str, x, y); ctx.fillStyle = color; ctx.fillText(str, x, y);
  }

  function drawBackground() {
    var g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, '#1d1240'); g.addColorStop(0.65, '#0f0b22'); g.addColorStop(1, '#0c0a17');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = 'rgba(167,139,250,.10)'; ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
    for (var i = 0; i < bits.length; i++) {
      var b = bits[i];
      ctx.font = '700 ' + b.s + 'px monospace'; ctx.fillText(b.c, b.x, b.y);
    }
  }

  function drawPipe(p) {
    var x = p.x, y2 = p.top + p.gap, bottomH = H - GROUND - y2;
    var bg = ctx.createLinearGradient(x, 0, x + PW, 0);
    bg.addColorStop(0, '#5b21b6'); bg.addColorStop(0.5, '#8b5cf6'); bg.addColorStop(1, '#5b21b6');
    ctx.fillStyle = bg;
    ctx.fillRect(x, 0, PW, p.top); ctx.fillRect(x, y2, PW, bottomH);
    // garis sel matriks
    ctx.strokeStyle = 'rgba(255,255,255,.13)'; ctx.lineWidth = 1; ctx.beginPath();
    for (var y = p.top; y > 0; y -= 22) { ctx.moveTo(x, y); ctx.lineTo(x + PW, y); }
    for (var y3 = y2; y3 < H - GROUND; y3 += 22) { ctx.moveTo(x, y3); ctx.lineTo(x + PW, y3); }
    ctx.moveTo(x + PW / 2, 0); ctx.lineTo(x + PW / 2, p.top);
    ctx.moveTo(x + PW / 2, y2); ctx.lineTo(x + PW / 2, H - GROUND);
    ctx.stroke();
    // tutup emas
    [[p.top - 22], [y2]].forEach(function (c) {
      var cy = c[0], cg = ctx.createLinearGradient(0, cy, 0, cy + 22);
      cg.addColorStop(0, '#f6d77a'); cg.addColorStop(1, '#c8932a');
      ctx.fillStyle = cg; ctx.fillRect(x - 5, cy, PW + 10, 22);
      ctx.strokeStyle = 'rgba(12,10,23,.45)'; ctx.lineWidth = 2; ctx.strokeRect(x - 5, cy, PW + 10, 22);
    });
  }

  function drawGround() {
    var gy = H - GROUND;
    ctx.fillStyle = '#130f24'; ctx.fillRect(0, gy, W, GROUND);
    ctx.fillStyle = '#8b5cf6'; ctx.fillRect(0, gy, W, 3);
    ctx.fillStyle = 'rgba(139,92,246,.35)';
    for (var x = -groundX; x < W; x += 24) { ctx.fillRect(x, gy + 16, 12, 4); ctx.fillRect(x + 12, gy + 36, 12, 4); }
  }

  function drawBird() {
    ctx.save(); ctx.translate(PX, bird.y); ctx.rotate(bird.rot * 0.6);
    // sayap
    ctx.save(); ctx.rotate(bird.vy < 0 ? -0.6 : 0.35);
    ctx.fillStyle = 'rgba(196,181,253,.95)'; ctx.beginPath();
    ctx.ellipse(-R + 1, 5, 12, 6, 0, 0, Math.PI * 2); ctx.fill(); ctx.restore();
    // bingkai + foto
    ctx.shadowColor = 'rgba(139,92,246,.8)'; ctx.shadowBlur = 14;
    ctx.beginPath(); ctx.arc(0, 0, R, 0, Math.PI * 2); ctx.fillStyle = '#1c1636'; ctx.fill(); ctx.shadowBlur = 0;
    ctx.save(); ctx.beginPath(); ctx.arc(0, 0, R - 1.5, 0, Math.PI * 2); ctx.clip();
    if (bird.sprite) ctx.drawImage(bird.sprite, -R, -R, R * 2, R * 2);
    else { ctx.fillStyle = '#6d28d9'; ctx.fillRect(-R, -R, R * 2, R * 2); text('T', 0, 1, 22, '#fff', 800); }
    ctx.restore();
    ctx.lineWidth = 3; ctx.strokeStyle = '#c4b5fd'; ctx.beginPath(); ctx.arc(0, 0, R - 1.5, 0, Math.PI * 2); ctx.stroke();
    ctx.restore();
  }

  function drawPanel(lines) {
    ctx.fillStyle = 'rgba(12,10,23,.6)'; ctx.fillRect(0, 0, W, H - GROUND);
    rrect(W / 2 - 140, 150, 280, 210, 18);
    ctx.fillStyle = 'rgba(19,15,36,.96)'; ctx.fill();
    ctx.lineWidth = 1.5; ctx.strokeStyle = 'rgba(168,85,247,.5)'; ctx.stroke();
    lines.forEach(function (l) { text(l[0], W / 2, l[1], l[2], l[3], l[4]); });
  }

  function draw() {
    ctx.save();
    if (shake > 0.4) ctx.translate((Math.random() - 0.5) * shake, (Math.random() - 0.5) * shake);
    drawBackground();
    for (var i = 0; i < pipes.length; i++) drawPipe(pipes[i]);
    drawGround();
    drawBird();
    if (state === 'play') text(String(score), W / 2, 70, 52, '#ffffff', 800);
    if (state === 'ready') {
      drawPanel([
        ['FLAPPY TENSOR', 195, 26, '#e9d5ff', 800],
        ['Klik / ketuk atau tekan Spasi', 240, 14, '#cbd5e1', 500],
        ['Hindari tiang matriks!', 265, 14, '#cbd5e1', 500],
        ['Skor terbaik: ' + best, 318, 16, '#fde047', 700]
      ]);
    } else if (state === 'over') {
      var canRetry = Date.now() - overAt > 500;
      drawPanel([
        ['GAME OVER', 185, 28, '#f9a8d4', 800],
        [String(score), 238, 46, '#ffffff', 800],
        ['Terbaik: ' + best, 285, 16, '#fde047', 700],
        [canRetry ? 'Ketuk untuk main lagi' : ' ', 328, 14, '#cbd5e1', 500]
      ]);
    }
    ctx.restore();
  }

  // ───────── loop ─────────
  var lastT = 0, acc = 0, STEP = 1000 / 60;
  function loop(t) {
    if (!lastT) lastT = t;
    acc += Math.min(t - lastT, 100); lastT = t;
    while (acc >= STEP) { update(); acc -= STEP; }
    draw();
    requestAnimationFrame(loop);
  }

  // ───────── input ─────────
  canvas.addEventListener('pointerdown', function (e) { e.preventDefault(); canvas.focus(); action(); });
  window.addEventListener('keydown', function (e) {
    if (e.code === 'Space' || e.code === 'ArrowUp' || e.code === 'KeyW') { e.preventDefault(); action(); }
  });

  // ───────── karakter ─────────
  var picker = document.getElementById('picker');

  function makeFace(im) {
    var c = document.createElement('canvas'); c.width = c.height = 128;
    var s = Math.min(im.width, im.height);
    var sx = (im.width - s) / 2, sy = (im.height - s) * 0.25;
    c.getContext('2d').drawImage(im, sx, sy, s, s, 0, 0, 128, 128);
    return c;
  }
  function selectChar(i) {
    var c = CHARS[i]; if (!c) return;
    bird.name = c.name;
    var im = new Image();
    im.onload = function () { bird.sprite = makeFace(im); };
    im.src = c.img;
    Array.prototype.forEach.call(picker.children, function (el, idx) { el.classList.toggle('on', idx === i); });
    try { localStorage.setItem('tensorFlappyChar', c.name); } catch (e) {}
  }
  function buildPicker() {
    picker.innerHTML = '';
    CHARS.forEach(function (c, i) {
      var d = document.createElement('div'); d.className = 'av';
      var img = document.createElement('img'); img.src = c.img; img.alt = c.name;
      var sp = document.createElement('span'); sp.textContent = c.name.split(' ')[0];
      d.appendChild(img); d.appendChild(sp);
      d.addEventListener('click', function () { selectChar(i); });
      picker.appendChild(d);
    });
  }

  // ───────── mulai ─────────
  fit();
  window.addEventListener('resize', fit);
  if (typeof ResizeObserver !== 'undefined') new ResizeObserver(fit).observe(stage);
  buildPicker();
  var startIdx = 0, saved = '';
  try { saved = localStorage.getItem('tensorFlappyChar') || ''; } catch (e) {}
  for (var q = 0; q < CHARS.length; q++) {
    if (CHARS[q].name === (DEFAULT_NAME || saved)) { startIdx = q; break; }
  }
  if (CHARS.length) selectChar(startIdx);
  requestAnimationFrame(loop);
})();
</script>
</body>
</html>
"""


def _stage_css(key: str, offset: int, min_height: int) -> str:
    k = f'[class*="st-key-{key}"]'
    return f"""
    <style>
    /* semua pembungkus iframe dipaksa selebar area konten */
    {k},
    {k} > *,
    {k} [data-testid="stElementContainer"],
    {k} [data-testid="stIFrame"],
    {k} .element-container,
    {k} iframe {{
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
    }}
    {k} iframe {{
        height: calc(100vh - {offset}px) !important;
        height: calc(100dvh - {offset}px) !important;
        min-height: {min_height}px;
        border: 0;
        display: block;
    }}
    /* kalau game ditaruh di dalam st.columns, kolomnya dilebarkan penuh */
    [data-testid="stHorizontalBlock"]:has({k}) {{ flex-wrap: wrap !important; }}
    :is([data-testid="stColumn"], [data-testid="column"]):has({k}) {{
        flex: 1 1 100% !important;
        width: 100% !important;
        min-width: 100% !important;
    }}
    .block-container, [data-testid="stMainBlockContainer"] {{ padding-bottom: 1rem !important; }}
    </style>
    """


def render_flappy(characters: dict, default: str = "", offset: int = 90, min_height: int = 480):
    """
    Tampilkan game Flappy Tensor memenuhi area konten (sidebar tetap terlihat).

    characters : {nama: PIL.Image atau data-URI}  -> muncul sebagai pilihan karakter
    default    : nama karakter yang dipilih di awal (opsional)
    offset     : ruang (px) yang disisakan di atas/bawah game; naikkan jika ada judul di atasnya
    min_height : tinggi minimum game (px) untuk layar pendek
    """
    key = "game-stage-flappy"
    html = (
        _FLAPPY_HTML
        .replace("__CHARACTERS__", _characters_json(characters))
        .replace("__DEFAULT__", json.dumps(default, ensure_ascii=False))
    )
    st.markdown(_stage_css(key, offset, min_height), unsafe_allow_html=True)
    with st.container(key=key):
        components.html(html, height=700, scrolling=False)
