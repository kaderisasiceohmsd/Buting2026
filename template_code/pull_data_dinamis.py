"""
PULL DATA DINAMIS BUTING 2026
=============================
Cara pakai:
  python pull_data_dinamis.py rafli      → simpan Data/data_dinamis/rafli.json
  python pull_data_dinamis.py mojes      → simpan Data/data_dinamis/mojes.json
  python pull_data_dinamis.py all        → simpan JSON per orang sekaligus (13 file)
"""

import urllib.request
import json
import os
import sys
import ssl

# ==============================================================================
# GANTI URL INI DENGAN URL WEB APP DARI GOOGLE APPS SCRIPT SETELAH DI-DEPLOY!
# ==============================================================================
APPSCRIPT_URL = "https://script.google.com/macros/s/AKfycbx_w0AofT3G2bqNxuaUvfQLX8OO9MCj83z6NfprmpxxilNNTuW0CN9FgVkSrvlLox1m/exec"
# ==============================================================================

# Folder output relatif terhadap script ini
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data", "data_dinamis")


def pull(nama):
    url = f"{APPSCRIPT_URL}?nama={nama}"
    print(f"📡 Mengambil data untuk: {nama}")
    print(f"   URL: {url}")

    # Bypass SSL verification (kadang perlu untuk Google redirect)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, context=ctx) as resp:
            raw = resp.read().decode("utf-8")
            data = json.loads(raw)
    except Exception as e:
        print(f"❌ Gagal mengambil data: {e}")
        print("   Pastikan:")
        print("   1. URL AppScript sudah diganti di pull_data_dinamis.py")
        print("   2. AppScript sudah di-deploy sebagai Web App (akses: Anyone)")
        return

    # Buat folder output
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if nama.lower() == "all":
        # data = array of {pemilik, data:[...]}
        for member in data:
            save_member(member)
        print(f"\n🎉 Selesai! {len(data)} file JSON tersimpan di: {OUTPUT_DIR}")
    else:
        # data = array dengan 1 elemen
        if data:
            save_member(data[0])
            print(f"\n🎉 Selesai! File tersimpan di: {OUTPUT_DIR}")
        else:
            print("⚠️  Data kosong.")


def save_member(member_data):
    pemilik = member_data.get("pemilik", "unknown").strip()
    member_data["pemilik"] = pemilik
    filename = pemilik.lower().replace(" ", "_") + ".json"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Simpan sebagai array (format yang dibaca oleh load_dinamis_data di template)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([member_data], f, ensure_ascii=False, indent=2)

    jumlah_kating = len(member_data.get("data", []))
    foto_count = sum(1 for d in member_data.get("data", []) if d.get("foto_massal_gdrive_id"))
    kesan_count = sum(1 for d in member_data.get("data", []) if d.get("kesan"))

    print(f"   ✅ {filename} — {jumlah_kating} kating, {foto_count} foto, {kesan_count} kesan/pesan")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("Contoh:")
        print("  python pull_data_dinamis.py rafli")
        print("  python pull_data_dinamis.py all")
        sys.exit(1)

    nama = sys.argv[1].strip()
    pull(nama)
