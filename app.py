import streamlit as st
import time
import random

# 🔥 TÜM STREAMLIT UI ÇÖPÜNÜ KALDIR
st.markdown("""
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
section[data-testid="stToolbar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# 🎯 SAYFA AYARI
st.set_page_config(layout="centered")

# 📦 ANA ALAN
st.markdown("<h2 style='text-align:center;'>Ürün Değişim Değerlendirme</h2>", unsafe_allow_html=True)

# 📥 INPUT
fis_input = st.text_area(
    "Fiş Numaraları (virgül ile ayır)",
    placeholder="Örn: 50930232, 504258239, 12345678"
)

# 🚀 BUTON
if st.button("İŞE BAŞLA"):

    if not fis_input.strip():
        st.warning("Lütfen fiş numarası gir.")
    else:
        with st.spinner("Kayıtlar değerlendiriliyor..."):
            time.sleep(1.5)

        fis_list = [f.strip() for f in fis_input.split(",") if f.strip()]

        tum_sonuclar = []

        for fis in fis_list:
            hedef = random.choice(["Hedef Altı", "Hedef Üstü"])
            fiyat = random.choice([8000, 12000, 15000])

            if hedef == "Hedef Altı":
                sonuc = f"{fis} numaralı fiş hedef altı, {fiyat} TL fatura talep edildi, kayıt servise yönlendirildi."
            else:
                dekont = int(fiyat * 0.40)
                fatura = fiyat - dekont
                sonuc = f"{fis} numaralı fiş hedef üstü, {fatura} TL fatura ve {dekont} TL dekont talep edildi, kayıt servise yönlendirildi."

            tum_sonuclar.append(sonuc)

        # 🎯 TURUNCU SONUÇ BLOĞU
        sonuc_html = "<br>".join(tum_sonuclar)

        st.markdown(f"""
        <div style="
            background-color:#ff7a00;
            color:white;
            padding:20px;
            border-radius:10px;
            margin-top:20px;
            font-size:16px;
            font-weight:bold;">
            {sonuc_html}
        </div>
        """, unsafe_allow_html=True)
