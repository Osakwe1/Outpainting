import numpy as np
import pandas as pd
from PIL import Image


import matplotlib.pyplot as plt
import matplotlib.image as img



from preprocessing import preprocess
from load_model import load_model
from postprocessing import postprocess

path = '/home/krishinipatel/code/krishinipatel/trial_project/mountain_trial.JPG'

expand_side = 'right'

preprocessed_image = preprocess(path,expand_side)
#print(preprocessed_image.shape)

#test = Image.fromarray(((preprocessed_image[0,:,:,:])*256).astype(np.uint8))

#test.save('/home/krishinipatel/code/krishinipatel/trial_project/mountain_test.jpg')

#this can be commented out at the end
#st.image(preprocessed_image)

#update these with compute engine paths

#model_path_dis_r = 'xxx'
model_path_gen_r = '/home/krishinipatel/code/krishinipatel/trial_project/generator (3).h5'
model_uploaded = load_model(model_path_gen=model_path_gen_r)


prediction = model_uploaded.predict(preprocessed_image)

#print(prediction.shape)

test = Image.fromarray(((prediction[0,:,:,:])*256).astype(np.uint8))

test.save('/home/krishinipatel/code/krishinipatel/trial_project/mountain_predict.jpg')

#now we need to do post-processing
output = postprocess(prediction,80).astype(np.uint8)
#print(output.shape)
output_ready = Image.fromarray(output)
output_ready.save('/home/krishinipatel/code/krishinipatel/trial_project/mountain_output.jpg')

#print(output_ready)
