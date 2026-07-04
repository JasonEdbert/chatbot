import streamlit as st
# Import fungsi utama dari skrip chatbot lama Anda
# Misal nama fungsinya adalah 'dapatkan_respon'
from chatbot import dapatkan_respon 

st.title("Chatbot simple")

# --- Logika Streamlit (Tampilan Chat) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tanya sesuatu..."):
    # 1. Tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Panggil fungsi chatbot lama Anda untuk mendapatkan jawaban
    # Ini adalah bagian yang memindahkan hasil terminal ke website
    jawaban = dapatkan_respon(prompt) 

    # 3. Tampilkan jawaban di website
    with st.chat_message("assistant"):
        st.markdown(jawaban)
    st.session_state.messages.append({"role": "assistant", "content": jawaban})