import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cyber Hack: Terminal Override 4x4", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #030712;
    color: #ffffff;
}
h1 {
    color: #38bdf8 !important;
    font-family: 'Courier New', monospace;
    text-align: center;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

st.title("CYBER HACK: TERMINAL OVERRIDE")
st.markdown("<p style='text-align: center; color: #94a3b8;'>Matriks 16 node (4x4) responsif penuh! Lacak pergerakan anomali target tanpa terpotong.</p>", unsafe_allow_html=True)

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        background-color: #030712;
        color: #f8fafc;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 0;
        padding: 10px;
        overflow-x: hidden;
    }
    .stats-panel {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 15px;
    }
    .stat-box {
        background: #0f172a;
        border: 1px solid #38bdf8;
        padding: 8px 16px;
        border-radius: 8px;
        color: #38bdf8;
        font-size: 13px;
        font-weight: bold;
    }
    .trace-container {
        width: 100%;
        max-width: 500px;
        background: #1e293b;
        height: 10px;
        border-radius: 5px;
        margin: 0 auto 15px auto;
        overflow: hidden;
        border: 1px solid #38bdf8;
    }
    .trace-bar {
        width: 100%;
        height: 100%;
        background: #4ade80;
        transition: width 0.1s linear;
    }
    .mission-box {
        background: #0f172a;
        border: 2px dashed #38bdf8;
        padding: 10px;
        border-radius: 8px;
        margin: 0 auto 15px auto;
        max-width: 500px;
        font-size: 14px;
    }
    .target-highlight {
        color: #38bdf8;
        font-weight: bold;
        font-size: 16px;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin: 15px auto;
        width: 100%;
        max-width: 500px;
    }
    .node-box {
        background: #0f172a;
        border: 2px solid #38bdf8;
        border-radius: 8px;
        height: 80px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: transform 0.2s ease, border-color 0.2s, box-shadow 0.2s;
        box-shadow: 0 0 8px rgba(56, 189, 248, 0.15);
    }
    .node-box:hover {
        border-color: #4ade80;
        transform: scale(1.03);
        box-shadow: 0 0 12px rgba(74, 222, 128, 0.4);
    }
    .node-val {
        font-size: 16px;
        font-weight: bold;
        color: #f8fafc;
    }
    .terminal-msg {
        margin-top: 15px;
        font-size: 14px;
        font-weight: bold;
        height: 24px;
    }
    .action-btn {
        background-color: #38bdf8;
        color: #030712;
        border: none;
        padding: 12px 28px;
        font-size: 15px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 12px;
        font-family: 'Courier New', monospace;
        transition: background 0.2s;
    }
    .action-btn:hover {
        background-color: #4ade80;
    }
</style>
</head>
<body>

<div class="stats-panel">
    <div class="stat-box">SCORE: <span id="score">0</span></div>
    <div class="stat-box">LIVES: <span id="lives">3</span></div>
    <div class="stat-box">LEVEL: <span id="level">1</span></div>
</div>

<div class="trace-container">
    <div class="trace-bar" id="trace-bar"></div>
</div>

<div class="mission-box" id="mission-text">
    Inisialisasi matriks... Tekan tombol di bawah untuk mulai.
</div>

<div class="grid-container" id="grid-container"></div>

<div class="terminal-msg" id="terminal-msg"></div>
<button class="action-btn" id="main-btn" onclick="startHack()">MULAI OVERRIDE</button>

<script>
    let score = 0;
    let lives = 3;
    let level = 1;
    let nodes = [];
    let gameState = 'idle';
    let targetType = '';
    let traceTimer = null;
    let traceLeft = 100;
    let shuffleInterval = null;

    const totalNodes = 16;

    const pool = [
        { name: "Integer", vals: ["42", "108", "512", "999", "12", "7", "256", "88"] },
        { name: "Float", vals: ["3.14", "9.81", "0.55", "7.25", "4.19", "1.61", "0.25"] },
        { name: "String", vals: ["Alpha", "Beta", "Core", "Nexus", "Vector", "Stream", "Node"] },
        { name: "Boolean", vals: ["True", "False"] }
    ];

    function startHack() {
        score = 0;
        lives = 3;
        level = 1;
        document.getElementById('main-btn').style.display = 'none';
        initRound();
    }

    function initRound() {
        gameState = 'reveal';
        document.getElementById('terminal-msg').innerText = "";
        
        let domIdx = Math.floor(Math.random() * pool.length);
        let domType = pool[domIdx];
        let anomPool = pool.filter((_, i) => i !== domIdx);
        let anomType = anomPool[Math.floor(Math.random() * anomPool.length)];

        targetType = anomType.name;
        document.getElementById('mission-text').innerHTML = `TARGET PROTOKOL: Cari tipe data <span class="target-highlight">${targetType}</span>`;

        let rawNodes = [];
        for(let i=0; i<totalNodes - 1; i++) {
            let val = domType.vals[Math.floor(Math.random() * domType.vals.length)];
            rawNodes.push({ val: val, type: domType.name, isAnom: false });
        }
        let anomVal = anomType.vals[Math.floor(Math.random() * anomType.vals.length)];
        rawNodes.push({ val: anomVal, type: anomType.name, isAnom: true });

        rawNodes.sort(() => Math.random() - 0.5);

        nodes = rawNodes.map((n, idx) => ({
            ...n,
            id: idx
        }));

        renderNodes();

        setTimeout(() => {
            startShufflingPhase();
        }, 2500);
    }

    function renderNodes() {
        const container = document.getElementById('grid-container');
        container.innerHTML = '';
        
        nodes.forEach((node, index) => {
            const el = document.createElement('div');
            el.className = 'node-box';
            el.onclick = () => handleNodeClick(index);

            el.innerHTML = `
                <div class="node-val">${node.val}</div>
            `;
            container.appendChild(el);
        });
    }

    async function startShufflingPhase() {
        gameState = 'shuffling';
        document.getElementById('terminal-msg').innerText = "Matriks 4x4 mengacak posisi node...";

        let totalSwaps = 6 + (level * 2);
        let currentSwap = 0;
        let speed = Math.max(180, 320 - (level * 20));

        shuffleInterval = setInterval(() => {
            let idx1 = Math.floor(Math.random() * totalNodes);
            let idx2;
            do {
                idx2 = Math.floor(Math.random() * totalNodes);
            } while(idx1 === idx2);

            let temp = nodes[idx1];
            nodes[idx1] = nodes[idx2];
            nodes[idx2] = temp;

            renderNodes();
            currentSwap++;

            if (currentSwap >= totalSwaps) {
                clearInterval(shuffleInterval);
                startGuessingPhase();
            }
        }, speed);
    }

    function startGuessingPhase() {
        gameState = 'guessing';
        document.getElementById('terminal-msg').innerHTML = `<span style="color: #4ade80;">Pilih node yang sesuai dengan target!</span>`;
        
        traceLeft = 100;
        let maxTime = Math.max(4000, 10000 - (level * 400));
        let intervalTime = 50;
        let decrement = (intervalTime / maxTime) * 100;

        const bar = document.getElementById('trace-bar');
        bar.style.background = "#4ade80";

        clearInterval(traceTimer);
        traceTimer = setInterval(() => {
            traceLeft -= decrement;
            bar.style.width = traceLeft + '%';
            
            if (traceLeft < 40) bar.style.background = "#eab308";
            if (traceLeft < 20) bar.style.background = "#ef4444";

            if (traceLeft <= 0) {
                clearInterval(traceTimer);
                handleFailure("Waktu habis! Sistem mendeteksi kegagalan pelacakan.");
            }
        }, intervalTime);
    }

    function handleNodeClick(index) {
        if (gameState !== 'guessing') return;
        clearInterval(traceTimer);
        gameState = 'result';

        renderNodes();
        const clickedNode = nodes[index];
        const msgEl = document.getElementById('terminal-msg');

        if (clickedNode.isAnom) {
            score += 300 * level;
            level += 1;
            msgEl.style.color = "#4ade80";
            msgEl.innerText = "BERHASIL MELACAK ANOMALI!";
            updateStats();
            setTimeout(initRound, 2000);
        } else {
            handleFailure(`SALAH! Itu adalah tipe ${clickedNode.type} (${clickedNode.val}).`);
        }
    }

    function handleFailure(reason) {
        clearInterval(traceTimer);
        lives -= 1;
        gameState = 'gameover';
        renderNodes();
        
        const msgEl = document.getElementById('terminal-msg');
        msgEl.style.color = "#ef4444";
        msgEl.innerText = reason;
        updateStats();

        if (lives <= 0) {
            document.getElementById('mission-text').innerHTML = `<span style="color: #ef4444; font-weight: bold;">SISTEM TERKUNCI PERMANEN (GAME OVER)</span>`;
            document.getElementById('main-btn').style.display = 'inline-block';
            document.getElementById('main-btn').innerText = "COBA LAGI";
            document.getElementById('main-btn').onclick = startHack;
        } else {
            setTimeout(initRound, 2500);
        }
    }

    function updateStats() {
        document.getElementById('score').innerText = score;
        document.getElementById('lives').innerText = lives;
        document.getElementById('level').innerText = level;
    }
</script>
</body>
</html>
"""

components.html(game_html, height=580)
