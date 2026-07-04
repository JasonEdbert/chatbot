import os
from google.genai import Client
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

client = Client(
    api_key=API_KEY,
    http_options={'api_version': 'v1'}
)

MODEL_ID = "gemini-2.5-flash"

# Membuat satu sesi chat global agar bot mengingat riwayat obrolan di web
chat_session = client.chats.create(model=MODEL_ID)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/kirim_pesan', methods=['POST'])
def chat():
    data = request.get_json()
    pesan_user = data.get('pesan')
    
    if not pesan_user:
        return jsonify({'jawaban': 'Pesan kosong.'})
    
    try:
        # Mengirim pesan menggunakan sesi chat yang aktif
        response = chat_session.send_message(pesan_user)
        jawaban_bot = response.text
    except Exception as e:
        jawaban_bot = f"Error: {e}"
        
    return jsonify({'jawaban': jawaban_bot})

# Route tambahan jika Anda ingin membuat tombol "Reset Chat" di HTML
@app.route('/reset_chat', methods=['POST'])
def reset():
    global chat_session
    chat_session = client.chats.create(model=MODEL_ID)
    return jsonify({'status': 'Sesi chat telah di-reset.'})

if __name__ == '__main__':
    app.run(debug=True)
