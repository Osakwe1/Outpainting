import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


import matplotlib.pyplot as plt
import matplotlib.image as img



from preprocessing import preprocess


st.title("Outpainting tool")

uploaded_file = st.file_uploader("Upload Image here")
st.image(uploaded_file)

#image_up = uploaded_file.getvalue()
#st.write(image_up)


option = st.selectbox(
    'Which side would you like to outpaint',
    ('Select side', 'left', 'right'))

st.write('You selected:', option)
if option == 'left' or option == 'right':
    preprocessed_image = preprocess(uploaded_file,expand_side=option)
    st.image(preprocessed_image)
