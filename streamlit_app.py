import streamlit as st
import pandas as pd

# Kullanıcıdan müşteri sayısını alın
num_customers = st.number_input("Müşteri Sayısını Girin", min_value=1, step=1)

# Müşterilerin maaşlarını girmek için bir liste oluşturun
salaries = []
for i in range(num_customers):
    salary = st.number_input(f"{i+1}. Müşteri Maaşı", min_value=0, step=1)
    salaries.append(salary)

# Grafiği oluşturma işlemini gerçekleştirin
if st.button("Grafikleri Oluştur"):
    # Verileri bir veri çerçevesine aktarın
    data = {'Maaş': salaries}
    df = pd.DataFrame(data)
    
    # Aynı maaşı alanları sayın
    maas_sayisi = df['Maaş'].value_counts()
    
    # Çubuk grafik verisini hazırlayın
    bar_chart_data = pd.DataFrame({'Maaş': maas_sayisi.index, 'Kişi Sayısı': maas_sayisi.values})

    # Streamlit'te grafiği oluşturun
    st.write("Aynı Maaşı Alan Müşteri Sayısı")
    st.dataframe(bar_chart_data)

    # Çubuk grafik olarak gösterin
    st.bar_chart(bar_chart_data.set_index('Maaş'))
