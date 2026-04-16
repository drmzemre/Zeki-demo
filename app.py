import streamlit as st
import time
import random
import base64

# 🔥 STREAMLIT HEADER KAPAT
st.markdown("""
<style>
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 🔥 ARKA PLAN (dia.png)
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("dia.png")

# 🎨 CSS TASARIM
st.markdown(f"""
<style>

.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* ÜST BAR */
.top-bar {{
    background-color: rgba(60,60,60,0.9);
    padding: 10px 20px;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 6px;
    width: 60%;
    margin: 40px auto 0 auto;
    text-align: center;
}}

/* KULLANICI */
.user-box {{
    display: flex;
    align-items: center;
    justify-content: center;
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
    background-color: rgba(255,255,255,0.95);
    padding: 30px;
    border-radius: 12px;
    margin-top: 180px;
    width: 50%;
    margin-left: auto;
    margin-right: auto;
}}

/* SONUÇ KUTUSU */
.result-box {{
    background-color: #ff7a00;
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    font-size: 18px;
    font-weight: bold;
}}

</style>
""", unsafe_allow_html=True)

# 🔝 ÜST BAR
st.markdown('<div class="top-bar">☰ Dia</div>', unsafe_allow_html=True)

# 👤 KULLANICI
st.markdown("""
<div class="user-box">
    <div class="user-avatar"></div>
    <div class="user-name">Emre Durmaz</div>
</div>
""", unsafe_allow_html=True)

# 📦 PANEL
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.write("Dia - Online Arçelik Ürün Değişim Sistemlerine Hoşgeldiniz...")

# 📥 ÇOKLU FİŞ GİRİŞİ
fis_input = st.text_area("Fiş Numaraları (virgül ile ayır)")

# 🚀 BUTON
if st.button("İŞE BAŞLA"):

    with st.spinner("Zeki tüm kayıtları inceliyor..."):
        time.sleep(2)

    fis_list = [f.strip() for f in fis_input.split(",") if f.strip()]

    tum_sonuclar = ""

    for fis in fis_list:
        hedef = random.choice(["Hedef Altı", "Hedef Üstü"])
        fiyat = random.choice([8000, 12000, 15000])

        if hedef == "Hedef Altı":
            sonuc = f"{fis} numaralı fiş hedef altı, {fiyat} TL fatura talep edildi, kayıt servise yönlendirildi."
        else:
            dekont = int(fiyat * 0.40)
            fatura = fiyat - dekont
            sonuc = f"{fis} numaralı fiş hedef üstü, {fatura} TL fatura ve {dekont} TL dekont talep edildi, kayıt servise yönlendirildi."

        tum_sonuclar += f"<p>{sonuc}</p>"

    st.markdown(f'<div class="result-box">{tum_sonuclar}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
