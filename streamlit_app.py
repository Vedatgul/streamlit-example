import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Kullanıcıdan müşteri sayısını alın
num_customers = st.number_input("Müşteri Sayısını Girin", min_value=1, step=1)

# Müşterilerin maaşlarını girmek için bir liste oluşturun
salaries = []
for i in range(num_customers):
    salary = st.number_input(f"{i+1}. Müşteri Maaşı", min_value=0, step=1)
    salaries.append(salary)

# Grafik oluşturma işlemini gerçekleştirin
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
