import streamlit as st
import pandas as pd

with open("hospital_model.pkl", "rb") as f:
  bundle = pickle.load(f)
  st.write("Connected")
