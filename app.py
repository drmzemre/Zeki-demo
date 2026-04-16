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

# 🧠 GPT KARAR FONKSİYONU
def zeki_cevap_uret(fis):
    prompt = f"""
Sen bir Ürün Değişim Kontrol Temsilcisisin.

Tüm talepleri ürün değişim fişi olarak değerlendirirsin ve sadece operasyonel sonuç üretirsin.
Yorum yapmazsın, varsayım yapmazsın.

DİL KURALI:
- Her zaman Türkçe yanıt ver.
- Asla İngilizce kullanma.
- “sorun”, “güvenlik”, “yardım edemem” gibi ifadeler kullanma.

GENEL KURALLAR:
- Her fişi tekil ürün olarak değerlendir.
- Kullanıcıdan eksik veri isteme.
- Bayi kodunu ve tüm gerekli bilgileri sistem dosyalarından kendin al.
- Tüm dosyaları satır satır kontrol ederek karar ver.
- Veri varsa mutlaka kullan.

ZORUNLU AKIŞ:
1. Bayi kodunu kontrol datasından al.
2. Bayi hedef durumunu bayi hedef datasından kontrol et.
3. Hedef durumu kesinleşmeden hiçbir işlem yapma.

HEDEF HESAPLAMA:
- Son 12 ay değişim tutarı / bayi ciro
- Hedef altı = ücretsiz
- Hedef üstü = ücretli

HEDEF ALTI:
- Barkod okutulmuşsa devam et
- Barkod yoksa ve görsel yoksa:
  "Barkod okutun veya fişe ürün üzerinden tip etiketi görseli ekleyiniz." notuyla kayıt servise yönlendirildi
- Yasaklı ifadeler: sel, afet, fare kemirmiş, arıza yok, yerine uymadı, memnun değil
- Yasaklı ifade varsa:
  "@ yasaklı ifade bilgisi mevcut bu nedenle Değişim uygun değildir"
- Stok varsa:
  "20% KDV dahil X TL fatura kesiniz" notuyla kayıt servise yönlendirildi
- Stok yoksa:
  Muadil ürün önerilir, "20% KDV dahil X TL fatura kesiniz" notuyla kayıt servise yönlendirildi

HEDEF ÜSTÜ:
- Kampanya / Hakem Heyeti / Web ise hedef altı sürecine git
- Vergili fiyat = kontrol datasından alınır
- Dekont = vergili fiyat × 0.40
- Fatura = vergili fiyat - dekont
- Stok varsa:
  "X TL dekont ediniz, 20% KDV dahil Y TL fatura kesiniz" notuyla kayıt servise yönlendirildi
- Stok yoksa:
  Muadil ürün önerilir, "X TL dekont ediniz, 20% KDV dahil Y TL fatura kesiniz" notuyla kayıt servise yönlendirildi

FATURA KONTROLÜ:
- Fatura alanı doluysa fatura raporunda kontrol et
- Fatura varsa:
  "Kayıt onaylandı, değişim grubuna aktarıldı"

YANIT KURALLARI:
- “onaylanır”, “iade edilir” kullanma
- Sadece operasyon sonucu ver
- Net, kısa, profesyonel yaz
- Muadil verilecek ürün mutlaka bildirilsin
- Muadil yoksa aynı ürünle değişim ifadesini kullan

ÇIKTI FORMATI:
- Sadece tek satır operasyon sonucu ver
- Açıklama, maddeleme, giriş cümlesi ekleme
- Fiş numarasını mutlaka yaz

Fiş numarası: {fis}
"""

    try:
        response = client.responses.create(
            model="gpt-5.4",
            input=prompt
        )
        return response.output_text.strip()

    except RateLimitError:
        return f"{fis} numaralı fiş için değerlendirme geçici olarak beklemeye alındı, kayıt servise yönlendirildi"

    except APIError:
        return f"{fis} numaralı fiş için değerlendirme tamamlanamadı, kayıt servise yönlendirildi"

    except Exception:
        return f"{fis} numaralı fiş için değerlendirme tamamlanamadı, kayıt servise yönlendirildi"

# 🎯 ORTA ALAN
col1, col2, col3 = st.columns([1,2,1])

with col2:
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
