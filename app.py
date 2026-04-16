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

st.markdown(f"""
<style>
header, footer, #MainMenu {{visibility: hidden;}}

.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
}}

/* BAŞLIK */
.title {{
    text-align:center;
    font-size:40px;
    color:white;
    font-weight:bold;
    margin-top:40px;
}}

/* ALT BLOK */
.bottom {{
    position: fixed;
    bottom: 80px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

/* INPUT */
textarea {{
    width: 600px !important;
    background:#1e1e1e !important;
    color:white !important;
    border-radius:10px !important;
}}

/* BUTON */
button {{
    background:black !important;
    color:white !important;
    border-radius:8px !important;
    margin-top:10px;
}}

/* SONUÇ */
.result {{
    background:#ff7a00;
    color:white;
    padding:20px;
    border-radius:12px;
    font-weight:bold;
    margin-top:20px;
    width:600px;
}}

</style>
""", unsafe_allow_html=True)

# 🎯 BAŞLIK
st.markdown('<div class="title">ZEKİ DEMO</div>', unsafe_allow_html=True)

# 🎯 ALT BLOK
st.markdown('<div class="bottom">', unsafe_allow_html=True)

fis_input = st.text_area(
    "Fiş Numaraları (virgül ile ayır)",
    placeholder="Örn: 50930232,504258239"
)

buton = st.button("İŞE BAŞLA")

# 🚀 ÇALIŞTIR
if buton:

    if not fis_input.strip():
        st.warning("Fiş girilmedi")
    else:
        with st.spinner("Kayıtlar kontrol ediliyor..."):
            time.sleep(1)

        fis_list = [f.strip() for f in fis_input.split(",") if f.strip().isdigit()]

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

        # 🎯 SONUÇ GÖSTER
        for s in sonuc_list:
            st.markdown(f'<div class="result">{s}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
