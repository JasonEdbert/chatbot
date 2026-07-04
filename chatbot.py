import asyncio
import os
from google.genai import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

client = Client(
    api_key=API_KEY,
    http_options={'api_version': 'v1'}
)

MODEL_ID = "gemini-2.5-flash"

def dapatkan_respon(pesan_user):
    try:
        # Kita buat chat session sederhana untuk satu kali tanya-jawab
        chat = client.chats.create(model=MODEL_ID)
        response = chat.send_message(pesan_user)
        return response.text
    except Exception as e:
        return f"Error: {e}"
    
#async def ainput(prompt: str) -> str:
#    return await asyncio.to_thread(input, prompt)
#
#async def chat_loop():
#    if not API_KEY:
#        print("[ERROR] GEMINI_API_KEY tidak ditemukan di file .env")
#        return
#
#    print("-" * 60)
#    print(" AI Chatbot - Google Gemini (Official SDK)")
#    print(" Ketik 'exit' untuk keluar, 'reset' untuk mulai sesi baru")
#    print("-" * 60)
#
#    chat = client.chats.create(model=MODEL_ID)
#
#    while True:
#        try:
#            user_input = await ainput("\nKamu : ")
#            user_input = user_input.strip()
#        except (EOFError, KeyboardInterrupt):
#            print("\nSampai jumpa!")
#            break
#
#        if not user_input:
#            continue
#
#        if user_input.lower() in {"exit", "quit"}:
#            print("Sampai jumpa!")
#            break
#
#        if user_input.lower() == "reset":
#            chat = client.chats.create(model=MODEL_ID)
#            print("[INFO] Sesi chat di-reset.")
#            continue
#
#        try:
#            response = chat.send_message(user_input)
#            print(f"\nBot : {response.text}")
#        except Exception as e:
#            print(f"\n[ERROR] {e}")

#if __name__ == "__main__":
#    asyncio.run(chat_loop())