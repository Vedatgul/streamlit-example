import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Grafiği oluşturma işlemini gerçekleştirin
if st.button("Grafikleri Oluştur"):
    # Verileri bir veri çerçevesine aktarın
    data = {'Maaş': salaries}
    df = pd.DataFrame(data)
    
    # Aynı maaşı alanları sayın
    maas_sayisi = df['Maaş'].value_counts()
    
    # Grafiği oluşturun
    st.bar_chart(maas_sayisi)

    # Çubukların üzerine değerleri yazdırın
    for i, v in enumerate(maas_sayisi):
        st.text(f"{i}: {v} kişi")
