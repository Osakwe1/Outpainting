import streamlit as st
import numpy as np
import pandas as pd


st.title("Outpainting tool")

uploaded_file = st.file_uploader("Upload Image here")
#image_up = uploaded_file.getvalue()
#st.write(image_up)


option = st.selectbox(
    'Which side would you like to outpaint',
    ('Select side', 'Left', 'Right', 'Both'))

st.write('You selected:', option)

