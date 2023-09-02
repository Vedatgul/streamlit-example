import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

num_customers = st.number_input("Müşteri Sayısını Girin", min_value=1, step=1)
