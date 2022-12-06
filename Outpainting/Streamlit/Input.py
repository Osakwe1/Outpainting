import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


import matplotlib.pyplot as plt
import matplotlib.image as img



from preprocessing import preprocess
from load_model import load_model


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
    #this can be commented out at the end
    st.image(preprocessed_image)

    #update these with compute engine paths
    model_path_dis_r = 'xxx'
    model_path_gen_r = 'yyy'
    model_uploaded = load_model(model_path_dis=model_path_dis_r, model_path_gen=model_path_gen_r)

    model_generator = model_uploaded[0]

    prediction = model_generator.predict(preprocessed_image)

    #now we need to do post-processing
