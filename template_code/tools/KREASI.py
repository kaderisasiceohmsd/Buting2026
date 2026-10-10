import streamlit as st
import random
import time
from collections import deque
import heapq

# ============================================================
#            KREASI — MINI GAMES & AI SHOWCASE 🎮🤖
# ============================================================

# ===== CSS Styling =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

    .game-header { text-align: center; padding: 1.5rem 1rem 0.5rem 1rem; }
    .game-title {
        font-family: 'Poppins', sans-serif; font-size: 2.8em; font-weight: 900;
        background: linear-gradient(135deg, #ffd740, #ffab40, #ff6e40);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; letter-spacing: 2px; margin-bottom: 0;
    }
    .game-subtitle {
        font-family: 'Poppins', sans-serif; color: #90a4ae; font-size: 1em;
        font-weight: 300; letter-spacing: 1px; margin-top: 0.3rem;
    }
    .fancy-divider {
        height: 2px; background: linear-gradient(90deg, transparent, #ffd740, #ffab40, transparent);
        margin: 1.5rem auto; max-width: 400px; border: none;
    }
    .score-box {
        background: linear-gradient(135deg, rgba(255,215,64,0.08), rgba(255,171,64,0.08));
        border: 1px solid rgba(255,215,64,0.25); border-radius: 14px;
        padding: 1rem 1.2rem; text-align: center; margin: 0.8rem 0;
    }
    .score-number { font-family: 'Poppins', sans-serif; font-size: 2.2em; font-weight: 800; color: #ffd740; }
    .score-label { color: #90a4ae; font-size: 0.82em; font-weight: 400; }
    
    /* Tic Tac Toe Grid */
    .ttt-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 300px; margin: 0 auto; }
    
    /* Maze Grid */
    .maze-row { display: flex; justify-content: center; }
    .maze-cell {
        width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;
        margin: 2px; border-radius: 6px; font-size: 1.5em; background: rgba(255,255,255,0.05);
    }
    .cell-wall { background: #5d4037; }
    .cell-path { background: rgba(255, 215, 64, 0.3); }
    .cell-explored { background: rgba(76, 175, 80, 0.2); }
</style>
""", unsafe_allow_html=True)

# ===== Data Anggota (Untuk Game Tebak NIM) =====
anggota = [
    {"nama": "Bintang Mahardika", "sebagai": "Palu", "nim": "125450106"},
    {"nama": "Sayyidina Najwa Syahra", "sebagai": "Bulu", "nim": "125450002"},
    {"nama": "Muhammad Rafli Raditya", "sebagai": "Anggota", "nim": "125450095"},
    {"nama": "M Abyan Alghaniyyu", "sebagai": "Anggota", "nim": "125450104"},
    {"nama": "Rahmad Bayu Ridho", "sebagai": "Anggota", "nim": "125450093"},
    {"nama": "Mojes Wijaya", "sebagai": "Anggota", "nim": "125450094"},
    {"nama": "Iva Aulia Sofia", "sebagai": "Anggota", "nim": "125450062"},
    {"nama": "Astrit Aisyah Rahmi", "sebagai": "Anggota", "nim": "125450036"},
    {"nama": "Septi Widia Arin", "sebagai": "Anggota", "nim": "12545005"},
    {"nama": "Fildzah Cahya Kamila", "sebagai": "Anggota", "nim": "125450040"},
    {"nama": "Lintar Abhinaya Putra Zulmi", "sebagai": "Anggota", "nim": "125450064"},
    {"nama": "Ahda Nabiwa", "sebagai": "Anggota", "nim": "125450069"},
    {"nama": "Bening Arianti", "sebagai": "Anggota", "nim": "154500068"},
]


# ============================================================
#               HEADER & TABS
# ============================================================
st.markdown("""
<div class='game-header'>
    <div class='game-title'>🎮 JORDAN ARCADE</div>
    <div class='game-subtitle'>Game seru & Eksperimen AI Search (Minimax, BFS, A*)</div>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

tab_nim, tab_ttt, tab_maze = st.tabs(["🔢 Tebak NIM", "⚔️ Tic-Tac-Toe AI", "🗺️ AI Pathfinding"])


# ============================================================
#                 TAB 1: TEBAK NIM
# ============================================================
with tab_nim:
    st.markdown("### 🔢 Uji Hafalan NIM")
    st.info("Bermain 5 ronde tanpa pengulangan. Tebak pemilik NIM dari teman-teman Jordan!")
    
    TOTAL_ROUNDS = 5
    if "nim_members" not in st.session_state:
        st.session_state.nim_members = random.sample(anggota, TOTAL_ROUNDS)
        st.session_state.nim_round = 0
        st.session_state.nim_score = 0
        st.session_state.nim_answered = False
        st.session_state.nim_last_correct = False
        st.session_state.nim_options = []
        for m in st.session_state.nim_members:
            opts = random.sample([a for a in anggota if a["nama"] != m["nama"]], 3) + [m]
            random.shuffle(opts)
            st.session_state.nim_options.append(opts)

    if st.session_state.nim_round < TOTAL_ROUNDS:
        rd = st.session_state.nim_round
        current = st.session_state.nim_members[rd]
        
        col1, col2 = st.columns(2)
        with col1: st.metric("Skor Sementara", f"{st.session_state.nim_score} / {TOTAL_ROUNDS}")
        with col2: st.metric("Ronde", f"{rd + 1} dari {TOTAL_ROUNDS}")
        
        st.markdown(f"<h2 style='text-align: center; color: #ffd740; margin: 1rem 0;'>NIM: {current['nim']}</h2>", unsafe_allow_html=True)
        
        if not st.session_state.nim_answered:
            with st.form(f"nim_form_{rd}"):
                choice = st.radio("Siapa pemilik NIM ini?", [m["nama"] for m in st.session_state.nim_options[rd]])
                if st.form_submit_button("Jawab"):
                    st.session_state.nim_answered = True
                    st.session_state.nim_last_correct = (choice == current["nama"])
                    if st.session_state.nim_last_correct: st.session_state.nim_score += 1
                    st.rerun()
        else:
            if st.session_state.nim_last_correct:
                st.success(f"✅ Benar! Itu NIM dari {current['nama']}.")
            else:
                st.error(f"❌ Salah! Jawaban yang benar adalah {current['nama']}.")
            
            if st.button("Lanjut ➡️"):
                st.session_state.nim_round += 1
                st.session_state.nim_answered = False
                st.rerun()
    else:
        st.markdown(f"<h2 style='text-align:center;'>Skor Akhir: {st.session_state.nim_score} / {TOTAL_ROUNDS}</h2>", unsafe_allow_html=True)
        if st.button("🔄 Main Lagi"):
            for key in ["nim_members", "nim_round", "nim_score", "nim_answered", "nim_last_correct", "nim_options"]:
                del st.session_state[key]
            st.rerun()


# ============================================================
#          TAB 2: TIC-TAC-TOE vs MINIMAX AI
# ============================================================
with tab_ttt:
    st.markdown("### ⚔️ Tic-Tac-Toe vs Minimax AI")
    st.info("**Adversarial Search:** AI menggunakan algoritma Minimax untuk memprediksi semua kemungkinan langkah. AI ini **mustahil dikalahkan**. Mampukah kamu menahan seri?")

    # -- AI Logic --
    def check_winner(board, player):
        win_cond = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(board[i] == board[j] == board[k] == player for i,j,k in win_cond)

    def is_draw(board):
        return ' ' not in board

    def minimax(board, depth, is_maximizing):
        if check_winner(board, 'O'): return 10 - depth  # O is AI
        if check_winner(board, 'X'): return depth - 10  # X is User
        if is_draw(board): return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def best_move(board):
        best_score = -float('inf')
        move = 0
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, 0, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return move

    # -- Game State --
    if "ttt_board" not in st.session_state:
        st.session_state.ttt_board = [' '] * 9
        st.session_state.ttt_winner = None

    board = st.session_state.ttt_board

    # Check state before render
    if not st.session_state.ttt_winner:
        if check_winner(board, 'X'): st.session_state.ttt_winner = 'X (Kamu Menang!)'
        elif check_winner(board, 'O'): st.session_state.ttt_winner = 'O (Jordan AI Menang!)'
        elif is_draw(board): st.session_state.ttt_winner = 'Seri'

    # Render Board
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        for i in range(3):
            c1, c2, c3 = st.columns(3)
            for j, col in enumerate([c1, c2, c3]):
                idx = i * 3 + j
                label = board[idx] if board[idx] != ' ' else '‎'
                with col:
                    if st.button(label, key=f"ttt_{idx}", use_container_width=True, disabled=(board[idx] != ' ' or st.session_state.ttt_winner is not None)):
                        st.session_state.ttt_board[idx] = 'X'
                        # AI Turn
                        if not check_winner(st.session_state.ttt_board, 'X') and not is_draw(st.session_state.ttt_board):
                            ai_idx = best_move(st.session_state.ttt_board)
                            st.session_state.ttt_board[ai_idx] = 'O'
                        st.rerun()

    if st.session_state.ttt_winner:
        st.success(f"**Hasil:** {st.session_state.ttt_winner}")
        if st.button("🔄 Main Lagi", key="ttt_reset"):
            st.session_state.ttt_board = [' '] * 9
            st.session_state.ttt_winner = None
            st.rerun()


# ============================================================
#          TAB 3: MAZE PATHFINDING (BFS vs A*)
# ============================================================
with tab_maze:
    st.markdown("### 🗺️ AI Pathfinding (Blind vs Heuristic)")
    st.info("**Blind Search (BFS)** mengecek semua arah secara buta, sedangkan **Heuristic Search (A*)** menggunakan insting (jarak manhattan) untuk menebak jalan tercepat ke tujuan.")

    GRID_SIZE = 8
    START = (0, 0)
    GOAL = (7, 7)

    if "maze_walls" not in st.session_state:
        # Generate random walls
        walls = set()
        for _ in range(15):
            r, c = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if (r, c) != START and (r, c) != GOAL:
                walls.add((r, c))
        st.session_state.maze_walls = walls
        st.session_state.maze_path = []
        st.session_state.maze_explored = []
        st.session_state.maze_algo = None
        st.session_state.maze_cost = 0

    walls = st.session_state.maze_walls

    def get_neighbors(r, c):
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE and (nr, nc) not in walls:
                yield nr, nc

    def run_bfs():
        queue = deque([(START, [START])])
        visited = {START}
        explored = []
        while queue:
            curr, path = queue.popleft()
            if curr != START and curr != GOAL: explored.append(curr)
            if curr == GOAL: return path, explored
            
            for nxt in get_neighbors(*curr):
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, path + [nxt]))
        return [], explored

    def run_astar():
        # Heuristic: Manhattan distance
        def h(pos): return abs(pos[0] - GOAL[0]) + abs(pos[1] - GOAL[1])
        
        # Priority Queue: (f_score, g_score, current_node, path)
        pq = [(h(START), 0, START, [START])]
        visited = set()
        explored = []
        
        while pq:
            f, g, curr, path = heapq.heappop(pq)
            if curr in visited: continue
            visited.add(curr)
            
            if curr != START and curr != GOAL: explored.append(curr)
            if curr == GOAL: return path, explored
            
            for nxt in get_neighbors(*curr):
                if nxt not in visited:
                    heapq.heappush(pq, (g + 1 + h(nxt), g + 1, nxt, path + [nxt]))
        return [], explored

    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("🔍 Jalankan BFS (Blind)"):
            path, explored = run_bfs()
            st.session_state.maze_algo = "BFS"
            st.session_state.maze_path = path
            st.session_state.maze_explored = explored
            st.session_state.maze_cost = len(explored)
    with col_btn2:
        if st.button("🎯 Jalankan A* (Heuristic)"):
            path, explored = run_astar()
            st.session_state.maze_algo = "A*"
            st.session_state.maze_path = path
            st.session_state.maze_explored = explored
            st.session_state.maze_cost = len(explored)
    with col_btn3:
        if st.button("🎲 Acak Map"):
            del st.session_state.maze_walls
            st.rerun()

    # --- Metrics ---
    if st.session_state.maze_algo:
        if not st.session_state.maze_path:
            st.warning("Jalan buntu! Tidak ada rute yang ditemukan.")
        else:
            st.success(f"Algoritma **{st.session_state.maze_algo}** mengeksplorasi **{st.session_state.maze_cost} kotak** sebelum menemukan jalan keluar.")

    # --- Render Grid ---
    st.markdown("<div style='margin-top: 1rem;'>", unsafe_allow_html=True)
    for r in range(GRID_SIZE):
        row_html = "<div class='maze-row'>"
        for c in range(GRID_SIZE):
            pos = (r, c)
            css_class = ""
            icon = ""
            
            if pos == START:
                icon = "🏃"
            elif pos == GOAL:
                icon = "🚩"
            elif pos in walls:
                css_class = "cell-wall"
            elif pos in st.session_state.maze_path:
                css_class = "cell-path"
                icon = "🔵"
            elif pos in st.session_state.maze_explored:
                css_class = "cell-explored"
                icon = "👣"
            
            row_html += f"<div class='maze-cell {css_class}'>{icon}</div>"
        row_html += "</div>"
        st.markdown(row_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #546e7a; font-size: 0.8em;'>Made with ❤️ by Kelompok 01 Jordan</div>", unsafe_allow_html=True)
