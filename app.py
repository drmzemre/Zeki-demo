import streamlit as st
import time
import random
import base64

# 🔥 SAYFA AYARI
st.set_page_config(layout="wide")

# 📌 BACKGROUND (dia.png)
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("dia.png")

st.markdown(f"""
<style>

/* HER ŞEYİ TEMİZLE */
header, footer, #MainMenu {{visibility: hidden;}}

/* BACKGROUND */
.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* İÇ KUTU YOK */
.block-container {{
    background: transparent !important;
    padding-top: 120px;
}}

/* INPUT */
textarea {{
    background-color: #1e1e1e !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 15px !important;
}}

/* BUTON */
button {{
    background-color: #111 !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 10px 20px !important;
    font-weight: bold !important;
}}

/* BAŞLIK */
.title {{
    text-align:center;
    font-size:32px;
    color:white;
    font-weight:bold;
    margin-bottom:30px;
}}

/* SONUÇ BLOĞU */
.result {{
    background-color:#ff7a00;
    color:white;
    padding:20px;
    border-radius:12px;
    font-size:16px;
    font-weight:bold;
    margin-top:20px;
}}

</style>
""", unsafe_allow_html=True)

# 🎯 BAŞLIK
st.markdown("<div class='title'>Ürün Değişim Değerlendirme</div>", unsafe_allow_html=True)

# 📥 INPUT
fis_input = st.text_area(
    "Fiş Numaraları (virgül ile ayır)",
    placeholder="Örn: 50930232,504258239,12345678"
)

# 🚀 BUTON
if st.button("İŞE BAŞLA"):

    if not fis_input.strip():
        st.warning("Fiş girilmedi")
    else:
        with st.spinner("Kayıtlar kontrol ediliyor..."):
            time.sleep(1.5)

        fis_list = [f.strip() for f in fis_input.split(",") if f.strip()]

        tum_sonuclar = []

        for fis in fis_list:

            hedef = random.choice(["Hedef Altı", "Hedef Üstü"])
            fiyat = random.choice([8000, 12000, 15000])
            stok = random.choice([True, False])

            if hedef == "Hedef Altı":

                if stok:
                    sonuc = f"{fis} numaralı fiş için 20% KDV dahil {fiyat} TL fatura kesiniz notuyla kayıt servise yönlendirildi"
                else:
                    sonuc = f"{fis} numaralı fiş için stok bulunamadı, muadil ürün önerilir, 20% KDV dahil {fiyat} TL fatura kesiniz notuyla kayıt servise yönlendirildi"

            else:
                dekont = int(fiyat * 0.40)
                fatura = fiyat - dekont

                if stok:
                    sonuc = f"{fis} numaralı fiş için {dekont} TL dekont ediniz, 20% KDV dahil {fatura} TL fatura kesiniz notuyla kayıt servise yönlendirildi"
                else:
                    sonuc = f"{fis} numaralı fiş için muadil ürün önerilir, {dekont} TL dekont ediniz, 20% KDV dahil {fatura} TL fatura kesiniz notuyla kayıt servise yönlendirildi"

            tum_sonuclar.append(sonuc)

        # 🎯 SONUÇ BAS
        sonuc_html = "<br><br>".join(tum_sonuclar)

        st.markdown(f"""
        <div class="result">
        {sonuc_html}
        </div>
        """, unsafe_allow_html=True)
