import streamlit as st
import math 
st.title("Menghitung :volume Tabung buatan andre&Dino[cool] :rocket:")


r = st.number_input("Masukan Jari_Jari (cm): ",0)
t = st.number_input("Masukan Tinggi (cm): ",0)

if st.button("Hitung Volume", type="primary"):
  v = math.pi*(r**2)*t
  St.success(f'Volume Tabung adalah {v:2f}')
