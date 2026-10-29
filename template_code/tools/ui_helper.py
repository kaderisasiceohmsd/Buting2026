"""
ui_helper.py
Design System – Buku Kating Digital TENSOR 2026
Dark Violet Theme · Clean, Minimal & Elegant
"""

import html
import re
from io import BytesIO

import requests
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageDraw, ImageOps

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────────────────────────────────────

_GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

/* ── Global Font (Kecuali Material Icons agar ikon sidebar tidak rusak) ── */
html, body, [class*="css"], .stMarkdown p, .stMarkdown div, h1, h2, h3, h4, label {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ── Lindungi Material Symbols & Icons agar tidak ter-override ── */
[data-testid="stIconMaterial"], 
.material-symbols-rounded, 
.material-icons, 
[class*="material-symbols"] {
    font-family: 'Material Symbols Rounded', 'Material Symbols Outlined', 'Material Icons' !important;
    font-style: normal !important;
    font-weight: normal !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    display: inline-block !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
}

/* ── Custom Scrollbar Halus ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0c0a17; }
::-webkit-scrollbar-thumb { background: rgba(139,92,246,0.35); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: rgba(168,85,247,0.6); }

/* ── Typography & Header ── */
.g-title {
    background: linear-gradient(130deg, #ede9fe 10%, #c4b5fd 55%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    letter-spacing: -0.02em;
    text-align: center;
    margin: 0;
    line-height: 1.2;
}

.g-tag {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 14px;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 99px;
    font-size: 0.75rem;
    font-weight: 600;
    color: #c4b5fd;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* ── Card Kontainer Serbaguna ── */
.g-card {
    background: rgba(19, 15, 36, 0.95);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 20px;
    transition: border-color 0.25s ease;
}
.g-card:hover { border-color: rgba(139,92,246,0.45); }

/* ── Foto Kelompok Frame ── */
.photo-frame {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(139,92,246,0.25);
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    margin: 10px 0 16px 0;
}

/* ── Efek Kaca (Glassmorphism & Sheen Hover) ── */
.glass-box,
[class*="st-key-glass-card-"] {
    background: rgba(19, 15, 36, 0.75);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(168, 85, 247, 0.25);
    border-radius: 14px;
    padding: 16px;
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.glass-box:hover,
[class*="st-key-glass-card-"]:hover {
    background: rgba(28, 22, 54, 0.55);
    border-color: rgba(196, 181, 253, 0.6);
    box-shadow: 
        0 12px 32px 0 rgba(139, 92, 246, 0.3),
        inset 0 0 16px 0 rgba(255, 255, 255, 0.1);
    transform: translateY(-4px) scale(1.008);
}

.glass-box::before,
[class*="st-key-glass-card-"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: -120%;
    width: 60%;
    height: 100%;
    background: linear-gradient(
        90deg, 
        transparent, 
        rgba(255, 255, 255, 0.08), 
        rgba(196, 181, 253, 0.22), 
        transparent
    );
    transform: skewX(-25deg);
    pointer-events: none;
    z-index: 2;
}

.glass-box:hover::before,
[class*="st-key-glass-card-"]:hover::before {
    left: 160%;
    transition: all 0.75s ease-in-out;
}

/* ── Efek Kaca Khusus Foto Kelompok & Anggota ── */
.glass-photo-wrap,
[class*="st-key-glass-photo-"] {
    position: relative;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(139, 92, 246, 0.25);
    transition: all 0.35s ease;
}

.glass-photo-wrap:hover,
[class*="st-key-glass-photo-"]:hover {
    border-color: rgba(196, 181, 253, 0.65);
    box-shadow: 
        0 14px 36px 0 rgba(139, 92, 246, 0.35),
        inset 0 0 20px 0 rgba(255, 255, 255, 0.12);
    transform: translateY(-4px) scale(1.01);
}

.glass-photo-wrap img,
[class*="st-key-glass-photo-"] img {
    transition: transform 0.4s ease;
}

.glass-photo-wrap:hover img,
[class*="st-key-glass-photo-"]:hover img {
    transform: scale(1.02);
}

.glass-photo-wrap::before,
[class*="st-key-glass-photo-"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: -120%;
    width: 50%;
    height: 100%;
    background: linear-gradient(
        90deg, 
        transparent, 
        rgba(255, 255, 255, 0.15), 
        rgba(216, 180, 254, 0.3), 
        transparent
    );
    transform: skewX(-25deg);
    pointer-events: none;
    z-index: 3;
}

.glass-photo-wrap:hover::before,
[class*="st-key-glass-photo-"]:hover::before {
    left: 160%;
    transition: all 0.8s ease-in-out;
}


/* Streamlit container versions: let inner elements fill and clip properly */
[class*="st-key-glass-photo-"] .stImage img {
    border: none;
    border-radius: 0;
}
[class*="st-key-glass-card-"], [class*="st-key-glass-photo-"] {
    gap: 0;
}
[class*="st-key-glass-card-"][class*="st-key-glass-card-"] {
    margin-bottom: 24px;
}


/* ── Photo overlay: name + title always visible, details slide up on hover ── */
[class*="st-key-glass-photo-"] {
    --head-h: 78px;
}

[class*="st-key-glass-photo-"] .stElementContainer:has(.photo-overlay),
[class*="st-key-glass-photo-"] .element-container:has(.photo-overlay) {
    position: absolute;
    inset: 0;
    margin: 0;
    z-index: 4;
    pointer-events: none;
}

.photo-overlay {
    position: absolute;
    left: 0; right: 0; bottom: 0;
    padding: 40px 14px 12px;
    background:
        radial-gradient(120% 90% at 0% 100%, rgba(139, 92, 246, 0.22), transparent 65%),
        linear-gradient(to bottom,
            rgba(19, 15, 36, 0) 0,
            rgba(19, 15, 36, 0.78) 40px,
            rgba(16, 12, 32, 0.92) 100%);
    transform: translateY(calc(100% - var(--head-h)));
    transition: transform 0.5s cubic-bezier(0.22, 1, 0.36, 1);
}

.photo-overlay::before {
    content: '';
    position: absolute;
    inset: 0;
    z-index: -1;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    -webkit-mask-image: linear-gradient(to bottom, transparent 0, #000 40px);
    mask-image: linear-gradient(to bottom, transparent 0, #000 40px);
    pointer-events: none;
}

.po-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
}
.po-name {
    flex: 1;
    min-width: 0;
    font-size: 0.98rem;
    font-weight: 700;
    color: #ffffff;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-shadow: 0 1px 8px rgba(0, 0, 0, 0.6);
}
.photo-overlay .tm-role { margin: 0; flex-shrink: 0; font-size: 0.64rem; padding: 2px 8px; }
.po-nim { font-family: 'Courier New', Courier, monospace; letter-spacing: 0.04em; text-transform: none; }

.po-more {
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px solid rgba(167, 139, 250, 0.22);
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.po-more > * {
    opacity: 0;
    transform: translateY(12px);
    transition: opacity 0.35s ease, transform 0.45s cubic-bezier(0.22, 1, 0.36, 1);
}

.po-row { display: flex; align-items: center; gap: 10px; }
.po-ico {
    width: 28px; height: 28px;
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem;
    border-radius: 8px;
    background: rgba(139, 92, 246, 0.16);
    border: 1px solid rgba(167, 139, 250, 0.28);
}
.po-label {
    display: block;
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 1px;
}
.po-val { font-size: 0.82rem; font-weight: 500; color: #f1f5f9; line-height: 1.3; }
.po-mono { font-family: 'Courier New', Courier, monospace; letter-spacing: 0.04em; }

.po-quote {
    padding: 7px 11px;
    border-left: 3px solid #a855f7;
    border-radius: 0 10px 10px 0;
    background: linear-gradient(90deg, rgba(168, 85, 247, 0.16), rgba(168, 85, 247, 0.03));
    font-size: 0.82rem;
    font-style: italic;
    color: #f3e8ff;
    line-height: 1.4;
}
.po-quote .po-label { font-style: normal; color: #d8b4fe; }

[class*="st-key-glass-photo-"]:hover .photo-overlay { transform: translateY(0); }
[class*="st-key-glass-photo-"]:hover .po-more > * { opacity: 1; transform: translateY(0); }
[class*="st-key-glass-photo-"]:hover .po-more > :nth-child(1) { transition-delay: 0.12s; }
[class*="st-key-glass-photo-"]:hover .po-more > :nth-child(2) { transition-delay: 0.20s; }
[class*="st-key-glass-photo-"]:hover .po-more > :nth-child(3) { transition-delay: 0.28s; }

/* ── Compact cards ── */
[class*="st-key-glass-photo-"] .stImage img,
[class*="st-key-glass-photo-"] [data-testid="stImage"] img {
    aspect-ratio: 4 / 5 !important;
    height: auto !important;
    object-fit: cover !important;
    object-position: center 25% !important;
}
[class*="st-key-glass-card-"] { padding: 12px; }

/* Photo inside a glass card: no second layer of effects */
[class*="st-key-glass-card-"] [class*="st-key-glass-photo-"] {
    border-color: rgba(139, 92, 246, 0.15);
    transition: none;
}
[class*="st-key-glass-card-"] [class*="st-key-glass-photo-"]:hover {
    transform: none;
    box-shadow: none;
    border-color: rgba(139, 92, 246, 0.15);
}
[class*="st-key-glass-card-"] [class*="st-key-glass-photo-"]::before { display: none; }
[class*="st-key-glass-card-"] [class*="st-key-glass-photo-"]:hover img { transform: none; }

/* soften card hover */
[class*="st-key-glass-card-"]:hover { transform: translateY(-2px); }

/* ── Kating card: solid, info always visible (no glass, no hover) ── */
[class*="st-key-kating-card-"] {
    background: rgba(19, 15, 36, 0.95);
    border: 1px solid rgba(139, 92, 246, 0.22);
    border-radius: 14px;
    padding: 12px;
    margin-bottom: 20px;
    gap: 0;
}
[class*="st-key-kating-card-"] .stImage img,
[class*="st-key-kating-card-"] [data-testid="stImage"] img {
    aspect-ratio: 4 / 5;
    height: auto;
    object-fit: cover;
    object-position: center 25%;
    border: none;
    border-radius: 10px;
}
.kc-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    margin-top: 12px;
}
.kc-name {
    min-width: 0;
    font-size: 1.05rem;
    font-weight: 700;
    color: #f8fafc;
    line-height: 1.3;
}
.kc-nim {
    flex-shrink: 0;
    padding: 3px 10px;
    border-radius: 99px;
    background: rgba(139, 92, 246, 0.15);
    border: 1px solid rgba(139, 92, 246, 0.35);
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.74rem;
    letter-spacing: 0.04em;
    color: #c4b5fd;
}
.kc-nim-label {
    margin-right: 7px;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 0.66rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    color: #a78bfa;
}
.kc-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px 16px;
    margin-top: 12px;
    padding-top: 12px;
    border-top: 1px solid rgba(139, 92, 246, 0.2);
}
.kc-cell { min-width: 0; }
.kc-cell.wide { grid-column: 1 / -1; }
.kc-label {
    display: block;
    font-size: 0.64rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 2px;
}
.kc-val {
    font-size: 0.88rem;
    color: #f1f5f9;
    line-height: 1.35;
    overflow-wrap: anywhere;
}

/* Fix: Streamlit pulls markdown up by -1rem, which made the last block overflow the card border */
[class*="st-key-kating-card-"] [data-testid="stElementContainer"],
[class*="st-key-kating-card-"] .element-container,
[class*="st-key-kating-card-"] [data-testid="stMarkdown"],
[class*="st-key-kating-card-"] [data-testid="stMarkdownContainer"] {
    margin-bottom: 0 !important;
}

/* Equal-height cards: every card in a row stretches to the tallest one */
[data-testid="stHorizontalBlock"]:has([class*="st-key-kating-card-"]) {
    align-items: stretch !important;
}
[data-testid="stHorizontalBlock"]:has([class*="st-key-kating-card-"]) > [data-testid="stColumn"],
[data-testid="stHorizontalBlock"]:has([class*="st-key-kating-card-"]) > [data-testid="column"] {
    display: flex;
    flex-direction: column;
}
[data-testid="stHorizontalBlock"]:has([class*="st-key-kating-card-"]) > [data-testid="stColumn"] > [data-testid="stVerticalBlock"],
[data-testid="stHorizontalBlock"]:has([class*="st-key-kating-card-"]) > [data-testid="column"] > [data-testid="stVerticalBlock"] {
    flex: 1 1 auto;
}
[data-testid="stVerticalBlock"] > [class*="st-key-kating-card-"],
[data-testid="stVerticalBlock"] > [data-testid="stLayoutWrapper"]:has(> [class*="st-key-kating-card-"]) {
    flex: 1 1 auto;
}
[data-testid="stLayoutWrapper"] > [class*="st-key-kating-card-"] {
    height: 100%;
}

/* ── Home page photos: glass + shimmer effect on the real photo wrapper ── */
[class*="st-key-shine-photo-"] {
    position: relative;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(139, 92, 246, 0.25);
    gap: 0;
    transition: all 0.35s ease;
}
[class*="st-key-shine-photo-"]:hover {
    border-color: rgba(196, 181, 253, 0.65);
    box-shadow:
        0 14px 36px 0 rgba(139, 92, 246, 0.35),
        inset 0 0 20px 0 rgba(255, 255, 255, 0.12);
    transform: translateY(-4px) scale(1.01);
}
[class*="st-key-shine-photo-"] .stImage img,
[class*="st-key-shine-photo-"] [data-testid="stImage"] img {
    border: none;
    border-radius: 0;
    transition: transform 0.4s ease;
}
[class*="st-key-shine-photo-"]:hover img { transform: scale(1.02); }
[class*="st-key-shine-photo-"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: -120%;
    width: 50%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.15),
        rgba(216, 180, 254, 0.3),
        transparent
    );
    transform: skewX(-25deg);
    pointer-events: none;
    z-index: 3;
}
[class*="st-key-shine-photo-"]:hover::before {
    left: 160%;
    transition: all 0.8s ease-in-out;
}

/* Less empty space above the page title */
.block-container,
[data-testid="stMainBlockContainer"] {
    padding-top: 3.5rem !important;
}

/* ── Flip cards (Home gallery): photo on the front, text on the back ── */
[class*="st-key-flip-card-"] {
    position: relative;
    gap: 0;
    transform: perspective(1100px) rotateY(0deg);
    transform-style: preserve-3d;
    -webkit-transform-style: preserve-3d;
    transition: transform 0.75s cubic-bezier(0.22, 1, 0.36, 1);
    will-change: transform;
}
/* hover is read on the column (which doesn't rotate), so the flip never flickers at the edges */
:is([data-testid="stColumn"], [data-testid="column"]):hover [class*="st-key-flip-card-"] {
    transform: perspective(1100px) rotateY(180deg);
}

/* both faces hide their reverse side */
[class*="st-key-flip-card-"] :is([data-testid="stElementContainer"], .element-container) {
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
}

/* front: the photo (sets the card size) */
[class*="st-key-flip-card-"] .stImage img,
[class*="st-key-flip-card-"] [data-testid="stImage"] img {
    aspect-ratio: 1 / 1;
    height: auto;
    width: 100%;
    object-fit: cover;
    object-position: center 30%;
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 14px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}
[class*="st-key-flip-card-"] button[title="View fullscreen"],
[class*="st-key-flip-card-"] [data-testid="stImageToolbar"],
[class*="st-key-flip-card-"] [data-testid="StyledFullScreenButton"] {
    display: none;
}

/* back: the text, laid over the same area and turned around */
[class*="st-key-flip-card-"] :is([data-testid="stElementContainer"], .element-container):has(.flip-back) {
    position: absolute;
    inset: 0;
    margin: 0 !important;
    transform: rotateY(180deg);
}
[class*="st-key-flip-card-"] :is([data-testid="stElementContainer"], .element-container):has(.flip-back) [data-testid="stMarkdown"],
[class*="st-key-flip-card-"] :is([data-testid="stElementContainer"], .element-container):has(.flip-back) [data-testid="stMarkdownContainer"] {
    height: 100%;
    margin: 0 !important;
}
.flip-back {
    height: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 18px 20px;
    border-radius: 14px;
    overflow: hidden;
    background:
        radial-gradient(120% 90% at 50% 0%, rgba(139, 92, 246, 0.28), transparent 70%),
        linear-gradient(160deg, rgba(28, 22, 54, 0.98), rgba(16, 12, 32, 0.98));
    border: 1px solid rgba(168, 85, 247, 0.4);
    box-shadow: 0 14px 36px rgba(139, 92, 246, 0.3);
}
.flip-emoji { font-size: 1.8rem; margin-bottom: 8px; }
.flip-title { font-size: 1.02rem; font-weight: 700; color: #f1f5f9; margin-bottom: 8px; line-height: 1.3; }
.flip-desc  { font-size: 0.82rem; line-height: 1.55; color: #cbd5e1; }

/* ── Jargon Banner Estetis ── */
.jargon-card {
    background: linear-gradient(135deg, rgba(28, 20, 54, 0.85) 0%, rgba(16, 12, 32, 0.95) 100%);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(168, 85, 247, 0.35);
    border-radius: 14px;
    padding: 24px 28px;
    text-align: center;
    margin: 18px 0 24px 0;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(139, 92, 246, 0.15);
}

.jargon-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -120%;
    width: 50%;
    height: 100%;
    background: linear-gradient(
        90deg, 
        transparent, 
        rgba(255, 255, 255, 0.1), 
        rgba(196, 181, 253, 0.25), 
        transparent
    );
    transform: skewX(-25deg);
    pointer-events: none;
}

.jargon-card:hover::before {
    left: 160%;
    transition: all 0.85s ease-in-out;
}

.jargon-text {
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.7;
    background: linear-gradient(130deg, #ffffff 0%, #e9d5ff 40%, #c4b5fd 75%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.01em;
    font-style: italic;
    margin-top: 6px;
}

/* ══════════════════════════════════════════════
   KATING VERTICAL CARD SYSTEM
   (Normal, Elegan, Susunan Rapi Sesuai Aturan)
══════════════════════════════════════════════ */

.stImage img {
    border-radius: 10px;
    border: 1px solid rgba(139,92,246,0.2);
    display: block;
    width: 100%;
}

.logo-wrap .stImage img, .logo-wrap img {
    border: none !important;
    border-radius: 0 !important;
    background: transparent !important;
    box-shadow: none !important;
}

/* Biodata Card di bawah foto */
.k-card {
    background: rgba(19, 15, 36, 0.95);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 10px;
    padding: 14px 16px 16px;
    margin-top: 6px;
    margin-bottom: 24px;
    transition: border-color 0.25s ease;
}
.k-card:hover { border-color: rgba(139,92,246,0.45); }

.k-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: #f8fafc;
    margin: 0 0 2px 0;
    line-height: 1.3;
}

.k-nim {
    font-size: 0.78rem;
    font-family: 'Courier New', Courier, monospace;
    color: #a78bfa;
    display: block;
    margin-bottom: 8px;
    letter-spacing: 0.03em;
}

.k-sep {
    height: 1px;
    background: linear-gradient(90deg,
        rgba(139,92,246,0.05) 0%,
        rgba(139,92,246,0.3) 50%,
        rgba(139,92,246,0.05) 100%);
    margin: 8px 0 10px;
}

.k-info {
    display: flex;
    gap: 6px;
    font-size: 0.83rem;
    color: #cbd5e1;
    margin-bottom: 5px;
    line-height: 1.45;
}
.k-info-label {
    min-width: 60px;
    font-weight: 600;
    color: #c4b5fd;
    flex-shrink: 0;
}
.k-info-val { color: #f1f5f9; }

.k-q {
    margin-top: 8px;
    padding: 8px 12px;
    border-radius: 0 8px 8px 0;
    font-size: 0.82rem;
    line-height: 1.55;
    font-style: italic;
    border-left: 2px solid;
}
.k-kesan {
    border-color: #818cf8;
    background: rgba(99,102,241,0.08);
    color: #e0e7ff;
}
.k-pesan {
    border-color: #a855f7;
    background: rgba(168,85,247,0.08);
    color: #f3e8ff;
}
.k-q-label {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    opacity: 0.75;
    display: block;
    margin-bottom: 3px;
    font-style: normal;
}

/* ══════════════════════════════════════════════
   ANGGOTA KELOMPOK (ABOUT US) VERTICAL CARDS
══════════════════════════════════════════════ */
.tm-card {
    background: rgba(19, 15, 36, 0.95);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 10px;
    padding: 14px 16px;
    margin-top: 6px;
    margin-bottom: 20px;
    transition: border-color 0.25s;
}
.tm-card:hover { border-color: rgba(139,92,246,0.45); }
.tm-name { font-size: 1.05rem; font-weight: 700; color: #ffffff; margin-bottom: 4px; }
.tm-role {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 99px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
}
.tm-lurah {
    background: rgba(234, 179, 8, 0.15);
    border: 1px solid rgba(234, 179, 8, 0.4);
    color: #fde047;
}
.tm-member {
    background: rgba(139, 92, 246, 0.15);
    border: 1px solid rgba(139, 92, 246, 0.35);
    color: #c4b5fd;
}
.tm-nim { font-size: 0.78rem; font-family: monospace; color: #a78bfa; display: block; margin-bottom: 8px; }

/* ── Input Box Search ── */
[data-testid="stTextInput"] input {
    background: rgba(19, 15, 36, 0.92) !important;
    border: 1px solid rgba(139,92,246,0.25) !important;
    border-radius: 10px !important;
    color: #f8fafc !important;
    padding: 8px 14px !important;
    transition: all 0.2s ease !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: rgba(168,85,247,0.6) !important;
    box-shadow: 0 0 0 3px rgba(168,85,247,0.15) !important;
}
</style>
"""

def inject_custom_css():
    st.markdown(_GLOBAL_CSS, unsafe_allow_html=True)


def extract_gdrive_id(url: str) -> str:
    if not url:
        return ""
    m = re.search(r"[?&]id=([a-zA-Z0-9_-]+)", url)
    if m:
        return m.group(1)
    m = re.search(r"/d/([a-zA-Z0-9_-]+)", url)
    if m:
        return m.group(1)
    return ""


def get_fallback_avatar(name: str = "KT", size=(360, 480)) -> Image.Image:
    """Buat avatar placeholder jika foto gagal dimuat."""
    img = Image.new("RGB", size, color=(19, 15, 36))
    draw = ImageDraw.Draw(img)
    w, h = size
    draw.ellipse([w // 4, h // 4, 3 * w // 4, 3 * h // 4], fill=(35, 27, 65))
    initials = "".join(p[0].upper() for p in name.replace("*", "").split()[:2] if p) or "KT"
    tx = w // 2 - len(initials) * 6
    ty = h // 2 - 10
    draw.text((tx, ty), initials, fill=(196, 181, 253))
    return img


@st.cache_data(show_spinner=False)
def load_image(url: str, fallback_name: str = "Kating", keep_ratio: bool = False) -> Image.Image:
    """Muat gambar dari Google Drive/URL dengan caching dan fallback aman.
    Jika keep_ratio=True, gambar tidak akan dipotong (cocok untuk logo)."""
    if not url or not isinstance(url, str):
        return get_fallback_avatar(fallback_name)

    file_id = extract_gdrive_id(url)
    target = f"https://drive.google.com/uc?export=view&id={file_id}" if file_id else url

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko)"
        )
    }
    try:
        r = requests.get(target, headers=headers, timeout=6)
        if r.status_code == 200 and len(r.content) > 512:
            img = Image.open(BytesIO(r.content))
            img = ImageOps.exif_transpose(img)
            if keep_ratio:
                return img
            # Untuk foto kating: 3:4 dengan Lanczos
            img = ImageOps.fit(
                img, (360, 480), method=Image.Resampling.LANCZOS, centering=(0.5, 0.4)
            )
            return img
    except Exception:
        pass
    return get_fallback_avatar(fallback_name)


def clean_text(text: str) -> str:
    return str(text).replace("**", "").strip() if text else ""


def get_menu_styles(columns: int = 0) -> dict:
    """Style option_menu bernuansa dark purple.
    columns > 0: susun item menjadi grid rata dengan `columns` item per baris
    (mis. 10 departemen -> 5 x 2)."""
    styles = {
        "container": {
            "padding": "4px 8px",
            "background-color": "rgba(19, 15, 36, 0.95)",
            "border-radius": "10px",
            "border": "1px solid rgba(139,92,246,0.25)",
            "margin-bottom": "20px",
        },
        "icon": {"color": "#c4b5fd", "font-size": "16px"},
        "nav-link": {
            "font-size": "14px",
            "font-weight": "500",
            "text-align": "center",
            "padding": "8px 14px",
            "margin": "2px",
            "border-radius": "8px",
            "color": "#cbd5e1",
            "--hover-color": "rgba(139,92,246,0.15)",
        },
        "nav-link-selected": {
            "background": "linear-gradient(135deg, #6d28d9 0%, #8b5cf6 100%)",
            "color": "#ffffff",
            "font-weight": "600",
            "box-shadow": "0 4px 14px rgba(139, 92, 246, 0.35)",
        },
    }
    if columns:
        gap = 4
        styles["container"].update({"padding": "6px", "margin-bottom": "14px"})
        styles["nav"] = {"flex-wrap": "wrap", "gap": f"{gap}px"}
        # tiap item = 1/columns lebar baris (dikurangi bagian gap), jadi semua tombol sama lebar
        share = gap * (columns - 1) / columns
        styles["nav-item"] = {"flex": f"0 0 calc({100 / columns:.4f}% - {share:.2f}px)"}
        styles["icon"] = {"color": "#c4b5fd", "font-size": "14px", "margin": "0"}
        styles["nav-link"].update(
            {
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "gap": "6px",
                "font-size": "13px",
                "padding": "9px 6px",
                "margin": "0",
                "white-space": "nowrap",
            }
        )
    return styles


def dept_menu(options: list, columns: int = 5, default_index: int = 0, key: str = "dept_menu") -> str:
    """Menu departemen berupa grid rapi (default 5 item per baris), nama item tidak diubah."""
    return option_menu(
        menu_title=None,
        options=options,
        icons=["people-fill"] * len(options),
        default_index=default_index,
        orientation="horizontal",
        styles=get_menu_styles(columns=columns),
        key=key,
    )


def render_kating_cards(
    gambar_urls: list,
    data_list: list,
    department_title: str = "Daftar Anggota",
):
    """
    Tampilkan profil kating dalam tata letak vertikal (2 kolom grid):
    Foto di atas, biodata lengkap normal & rapi di bawah.
    """
    inject_custom_css()
    total = len(data_list)

    # Header Bar + Search Filter
    col_t, col_s = st.columns([1, 1.6])
    with col_t:
        st.markdown(
            f"""
            <div style="padding-top: 4px;">
                <span class="g-tag">🏛 {department_title}</span>
                <div style="font-size: 0.8rem; color: #94a3b8; margin-top: 3px;">
                    {total} Kating Terdata
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_s:
        query = st.text_input(
            "",
            placeholder="🔍 Cari nama, NIM, asal, atau alamat...",
            label_visibility="collapsed",
            key=f"ks_{department_title.replace(' ', '_')}",
        )

    # Filter pencarian
    filtered = []
    for i, data in enumerate(data_list):
        url = gambar_urls[i] if i < len(gambar_urls) else ""
        if not query:
            filtered.append((data, url))
        else:
            q = query.strip().lower()
            hay = " ".join([
                str(data.get("nama", "")),
                str(data.get("nim", "")),
                str(data.get("asal", "")),
                str(data.get("alamat", "")),
                str(data.get("hobbi", "")),
            ]).lower()
            if q in hay:
                filtered.append((data, url))

    if not filtered:
        st.markdown(
            f"""
            <div style="text-align: center; padding: 40px 20px; background: rgba(19,15,36,0.6); border-radius: 12px; border: 1px dashed rgba(139,92,246,0.25); margin-top: 15px;">
                <div style="font-size: 2rem; margin-bottom: 8px;">🔍</div>
                <div style="color: #f1f5f9; font-weight: 600;">Tidak ada kating dengan kata kunci "{query}"</div>
                <div style="color: #94a3b8; font-size: 0.85rem; margin-top: 4px;">Coba gunakan nama panggilan, NIM, atau kota asal lainnya.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    if query:
        st.markdown(
            f'<div style="font-size: 0.82rem; color: #a78bfa; margin-bottom: 12px;">✦ Menampilkan {len(filtered)} dari {total} kating</div>',
            unsafe_allow_html=True,
        )

    # 2 kartu per baris, sedikit dipusatkan dengan kolom kosong di sisi
    slug = re.sub(r"[^a-z0-9]+", "-", department_title.lower()).strip("-")

    def _cell(label, val, wide=False):
        if not val or val == "-":
            return ""
        cls = "kc-cell wide" if wide else "kc-cell"
        return (
            f'<div class="{cls}"><span class="kc-label">{label}</span>'
            f'<div class="kc-val">{html.escape(val)}</div></div>'
        )

    def _quote(label, text, cls):
        text = clean_text(text)
        if not text or text == "-":
            return ""
        return (
            f'<div class="k-q {cls}"><span class="k-q-label">{label}:</span>'
            f'\u201c{html.escape(text)}\u201d</div>'
        )

    for row in range(0, len(filtered), 2):
        _pad_l, col_a, col_b, _pad_r = st.columns([0.5, 3, 3, 0.5], gap="medium")
        cols = [col_a, col_b]
        for ci in range(2):
            idx = row + ci
            if idx >= len(filtered):
                break
            data, url = filtered[idx]

            nama   = clean_text(data.get("nama", "Kakak Tingkat"))
            nim    = clean_text(data.get("nim", ""))
            umur   = clean_text(data.get("umur", ""))
            asal   = clean_text(data.get("asal", ""))
            alamat = clean_text(data.get("alamat", ""))
            hobbi  = clean_text(data.get("hobbi", ""))
            sosmed = clean_text(data.get("sosmed", ""))

            nim_badge = (
                f'<span class="kc-nim"><span class="kc-nim-label">NIM</span>{html.escape(nim)}</span>'
                if nim else ""
            )
            grid = (
                _cell("Umur", f"{umur} Tahun" if umur else "")
                + _cell("Asal", asal)
                + _cell("Hobbi", hobbi)
                + _cell("Sosmed", sosmed)
                + _cell("Alamat", alamat, wide=True)
            )
            grid_html = f'<div class="kc-grid">{grid}</div>' if grid else ""
            quotes = _quote("Kesan", data.get("kesan", ""), "k-kesan") + _quote(
                "Pesan", data.get("pesan", ""), "k-pesan"
            )

            # satu baris HTML tanpa indentasi/newline agar tidak dibaca sebagai code block
            card_html = (
                f'<div class="kc-head"><div class="kc-name">{html.escape(nama)}</div>{nim_badge}</div>'
                f"{grid_html}{quotes}"
            )

            with cols[ci]:
                with st.container(key=f"kating-card-{slug}-{idx}"):
                    img = load_image(url, fallback_name=nama)
                    st.image(img, use_container_width=True)
                    st.markdown(card_html, unsafe_allow_html=True)
