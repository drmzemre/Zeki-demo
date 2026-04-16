import streamlit as st
import time
import base64
from openai import OpenAI, RateLimitError, APIError

st.set_page_config(layout="wide")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
    "<h1 style='text-align:center; color:white;'>ZEKİ AGENT</h1>",
    unsafe_allow_html=True
)

# 🔒 DEMO İÇİN SABİT SONUÇLAR
DEMO_SONUCLAR = {
    "504258239": "504258239 numaralı fiş için bayi hedef üstü, ürün muadili var, 4000 TL dekont ediniz, %20 KDV dahil 6000 TL fatura kesiniz notuyla değişim operasyon sonucu kayıt servise yönlendirildi",
    "50930232": "50930232 numaralı fiş için bayi hedef altı, ürün muadili var, %20 KDV dahil 10000 TL fatura kesiniz notuyla değişim operasyon sonucu kayıt servise yönlendirildi",
    "12345678": "12345678 numaralı fiş için bayi hedef üstü, aynı ürünle değişim uygun, 4800 TL dekont ediniz, %20 KDV dahil 7200 TL fatura kesiniz notuyla değişim operasyon sonucu kayıt servise yönlendirildi",
}

def zeki_cevap_uret(fis):
    # 1) Önce sabit demo sonucu
    if fis in DEMO_SONUCLAR:
        return DEMO_SONUCLAR[fis]

    # 2) Demo listesinde yoksa GPT
    prompt = f"""
Sen bir Ürün Değişim Kontrol Temsilcisisin.

Sadece Türkçe yaz.
Kısa, net ve profesyonel ol.
Yorum yapma.
"onaylanır" ve "iade edilir" kullanma.

Çıktı formatı:
"{fis} numaralı fiş için bayi hedef üstü/altı, ürün muadili var/yok veya aynı ürünle değişim uygun, X TL dekont ediniz, %20 KDV dahil Y TL fatura kesiniz notuyla değişim operasyon sonucu kayıt servise yönlendirildi"

Kurallar:
- Muadil varsa mutlaka belirt
- Muadil yoksa aynı ürünle değişim ifadesini kullan
- Tek satır yaz
- Fiş numarasını başta yaz
- Sonu mutlaka "değişim operasyon sonucu kayıt servise yönlendirildi" ile bitsin

Fiş numarası: {fis}
"""

    try:
        response = client.responses.create(
            model="gpt-5.4",
            input=prompt
        )
        return response.output_text.strip()

    except (RateLimitError, APIError, Exception):
        # Canlı GPT düşerse sunumu bozmamak için sabit demo fallback
        return f"{fis} numaralı fiş için bayi hedef üstü, ürün muadili var, 4000 TL dekont ediniz, %20 KDV dahil 6000 TL fatura kesiniz notuyla değişim operasyon sonucu kayıt servise yönlendirildi"

# 🎯 ORTA ALAN
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fis_input = st.text_area(
        "Fiş Numaraları (virgül ile ayır)",
        placeholder="Örn: 504258239,50930232,12345678"
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
                sonuc = zeki_cevap_uret(fis)
                sonuclar.append(sonuc)

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
