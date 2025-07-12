# Chatbot Streamlit dengan Gemini API, context dari file upload (txt, docx, pdf, xlsx)
import streamlit as st

import os
import requests
from PyPDF2 import PdfReader
from docx import Document
import openpyxl

# --- Konfigurasi API Gemini ---

GEMINI_API_KEY = "AIzaSyAbqQnYIhHsAN085jaS4jxPxVEGtQ7XqmA"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + GEMINI_API_KEY
if not GEMINI_API_KEY:
    st.error("Masukkan API Key Gemini di environment variable GEMINI_API_KEY atau di .streamlit/secrets.toml")
    st.stop()

st.title("Chatbot 17 Agustus Berbasis File & Gemini")
st.write("Upload file (txt, docx, pdf, xlsx) berisi informasi kegiatan. Chatbot hanya menjawab sesuai isi file.")

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        doc = Document(uploaded_file)
        return "\n".join([p.text for p in doc.paragraphs])
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        wb = openpyxl.load_workbook(uploaded_file, data_only=True)
        text = ""
        for ws in wb.worksheets:
            for row in ws.iter_rows(values_only=True):
                text += "\t".join([str(cell) if cell is not None else "" for cell in row]) + "\n"
        return text
    else:
        return ""

uploaded_file = st.file_uploader("Upload file context (txt, docx, pdf, xlsx)", type=["txt", "pdf", "docx", "xlsx"])
context = ""
if uploaded_file:
    context = extract_text_from_file(uploaded_file)
    st.success("File berhasil diupload dan dibaca.")
    with st.expander("Lihat context (isi file)"):
        st.write(context[:2000] + ("..." if len(context) > 2000 else ""))

if not context:
    st.info("Silakan upload file terlebih dahulu.")
    st.stop()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



user_input = st.text_input("Tulis pertanyaan Anda:")
if st.button("Kirim") and user_input:
    prompt = f"Jawablah hanya berdasarkan informasi berikut:\n{context}\n\nPertanyaan: {user_input}\nJawaban:"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    try:
        resp = requests.post(GEMINI_API_URL, headers=headers, json=data)
        if resp.status_code == 200:
            result = resp.json()
            answer = result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            answer = f"Terjadi error: {resp.status_code} - {resp.text}"
    except Exception as e:
        answer = f"Terjadi error: {e}"
    st.session_state.chat_history.append((user_input, answer))

if st.session_state.chat_history:
    st.write("## Riwayat Chat")
    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**Anda:** {q}")
        st.markdown(f"**Bot:** {a}")