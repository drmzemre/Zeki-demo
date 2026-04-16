import streamlit as st
import time
import base64
from openai import OpenAI

st.set_page_config(layout="wide")

# 🔐 OPENAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 📌 ARKA PLAN (AYNI - DOKUNMADIM)
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

# 🎯 BAŞLIK (İSTERSEN BURAYI ZEKİ AGENT YAPARSIN)
st.markdown(
    "<h1 style='text-align:center; color:white;'>Ürün Değişim Değerlendirme</h1>",
    unsafe_allow_html=True
)

# 🧠 GPT FONKSİYONU (SADE + SENİN FORMAT)
def zeki_cevap_uret(fis):

    prompt = f"""
Sen bir Ürün Değişim Kontrol Temsilcisisin.

Kurallar:
- Türkçe yaz
- Kısa ve net ol
- "onaylanır", "iade edilir" kullanma
- Tek satır sonuç ver
- Fiş numarasını mutlaka yaz
- Sonu "kayıt servise yönlendirildi" ile bitmeli

Fiş: {fis}

Sadece operasyon sonucu üret.
"""

    response = client.responses.create(
        model="gpt-5.4",
        input=prompt
    )

    return response.output_text.strip()

# 🎯 ORTA ALAN (AYNI - DOKUNMADIM)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    fis_input = st.text_area(
        "Fiş Numaraları (virgül ile ayır)",
        placeholder="Örn: 50930232,504258239,12345678"
    )

    calistir = st.button("İŞE BAŞLA")

    # 🔥 SONUÇ BURADA GÖRÜNECEK (AYNI TASARIM)
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

            # 🔥 TURUNCU SONUÇ BLOĞU (AYNI)
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
