import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Orange Protocol: Matrix Decrypt", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #09090b;
    color: #ffffff;
}
h1 {
    color: #f97316 !important;
    font-family: 'Courier New', monospace;
    text-align: center;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;900&family=Inter:wght@400;500;600;700&display=swap');

    /* Menyamakan font, warna, dan gaya sidebar persis seperti halaman utama */
     [data-testid="stSidebar"] {
        background-color: #f0e8d5 !important;
        border-right: 2px solid rgba(181, 142, 75, 0.4);
    }
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
        color: #1e1b18 !important;
        font-weight: 500;
    }

    /* Judul Utama dengan Grafis Modern Gradient */
    .main-title {
        font-family: 'Outfit', sans-serif;
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #5c4033 0%, #b58e4b 50%, #3d2817 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 4px 20px rgba(181, 142, 75, 0.25);
        margin-bottom: 0px;
    }

    .sub-title {
        font-family: 'Outfit', sans-serif;
        text-align: center;
        font-size: 1.4rem;
        color: #705335;
        letter-spacing: 4px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



st.title("MATH MATRIX: EQUATION CHAIN")
st.markdown("<p style='text-align: center; color: #fdba74;'>Pilih urutan angka dan operator dari matriks 4x4 untuk merakit persamaan yang hasilnya pas dengan Angka Target!</p>", unsafe_allow_html=True)

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        background-color: #09090b;
        color: #ffffff;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 0;
        padding: 5px;
        overflow-x: hidden;
    }
    .stats-panel {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 8px;
    }
    .stat-box {
        background: #18181b;
        border: 1px solid #f97316;
        padding: 6px 14px;
        border-radius: 8px;
        color: #f97316;
        font-size: 12px;
        font-weight: bold;
        box-shadow: 0 0 10px rgba(249, 115, 22, 0.2);
    }
    .timer-container {
        width: 100%;
        max-width: 480px;
        background: #18181b;
        height: 8px;
        border-radius: 4px;
        margin: 0 auto 8px auto;
        overflow: hidden;
        border: 1px solid #f97316;
    }
    .timer-bar {
        width: 100%;
        height: 100%;
        background: #f97316;
        transition: width 0.1s linear;
    }
    .mission-box {
        background: #18181b;
        border: 2px dashed #f97316;
        padding: 8px;
        border-radius: 8px;
        margin: 0 auto 8px auto;
        max-width: 480px;
        font-size: 13px;
        color: #fdba74;
    }
    .target-highlight {
        color: #ffffff;
        background: #c2410c;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 15px;
    }
    .expression-screen {
        background: #09090b;
        border: 2px solid #f97316;
        padding: 8px;
        border-radius: 6px;
        margin: 0 auto 8px auto;
        max-width: 480px;
        font-size: 16px;
        font-weight: bold;
        color: #4ade80;
        min-height: 22px;
        letter-spacing: 2px;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
        margin: 8px auto;
        width: 100%;
        max-width: 480px;
    }
    .node-box {
        background: #18181b;
        border: 2px solid #f97316;
        border-radius: 8px;
        height: 65px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: transform 0.2s ease, background-color 0.2s, border-color 0.2s;
        box-shadow: 0 0 8px rgba(249, 115, 22, 0.15);
    }
    .node-box.selected {
        background: #c2410c;
        border-color: #ffffff;
    }
    .node-box:hover {
        background: #27272a;
        border-color: #fb923c;
        transform: scale(1.03);
    }
    .node-val {
        font-size: 18px;
        font-weight: bold;
        color: #ffffff;
    }
    .terminal-msg {
        margin-top: 8px;
        font-size: 12px;
        font-weight: bold;
        height: 20px;
        color: #fdba74;
    }
    .action-btn {
        background-color: #f97316;
        color: #09090b;
        border: none;
        padding: 8px 18px;
        font-size: 13px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 6px;
        font-family: 'Courier New', monospace;
        transition: background 0.2s, transform 0.1s;
        box-shadow: 0 0 12px rgba(249, 115, 22, 0.4);
    }
    .action-btn:hover {
        background-color: #fb923c;
        transform: translateY(-2px);
    }
    .btn-group {
        display: flex;
        justify-content: center;
        gap: 8px;
    }
</style>
</head>
<body>

<div class="stats-panel">
    <div class="stat-box">SKOR: <span id="score">0</span></div>
    <div class="stat-box">NYAWA: <span id="lives">3</span></div>
    <div class="stat-box">LEVEL: <span id="level">1</span></div>
</div>

<div class="timer-container">
    <div class="timer-bar" id="timer-bar"></div>
</div>

<div class="mission-box" id="mission-text">
    TARGET ANGKA: <span class="target-highlight" id="target-display">0</span>
</div>

<div class="expression-screen" id="expr-display">Pilih ubin untuk merakit rumus...</div>

<div class="grid-container" id="grid-container"></div>

<div class="btn-group">
    <button class="action-btn" style="background-color: #27272a; color: #ffffff;" onclick="resetSelection()">RESET</button>
    <button class="action-btn" onclick="submitEquation()">EKSEKUSI</button>
</div>

<div class="terminal-msg" id="terminal-msg"></div>
<button class="action-btn" id="main-btn" onclick="startMathGame()" style="display:block; margin: 10px auto;">MULAI TANTANGAN</button>

<script>
    let score = 0;
    let lives = 3;
    let level = 1;
    let gridTiles = [];
    let targetNum = 0;
    let currentExpression = [];
    let gameActive = false;
    let timerInterval = null;
    let timeLeft = 100;

    const operators = ['+', '-', '*'];

    function startMathGame() {
        score = 0;
        lives = 3;
        level = 1;
        document.getElementById('main-btn').style.display = 'none';
        updateStats();
        initRound();
    }

    function initRound() {
        gameActive = true;
        currentExpression = [];
        document.getElementById('terminal-msg').innerText = "";
        document.getElementById('expr-display').innerText = "Pilih ubin untuk merakit rumus...";
        
        document.getElementById('mission-text').innerHTML = `TARGET ANGKA: <span class="target-highlight" id="target-display">0</span>`;

        let n1, n2, n3, op1, op2, valid = false;

        while (!valid) {
            n1 = Math.floor(Math.random() * 8) + 2;
            n2 = Math.floor(Math.random() * 8) + 2;
            n3 = Math.floor(Math.random() * 5) + 1;
            op1 = operators[Math.floor(Math.random() * operators.length)];
            op2 = operators[Math.floor(Math.random() * operators.length)];

            try {
                targetNum = eval(`${n1} ${op1} ${n2} ${op2} ${n3}`);
                if (Number.isInteger(targetNum) && targetNum >= 1 && targetNum <= 80) {
                    valid = true;
                }
            } catch (e) {
                valid = false;
            }
        }

        document.getElementById('target-display').innerText = targetNum;

        let tileValues = [n1.toString(), op1, n2.toString(), op2, n3.toString()];

        while(tileValues.length < 16) {
            if (Math.random() < 0.35) {
                tileValues.push(operators[Math.floor(Math.random() * operators.length)]);
            } else {
                tileValues.push((Math.floor(Math.random() * 9) + 1).toString());
            }
        }

        tileValues.sort(() => Math.random() - 0.5);

        gridTiles = tileValues.map((val, idx) => ({
            val: val,
            selected: false,
            id: idx
        }));

        renderGrid();
        startTimer();
    }

    function renderGrid() {
        const container = document.getElementById('grid-container');
        container.innerHTML = '';
        
        gridTiles.forEach((tile, index) => {
            const el = document.createElement('div');
            el.className = 'node-box' + (tile.selected ? ' selected' : '');
            el.onclick = () => handleTileClick(index);

            el.innerHTML = `<div class="node-val">${tile.val}</div>`;
            container.appendChild(el);
        });
    }

    function handleTileClick(index) {
        if (!gameActive) return;
        let tile = gridTiles[index];

        if (!tile.selected) {
            tile.selected = true;
            currentExpression.push({val: tile.val, index: index});
        } else {
            tile.selected = false;
            currentExpression = currentExpression.filter(item => item.index !== index);
        }

        updateExprDisplay();
        renderGrid();
    }

    function updateExprDisplay() {
        let text = currentExpression.map(item => item.val).join(' ');
        document.getElementById('expr-display').innerText = text || "Pilih ubin untuk merakit rumus...";
    }

    function resetSelection() {
        if (!gameActive) return;
        gridTiles.forEach(t => t.selected = false);
        currentExpression = [];
        updateExprDisplay();
        renderGrid();
    }

    function submitEquation() {
        if (!gameActive || currentExpression.length === 0) return;
        clearInterval(timerInterval);
        gameActive = false;

        let exprString = currentExpression.map(item => item.val).join(' ');

        try {
            let result = eval(exprString);
            const msgEl = document.getElementById('terminal-msg');

            if (result === targetNum) {
                score += 300 * level;
                level += 1;
                msgEl.style.color = "#4ade80";
                msgEl.innerText = `BERHASIL! ${exprString} = ${result}`;
                updateStats();
                setTimeout(initRound, 2000);
            } else {
                handleFailure(`SALAH! ${exprString} = ${result} (Target: ${targetNum})`);
            }
        } catch (e) {
            handleFailure("FORMAT RUMUS SALAH!");
        }
    }

    function handleFailure(reason) {
        clearInterval(timerInterval);
        lives -= 1;
        gameActive = false;
        
        const msgEl = document.getElementById('terminal-msg');
        msgEl.style.color = "#dc2626";
        msgEl.innerText = reason;
        updateStats();

        if (lives <= 0) {
            document.getElementById('mission-text').innerHTML = `<span style="color: #dc2626; font-weight: bold;">SYSTEM LOCKED: GAME OVER</span>`;
            let mainBtn = document.getElementById('main-btn');
            mainBtn.style.display = 'block';
            mainBtn.innerText = "COBA LAGI";
            mainBtn.onclick = startMathGame;
        } else {
            setTimeout(initRound, 2500);
        }
    }

    function startTimer() {
        timeLeft = 100;
        let maxTime = Math.max(6000, 16000 - (level * 600));
        let intervalTime = 50;
        let decrement = (intervalTime / maxTime) * 100;

        const bar = document.getElementById('timer-bar');
        bar.style.background = "#f97316";

        clearInterval(timerInterval);
        timerInterval = setInterval(() => {
            if (!gameActive) return;
            timeLeft -= decrement;
            bar.style.width = timeLeft + '%';
            
            if (timeLeft < 40) bar.style.background = "#ea580c";
            if (timeLeft < 20) bar.style.background = "#dc2626";

            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                gameActive = false;
                lives -= 1;
                document.getElementById('terminal-msg').style.color = "#dc2626";
                document.getElementById('terminal-msg').innerText = "WAKTU HABIS!";
                updateStats();

                if (lives <= 0) {
                    document.getElementById('mission-text').innerHTML = `<span style="color: #dc2626; font-weight: bold;">SYSTEM LOCKED: GAME OVER</span>`;
                    let mainBtn = document.getElementById('main-btn');
                    mainBtn.style.display = 'block';
                    mainBtn.innerText = "COBA LAGI";
                    mainBtn.onclick = startMathGame;
                } else {
                    setTimeout(initRound, 2500);
                }
            }
        }, intervalTime);
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

components.html(game_html, height=640)
