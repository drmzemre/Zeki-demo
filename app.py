import streamlit as st
import time
import random
import base64

st.set_page_config(layout="wide")

# 📌 BACKGROUND
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("dia.png")

# 🎨 STYLE
st.markdown(f"""
<style>

header, footer, #MainMenu {{visibility: hidden;}}

/* ARKA PLAN */
.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
}}

/* GRID YAPI */
.main {{
    display: flex;
    flex-direction: column;
    height: 100vh;
    justify-content: space-between;
}}

/* ÜST */
.top {{
    text-align: center;
    margin-top: 40px;
    font-size: 34px;
    color: white;
    font-weight: bold;
}}

/* ALT BLOK */
.bottom {{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 80px;
}}

/* INPUT */
textarea {{
    width: 600px !important;
    background-color: #1e1e1e !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 14px !important;
}}

/* BUTON */
button {{
    background-color: black !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 10px 25px !important;
    margin-top: 10px;
}}

/* SONUÇ */
.result {{
    background-color: #ff7a00;
    color: white;
    padding: 20px;
    border-radius: 12px;
    font-weight: bold;
    margin-top: 20px;
    width: 600px;
}}

</style>
""", unsafe_allow_html=True)

# 🎯 ÜST BAŞLIK
st.markdown('<div class="top">Ürün Değişim Değerlendirme</div>', unsafe_allow_html=True)

# 🎯 ALT BLOK (ORTA-ALT)
st.markdown('<div class="bottom">', unsafe_allow_html=True)

fis_input = st.text_area(
    "Fiş Numaraları (virgül ile ayır)",
    placeholder="Örn: 50930232,504258239,12345678"
)

buton = st.button("İŞE BAŞLA")

# 🚀 ÇALIŞMA BLOĞU
if buton:

    if not fis_input.strip():
        st.warning("Fiş girilmedi")
    else:
        with st.spinner("Kayıtlar kontrol ediliyor..."):
            time.sleep(1)

        fis_list = [f.strip() for f in fis_input.split(",") if f.strip()]
        sonuc_list = []

        for fis in fis_list:

            hedef = random.choice(["Hedef Altı", "Hedef Üstü"])
            fiyat = random.choice([8000, 10000, 12000])
            stok = random.choice([True, False])

            if hedef == "Hedef Altı":

                if stok:
                    sonuc = f"{fis} numaralı fiş için 20% KDV dahil {fiyat} TL fatura kesiniz notuyla kayıt servise yönlendirildi"
                else:
                    sonuc = f"{fis} numaralı fiş için muadil ürün önerilir, 20% KDV dahil {fiyat} TL fatura kesiniz notuyla kayıt servise yönlendirildi"

            else:
                dekont = int(fiyat * 0.40)
                fatura = fiyat - dekont

                if stok:
                    sonuc = f"{fis} numaralı fiş için {dekont} TL dekont ediniz, 20% KDV dahil {fatura} TL fatura kesiniz notuyla kayıt servise yönlendirildi"
                else:
                    sonuc = f"{fis} numaralı fiş için muadil ürün önerilir, {dekont} TL dekont ediniz, 20% KDV dahil {fatura} TL fatura kesiniz notuyla kayıt servise yönlendirildi"

            sonuc_list.append(sonuc)

        final = "<br><br>".join(sonuc_list)

        st.markdown(f'<div class="result">{final}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
