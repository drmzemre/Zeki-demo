import streamlit as st
import time
import random

st.title("Ürün Değişim Onay Sistemi")

fis = st.text_input("Fiş No")

if st.button("DEĞERLENDİR"):

    with st.spinner("Kontroller yapılıyor..."):
        time.sleep(2)

    hedef = random.choice(["Hedef Altı", "Hedef Üstü"])
    vergili_fiyat = random.choice([8000, 12000, 15000])

    if hedef == "Hedef Altı":
        sonuc = f"{fis} numaralı fiş hedef altı, {vergili_fiyat} TL fatura talep edildi, kayıt servise yönlendirildi."
    else:
        dekont = int(vergili_fiyat * 0.40)
        fatura = vergili_fiyat - dekont
        sonuc = f"{fis} numaralı fiş hedef üstü, {fatura} TL fatura ve {dekont} TL dekont talep edildi, kayıt servise yönlendirildi."

    st.success(sonuc)
