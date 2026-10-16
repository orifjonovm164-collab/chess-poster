import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = "@Uchesssss"

POSTS = [
    {"type": "text", "text": "♟️ Bilasanmi?\n\nShaxmat taxtasida 64 ta katak bor, har tomonda 16 tadan figura turadi.\n\nPiyoda oxirgi qatorga yetsa, farzinga (yoki boshqa figuraga) aylanadi! 👑"},
    {"type": "quiz", "q": "Skolyar mati necha yurishda qo'yiladi? ♟️", "options": ["2 yurishda", "4 yurishda", "6 yurishda", "8 yurishda"], "correct": 1, "explanation": "Oq farzin va fil f7 ga zarba beradi: 4-yurishda mat! 😎"},
    {"type": "text", "text": "😱 Eng qisqa mat: «Ahmoq mati»\n\n1.f3 e5 2.g4 — va qora farzini h4 ga chiqib mat qo'yadi!\n\nSen ham shunday xatoga tushganmisan? 😅 Izohda yoz 👇"},
    {"type": "quiz", "q": "Qaysi figura «L» shaklida yuradi? 🐴", "options": ["Fil", "Ot", "Rux", "Piyoda"], "correct": 1, "explanation": "Ot ikki katak to'g'ri va bir katak yonga yuradi, boshqa figuralar ustidan sakray oladi."},
    {"type": "text", "text": "🔥 Debyutning 3 oltin qoidasi:\n\n1️⃣ Markazni egalla (e4, d4)\n2️⃣ Figuralarni tez chiqar\n3️⃣ Shohni rokirovka bilan himoyala\n\nSaqlab qo'y! ♟️"},
    {"type": "quiz", "q": "Rokirovka paytida shoh necha katak yuradi? 🏰", "options": ["1 katak", "2 katak", "3 katak", "4 katak"], "correct": 1, "explanation": "Shoh ikki katak yuradi, rux esa uning ustidan o'tib qo'yiladi."},
    {"type": "quiz", "q": "Qaysi figura eng qimmat (shohdan tashqari)? 👑", "options": ["Rux", "Fil", "Farzin", "Ot"], "correct": 2, "explanation": "Farzin taxminan 9 ball, rux 5, fil va ot 3, piyoda 1."},
    {"type": "text", "text": "📜 Shaxmat taxminan 1500 yil oldin Hindistonda «chaturanga» o'yinidan paydo bo'lgan.\n\nBugun uni butun dunyo o'ynaydi! 🌍♟️"},
]


def send(method, payload):
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/{method}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(resp.read().decode())
    except urllib.error.HTTPError as e:
        print("Telegram xatosi:", e.read().decode())
        raise SystemExit(1)


def main():
    now = datetime.now(timezone.utc) + timedelta(hours=5)  # Toshkent vaqti
    slot = max(0, min(2, (now.hour - 10) // 4))
    day = (now.date() - datetime(2024, 1, 1).date()).days
    post = POSTS[(day * 3 + slot) % len(POSTS)]

    if post["type"] == "text":
        send("sendMessage", {"chat_id": CHANNEL, "text": post["text"]})
    else:
        send("sendPoll", {
            "chat_id": CHANNEL,
            "question": post["q"],
            "options": post["options"],
            "type": "quiz",
            "correct_option_id": post["correct"],
            "explanation": post["explanation"],
            "is_anonymous": True,
        })


main()
