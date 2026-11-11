import streamlit as st

# Sayfa başlığı
st.title("🔬 LGS Fen Bilimleri Analizi")
st.write("Öğrenci net hesaplama ve ilk durum tespiti.")

# Kullanıcıdan veri alma alanları
isim = st.text_input("Öğrencinin Adı:")
dogru = st.number_input("Doğru Sayısı:", min_value=0, max_value=20, value=0)
yanlis = st.number_input("Yanlış Sayısı:", min_value=0, max_value=20, value=0)

# Hesaplama butonu
if st.button("Neti Hesapla ve Analiz Et"):
    
    # 3 yanlış 1 doğruyu götürür formülü
    net = dogru - (yanlis / 3)
    
    # Sonucu ekrana yazdırma
    st.success(f"**{isim}** adlı öğrencinin neti: **{net:.2f}**")
    
    # Öğretmenin istediği mantıksal uyarılar
    if net >= 15:
        st.success("🟢 Harika durum! Yeni nesil zor sorulara ağırlık verilebilir.")
    elif net >= 10:
        st.warning("🟡 Eksik konular var, geçmiş denemelerdeki hatalar taranmalı.")
    else:
        st.error("🔴 Temel kavramlarda ciddi eksikler var, konu anlatımına dönülmeli.")
