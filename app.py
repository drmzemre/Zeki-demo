import streamlit as st
import time

st.title("Ürün Değişim Onay Sistemi")

fis = st.text_input("Fiş No")
notu = st.text_area("Servis Notu")
barkod = st.selectbox("Barkod", ["Okutuldu", "Okutulmadı"])
hedef = st.selectbox("Hedef", ["Hedef Altı", "Hedef Üstü"])

if st.button("DEĞERLENDİR"):
    with st.spinner("Kontrol ediliyor..."):
        time.sleep(2)

    if barkod == "Okutulmadı":
        st.error("Kayıt servise yönlendirildi")
        st.write("Barkod okutunuz")

    elif "memnun değil" in notu.lower():
        st.error("Değişim uygun değildir")

    else:
        st.success("Kayıt servise yönlendirildi")

        if hedef == "Hedef Üstü":
            fiyat = 12000
            dekont = int(fiyat * 0.40)
            fatura = fiyat - dekont

            st.write(f"Vergili fiyat: {fiyat}")
            st.write(f"Dekont: {dekont}")
            st.write(f"Fatura: {fatura}")
