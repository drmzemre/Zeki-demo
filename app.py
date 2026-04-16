import streamlit as st
import time
import random
import base64

# 🔥 ARKA PLAN GÖRSELİ (bg.png)
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("bg.png")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* ÜST BAR */
    .top-bar {{
        background-color: #3c3c3c;
        padding: 10px 20px;
        color: white;
        font-size: 18px;
        font-weight: bold;
    }}

    /* KULLANICI */
    .user-box {{
        display: flex;
        align-items: center;
        margin-top: 20px;
    }}

    .user-avatar {{
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-color: #2ecc71;
        margin-right: 15px;
    }}

    .user-name {{
        font-size: 20px;
        font-weight: bold;
        color: black;
    }}

    /* ANA PANEL */
    .main-card {{
        background-color: rgba(255,255,255,0.92);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
    }}

    /* SONUÇ */
    .result-box {{
        background-color: #d4edda;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
        font-size: 16px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 🔝 ÜST BAR
st.markdown('<div class="top-bar">☰ Dia</div>', unsafe_allow_html=True)

# 👤 KULLANICI
st.markdown(
    """
    <div class="user-box">
        <div class="user-avatar"></div>
        <div class="user-name">Emre Durmaz</div>
    </div>
    """,
    unsafe_allow_html=True
)

# 📦 ANA PANEL
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.write("Dia - Online Arçelik Ürün Değişim Sistemlerine Hoşgeldiniz...")

# 📥 FİŞ
fis = st.text_input("Fiş No")

# 🚀 BUTON
if st.button("DEĞERLENDİR"):

    with st.spinner("Zeki değerlendiriyor..."):
        time.sleep(2)

    hedef = random.choice(["Hedef Altı", "Hedef Üstü"])
    fiyat = random.choice([8000, 12000, 15000])

    if hedef == "Hedef Altı":
        sonuc = f"{fis} numaralı fiş hedef altı, {fiyat} TL fatura talep edildi, kayıt servise yönlendirildi."
    else:
        dekont = int(fiyat * 0.40)
        fatura = fiyat - dekont
        sonuc = f"{fis} numaralı fiş hedef üstü, {fatura} TL fatura ve {dekont} TL dekont talep edildi, kayıt servise yönlendirildi."

    st.markdown(f'<div class="result-box">{sonuc}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
