import os
import telegram
from flask import Flask, request, jsonify, send_from_directory

# --- Konfigurasi ---
# Ganti dengan token bot Telegram Anda yang sebenarnya
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'GANTI_DENGAN_TOKEN_BOT_ANDA')
# Ganti dengan URL webhook Anda jika menggunakan mode webhook
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', 'https://example.com/webhook')

# Tentukan path absolut untuk direktori frontend
# Ini mengasumsikan 'frontend' berada satu level di atas direktori 'backend'
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend')


# --- Inisialisasi Aplikasi ---
# Sajikan file statis dari direktori frontend
app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path='')
bot = telegram.Bot(token=BOT_TOKEN)


# --- Rute untuk Menyajikan Frontend ---

@app.route('/')
def serve_index():
    """Menyajikan halaman utama panel (index.html)."""
    return send_from_directory(FRONTEND_DIR, 'index.html')

# --- Rute API ---

@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Endpoint API untuk mengirim pesan melalui bot.
    Membutuhkan 'chat_id' dan 'text' dalam format JSON.
    """
    if not request.is_json:
        return jsonify({"error": "Request harus dalam format JSON"}), 400

    data = request.get_json()
    chat_id = data.get('chat_id')
    text = data.get('text')

    if not chat_id or not text:
        return jsonify({"error": "Payload JSON harus menyertakan 'chat_id' dan 'text'"}), 400

    try:
        bot.send_message(chat_id=chat_id, text=text)
        return jsonify({"success": True, "message": f"Pesan terkirim ke {chat_id}"}), 200
    except telegram.error.TelegramError as e:
        return jsonify({"success": False, "error": str(e)}), 500

# --- Fungsi Tambahan (Contoh: Webhook) ---

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook_handler():
    """Menangani update dari Telegram (mode webhook)."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        # Logika untuk menangani pesan masuk dari bot bisa ditambahkan di sini
        # Contoh: echo bot
        if update.message and update.message.text:
            chat_id = update.message.chat_id
            text = update.message.text
            bot.send_message(chat_id=chat_id, text=f"Echo: {text}")
    return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    """Mengatur webhook bot secara manual."""
    # URL webhook harus menggunakan HTTPS
    s = bot.set_webhook(f'{WEBHOOK_URL}/{BOT_TOKEN}')
    if s:
        return "Webhook berhasil diatur"
    else:
        return "Gagal mengatur webhook"

# --- Menjalankan Aplikasi ---
if __name__ == '__main__':
    # Port bisa diubah sesuai kebutuhan
    app.run(host='0.0.0.0', port=5000)
