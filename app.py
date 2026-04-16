import streamlit as st
import time
import random
import base64

# 🔥 HEADER VE MENÜ KALDIR
st.markdown("""
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 🔥 ARKA PLAN (blur + karartma)
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("dia.png")

st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
}}

/* ANA KUTU */
.main-box {{
    background: rgba(255,255,255,0.95);
    padding: 40px;
    border-radius: 12px;
    width: 40%;
    margin: 120px auto;
    text-align: center;
}}

/* INPUT */
textarea {{
    background-color: #2c2f36 !important;
    color: white !important;
    border-radius: 8px !important;
}}

/* BUTON */
button {{
    background-color: #111 !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 10px 20px !important;
}}

/* SONUÇ */
.result-box {{
    background-color: #ff7a00;
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    font-size: 18px;
    font-weight: bold;
    text-align: left;
}}

</style>
""", unsafe_allow_html=True)

# 📦 ANA PANEL
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.markdown("### Ürün Değişim Değerlendirme")

fis_input = st.text_area("Fiş Numaraları (virgül ile ayır)")

if st.button("İŞE BAŞLA"):

    with st.spinner("Kayıtlar değerlendiriliyor..."):
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
