import streamlit as st
import time
import random
import base64

st.set_page_config(layout="wide")

# 📌 ARKA PLAN
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
</style>
""", unsafe_allow_html=True)

# 🎯 BAŞLIK
st.markdown(
    "<h1 style='text-align:center; color:white;'>Ürün Değişim Değerlendirme</h1>",
    unsafe_allow_html=True
)

# 🎯 ORTA ALAN
col1, col2, col3 = st.columns([1,2,1])

with col2:
    fis_input = st.text_area(
        "Fiş Numaraları (virgül ile ayır)",
        placeholder="Örn: 50930232,504258239,12345678"
    )

    calistir = st.button("İŞE BAŞLA")

    # 🔥 SONUÇ BURADA GÖRÜNECEK
    if calistir:

        if not fis_input.strip():
            st.warning("Fiş girilmedi")
        else:
            time.sleep(1)

            fis_list = [f.strip() for f in fis_input.split(",") if f.strip()]
            sonuclar = []

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

                sonuclar.append(sonuc)

            # 🔥 SONUÇ (KESİN GÖRÜNÜR)
            for s in sonuclar:
                st.markdown(
                    f"""
                    <div style="
                        background-color:#ff7a00;
                        color:white;
                        padding:15px;
                        border-radius:10px;
                        margin-top:10px;
                        font-weight:bold;
                    ">
                    {s}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
