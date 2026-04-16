import streamlit as st
import time
import random
import base64

# 📌 SAYFA AYARI
st.set_page_config(layout="wide")

# 📌 ARKA PLAN (dia.png)
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("dia.png")

# 🎨 CSS
st.markdown(f"""
<style>

/* ÜST MENÜLERİ KALDIR */
header, footer, #MainMenu {{visibility: hidden;}}

/* ARKA PLAN */
.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* TÜM İÇERİĞİ ORTALA */
.block-container {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding-top: 120px;
}}

/* BAŞLIK */
.title {{
    font-size: 34px;
    color: white;
    font-weight: bold;
    margin-bottom: 30px;
    text-align: center;
}}

/* INPUT */
textarea {{
    width: 600px !important;
    background-color: #1e1e1e !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 14px !important;
    font-size: 16px !important;
    border: none !important;
}}

/* BUTON */
button {{
    background-color: black !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 10px 25px !important;
    font-weight: bold !important;
    margin-top: 10px;
}}

/* SONUÇ BLOĞU */
.result {{
    background-color: #ff7a00;
    color: white;
    padding: 20px;
    border-radius: 14px;
    font-size: 16px;
    font-weight: bold;
    margin-top: 30px;
    width: 600px;
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
            time.sleep(1)

        fis_list = [f.strip() for f in fis_input.split(",") if f.strip()]

        tum_sonuclar = []

        for fis in fis_list:

            hedef = random.choice(["Hedef Altı", "Hedef Üstü"])
            fiyat = random.choice([8000, 10000, 12000, 15000])
            stok = random.choice([True, False])

            # 🔽 HEDEF ALTI
            if hedef == "Hedef Altı":

                if stok:
                    sonuc = f"{fis} numaralı fiş için 20% KDV dahil {fiyat} TL fatura kesiniz notuyla kayıt servise yönlendirildi"
                else:
                    sonuc = f"{fis} numaralı fiş için muadil ürün önerilir, 20% KDV dahil {fiyat} TL fatura kesiniz notuyla kayıt servise yönlendirildi"

            # 🔽 HEDEF ÜSTÜ
            else:
                dekont = int(fiyat * 0.40)
                fatura = fiyat - dekont

                if stok:
                    sonuc = f"{fis} numaralı fiş için {dekont} TL dekont ediniz, 20% KDV dahil {fatura} TL fatura kesiniz notuyla kayıt servise yönlendirildi"
                else:
                    sonuc = f"{fis} numaralı fiş için muadil ürün önerilir, {dekont} TL dekont ediniz, 20% KDV dahil {fatura} TL fatura kesiniz notuyla kayıt servise yönlendirildi"

            tum_sonuclar.append(sonuc)

        sonuc_html = "<br><br>".join(tum_sonuclar)

        st.markdown(f"""
        <div class="result">
        {sonuc_html}
        </div>
        """, unsafe_allow_html=True)
