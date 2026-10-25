"""Menyusun HTML adegan kolam dari template + data simulasi (JSON)."""
import json
from pathlib import Path

_TEMPLATE = Path(__file__).parent / "assets" / "scene.html"


def build_html(payload: dict) -> str:
    html = _TEMPLATE.read_text(encoding="utf-8")
    return html.replace("/*__DATA__*/null", json.dumps(payload), 1)
