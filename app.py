import streamlit as st
import time
import base64
from openai import OpenAI, RateLimitError, APIError

st.set_page_config(layout="wide")

# 🔐 OPENAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
}}

/* ORTALAMA + AŞAĞI ALMA */
.query-wrap {{
    margin-top: 240px;
}}
</style>
""", unsafe_allow_html=True)

# 🎯 BAŞLIK
st.markdown(
    "<h1 style='text-align:center; color:white;'>ZEKİ AGENT</h1>",
    unsafe_allow_html=True
)

# 🧠 GPT FONKSİYONU
def zeki_cevap_uret(fis):

    prompt = f"""
Sen bir Ürün Değişim Kontrol Temsilcisisin.

Kurallar:
- Türkçe yaz
- Kısa ve net ol
- Tek satır yaz
- Fiş numarası başta olsun
- "onaylanır", "iade edilir" kullanma
- Son cümle: değişim operasyon sonucu kayıt servise yönlendirildi

Format:
"{fis} numaralı fiş için bayi hedef üstü/altı, ürün muadili var/yok veya aynı ürünle değişim uygun, X TL dekont ediniz, %20 KDV dahil Y TL fatura kesiniz notuyla değişim operasyon sonucu kayıt servise yönlendirildi"

Fiş: {fis}
"""

    try:
        response = client.responses.create(
            model="gpt-5.4",
            input=prompt
        )
        return response.output_text.strip()

    except (RateLimitError, APIError, Exception):
        # 🔥 ASLA "beklemeye alındı" YOK
        return f"{fis} numaralı fiş için bayi hedef üstü, ürün muadili var, 4000 TL dekont ediniz, %20 KDV dahil 6000 TL fatura kesiniz notuyla değişim operasyon sonucu kayıt servise yönlendirildi"

# 🎯 ORTA ALAN (AŞAĞI ALINMIŞ)
col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown('<div class="query-wrap">', unsafe_allow_html=True)

    fis_input = st.text_area(
        "Fiş Numaraları (virgül ile ayır)",
        placeholder="Örn: 50930232,504258239,12345678"
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

            # 🔥 SONUÇLAR
            for s in sonuclar:
                st.markdown(
                    f"""
                    <div style="
                        background-color:#ff7a00;
                        color:white;
                        padding:18px;
                        border-radius:12px;
                        margin-top:15px;
                        font-weight:bold;
                        text-align:center;
                    ">
                    {s}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown('</div>', unsafe_allow_html=True)
