import streamlit as st
import time
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

/* ARKA PLAN */
.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* SORGU BLOĞUNU AŞAĞI AL */
.query-wrap {{
    margin-top: 260px;
}}

/* TURUNCU SONUÇ KUTUSU */
.result-box {{
    background-color: #ff7a00;
    color: white;
    padding: 18px;
    border-radius: 12px;
    margin-top: 15px;
    font-weight: bold;
    text-align: left;
    line-height: 1.6;
}}
</style>
""", unsafe_allow_html=True)

# 🎯 BAŞLIK
st.markdown(
    "<h1 style='text-align:center; color:white;'>ZEKİ AGENT</h1>",
    unsafe_allow_html=True
)

# 📌 SABİT FİŞ SONUÇLARI
FIS_SONUCLARI = {
    "504258239": """504258239 numaralı fiş için bayi kodu 22468002, bayi hedef durumu HedefÜstü, barkod okutulmuş, servis notu uygun, stok durumu yok, muadil öneri 8911231200 – FK 8110 I. Vergili tutar 20.000,00 TL, dekont tutarı 8.000,00 TL, fatura tutarı 12.000,00 TL. Kayıt yetkili servise yönlendirildi. Mesaj alanı: “8911231200 FK 8110 I muadil model bilgisi öneriniz kabul edilir ise 8.000,00 TL dekont ediniz, %20 KDV dahil 12.000,00 TL tutarında fatura kesiniz.”""",

    "509028569": """509028569 numaralı fiş için bayi kodu 22506513, bayi hedef durumu HedefAltı, barkod okutulmuş, servis notu uygun, stok durumu var. Vergili tutar 25.000,00 TL. Kayıt yetkili servise yönlendirildi. Mesaj alanı: “%20 KDV dahil 25.000,00 TL fatura kesiniz.”""",

    "508777808": """508777808 numaralı fiş için bayi kodu 22438522, bayi hedef durumu HedefAltı, barkod okutulmuş, servis notu uygun. Fatura numarası mevcut ve Fatura Raporu’nda bulundu. Kayıt onaylandı, fiş değişim grubuna aktarıldı. Fatura No: YSL2026000001, Tarih: 2026-03-04."""
}

# 🎯 ORTA ALAN
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="query-wrap">', unsafe_allow_html=True)

    fis_input = st.text_area(
        "Fiş Numaraları (virgül ile ayır)",
        placeholder="Örn: 504258239,509028569,508777808"
    )

    calistir = st.button("İŞE BAŞLA")

    if calistir:
        if not fis_input.strip():
            st.warning("Fiş girilmedi")
        else:
            with st.spinner("Kayıtlar kontrol ediliyor..."):
                time.sleep(1)

            fis_list = [f.strip() for f in fis_input.split(",") if f.strip()]
            sonuclar = []

            for fis in fis_list:
                if fis in FIS_SONUCLARI:
                    sonuclar.append(FIS_SONUCLARI[fis])
                else:
                    sonuclar.append(
                        f"{fis} numaralı fiş sistemde bulunamadı."
                    )

            for s in sonuclar:
                st.markdown(
                    f'<div class="result-box">{s}</div>',
                    unsafe_allow_html=True
                )

    st.markdown('</div>', unsafe_allow_html=True)
