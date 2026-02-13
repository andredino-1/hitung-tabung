import streamlit as st
import math 
st.title("Menghitung :blue[volume Tabung buatan andre&Dino] :rocket:")


r = st.number_input("Masukan Jari_Jari (cm): ",0)
t = st.number_input("Masukan Tinggi (cm): ",0)

if st.button("Hitung Volume", type="primary"):
  loading = st.progres(0)
  for i in range(100):
    time.sleep(0.01)
    loading.progres(i+1)

  v = math.pi*(r**2)*t
  St.success(f'Volume Tabung adalah {v:2f}')
