import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


import matplotlib.pyplot as plt
import matplotlib.image as img



from preprocessing import preprocess,resize, convert_to_np
from load_model import load_model
from postprocessing import reduce_colors



def make_image():
    if option == 'left' or option == 'right':
        preprocessed_image,original_image = preprocess(uploaded_file,expand_side=option)
        #this can be commented out at the end
        #st.image(preprocessed_image)



        #col1, col2, col3 = st.columns([1, 5, 1])
        #col2.image(original_image)
        filler = np.full((256,64,3),(255))

        #st.image(image_tdp)

        model_path_gen_r = '/home/krishinipatel/code/krishinipatel/trial_project/generator (6).h5'
        model_uploaded = load_model(model_path_gen=model_path_gen_r)

        prediction = model_uploaded(preprocessed_image, training = True)

        output = reduce_colors(prediction[0],option_colours).astype(np.uint8)

        if option == 'left':

            image_input = np.hstack((filler,original_image))
            output = np.fliplr(output)

            output_full = np.hstack((output[:,:64,:],original_image))

        else:
            image_input = np.hstack((original_image,filler))
            output_full = np.hstack((original_image,output[:,192:,:]))


        with st.spinner('Outpainting...'):
            time.sleep(5)
        st.success('Done!')

        output_ready = Image.fromarray(output_full)
        output_ready.save('output_image.png')


        #col1, col2, col3 = st.columns([1, 5, 1])
        #col2.image('mountain_output.png')
        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image(image_input, width = 600)

        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image('output_image.png', width = 600)




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

        output_left  = reduce_colors(prediction_left[0] ,option_colours).astype(np.uint8)
        output_right = reduce_colors(prediction_right[0],option_colours).astype(np.uint8)

        output_left = np.fliplr(output_left)

        output_full = np.hstack((output_left[:,:64,:],original_image,output_right[:,192:,:]))

        with st.spinner('Outpainting...'):
            time.sleep(5)
        st.success('Done!')


        output_ready = Image.fromarray(output_full)
        output_ready.save('output_image.png')

        #col1, col2, col3 = st.columns([1, 5, 1])
        #col2.image(original_image,width = 400)

        #col1, col2, col3 = st.columns([1, 5, 1])
        #col2.image('mountain_output.png', width = 500)
        filler = np.full((256,64,3),(255))
        image_input = np.hstack((filler, original_image,filler))

        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image(image_input, width = 600)

        col1, col2, col3 = st.columns([1, 5, 1])
        col2.image('output_image.png', width = 600)

        #st.image(image_input)
        #st.image('output_image.png')

    return True

#st.title("OUTPAINTING")

option = None
uploaded_file = st.file_uploader("Upload Image here")
if uploaded_file is not None:
    #st.image(uploaded_file)

#image_up = uploaded_file.getvalue()
#st.write(image_up)


    option = st.selectbox(
    'Which side would you like to outpaint',
    ('Select side', 'left', 'right','both sides'))


    option_colours =  st.slider(
    'Select a range of values for no. of colours', min_value = 5, max_value = 200,value = 80)

    st.write('You selected:', option)
    if option != "Select side":


        if st.button('Run',on_click=make_image):




            #if option == 'left':
             #   image_input = np.hstack((filler, original_image))
            #original_image = preprocess(uploaded_file,expand_side=option)[1]
            #st.title('Outpainting')

            #filler = np.full((256,64,3),(255))
            #if option == 'left':

            #    image_input = np.hstack((filler,original_image))

            #elif option == 'right':
            #    image_input = np.hstack((original_image,filler))

            #else:
              #  image_input = np.hstack((filler,original_image,filler))


            #st.image(image_input)

            #st.image('output_image.png')
            uploaded_file = 'output_image.png'
