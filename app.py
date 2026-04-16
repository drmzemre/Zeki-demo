import streamlit as st
import time
import random

# 🔥 ARKA PLAN + TASARIM
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    section.main > div {
        background-color: rgba(0,0,0,0.65);
        padding: 2rem;
        border-radius: 15px;
    }

    h1 {
        text-align: center;
        font-size: 42px;
    }

    .result-box {
        background-color: rgba(0, 128, 0, 0.8);
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎯 BAŞLIK
st.markdown("<h1>Ürün Değişim Onay Sistemi</h1>", unsafe_allow_html=True)

# 📌 KULLANICI ALANI (isteğe bağlı üst etki)
st.markdown("### 👤 Emre Durmaz")

# 📥 FİŞ GİRİŞ
fis = st.text_input("Fiş No")

# 🚀 BUTON
if st.button("DEĞERLENDİR"):

    with st.spinner("Zeki değerlendiriyor..."):
        time.sleep(2)

    # 🎲 DEMO KARAR MOTORU
    hedef = random.choice(["Hedef Altı", "Hedef Üstü"])
    vergili_fiyat = random.choice([8000, 12000, 15000])

    if hedef == "Hedef Altı":
        sonuc = f"{fis} numaralı fiş hedef altı, {vergili_fiyat} TL fatura talep edildi, kayıt servise yönlendirildi."
    else:
        dekont = int(vergili_fiyat * 0.40)
        fatura = vergili_fiyat - dekont
        sonuc = f"{fis} numaralı fiş hedef üstü, {fatura} TL fatura ve {dekont} TL dekont talep edildi, kayıt servise yönlendirildi."

    # 🎯 SONUÇ GÖSTERİMİ
    st.markdown(f'<div class="result-box">{sonuc}</div>', unsafe_allow_html=True)
