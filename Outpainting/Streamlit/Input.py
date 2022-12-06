import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


import matplotlib.pyplot as plt
import matplotlib.image as img



from preprocessing import preprocess,resize, convert_to_np
from load_model import load_model
from postprocessing import reduce_colors


st.title("Outpainting tool")

option = None
uploaded_file = st.file_uploader("Upload Image here")
if uploaded_file is not None:
    st.image(uploaded_file)

#image_up = uploaded_file.getvalue()
#st.write(image_up)


    option = st.selectbox(
    'Which side would you like to outpaint',
    ('Select side', 'left', 'right','both sides'))

st.write('You selected:', option)
if option == 'left' or option == 'right':
    preprocessed_image,original_image = preprocess(uploaded_file,expand_side=option)
    #this can be commented out at the end
    #st.image(preprocessed_image)


    model_path_gen_r = '/home/krishinipatel/code/krishinipatel/trial_project/generator (6).h5'
    model_uploaded = load_model(model_path_gen=model_path_gen_r)

    prediction = model_uploaded(preprocessed_image, training = True)

    output = reduce_colors(prediction[0],80).astype(np.uint8)

    if option == 'left':
        output = np.fliplr(output)

        output_full = np.hstack((output[:,:64,:],original_image))

    else:
        output_full = np.hstack((original_image,output[:,192:,:]))


    output_ready = Image.fromarray(output_full)
    output_ready.save('/home/krishinipatel/code/krishinipatel/trial_project/mountain_output.png')
    st.image('/home/krishinipatel/code/krishinipatel/trial_project/mountain_output.png')

    #update these with compute engine paths
    #model_path_dis_r = 'xxx'
    #model_path_gen_r = 'yyy'
    #model_uploaded = load_model(model_path_dis=model_path_dis_r, model_path_gen=model_path_gen_r)

    #model_generator = model_uploaded[0]

    #prediction = model_generator.predict(preprocessed_image)

    #now we need to do post-processing

elif option == 'both sides':
    preprocessed_image_left,original_image = preprocess(uploaded_file,expand_side='left')
    preprocessed_image_right,original_image = preprocess(uploaded_file,expand_side='right')


    model_path_gen_r = '/home/krishinipatel/code/krishinipatel/trial_project/generator (6).h5'
    model_uploaded = load_model(model_path_gen=model_path_gen_r)





    prediction_left = model_uploaded(preprocessed_image_left, training = True)
    prediction_right = model_uploaded(preprocessed_image_right, training = True)

    output_left  = reduce_colors(prediction_left[0] ,80).astype(np.uint8)
    output_right = reduce_colors(prediction_right[0],80).astype(np.uint8)

    output_left = np.fliplr(output_left)

    output_full = np.hstack((output_left[:,:64,:],original_image,output_right[:,192:,:]))

    output_ready = Image.fromarray(output_full)
    output_ready.save('/home/krishinipatel/code/krishinipatel/trial_project/mountain_output.png')
    st.image('/home/krishinipatel/code/krishinipatel/trial_project/mountain_output.png')
