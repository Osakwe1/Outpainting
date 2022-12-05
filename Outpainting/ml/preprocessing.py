import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image


#edit this path once connected to streamlit
path = '/home/krishinipatel/code/krishinipatel/trial_project/mountain_trial.JPG'

#edit this variable name once connected to streamlit dropdown option
expand_side = 'left'
#also need to build in option to have both sides run through the model

def load_image(path):
    image = Image.open(path)
    return image


def resize(image):
    width, height = image.size
    if width == height:
        if width ==256:
            return image
        elif width <256:
            image = image.resize(256,256)
            return image
        elif width >256:
            image = image.resize(256,256)
            return image
    elif width > height:
        rescale_size = height/256
        width_rescaled = width/rescale_size
        image_scaled = image.resize((int(width_rescaled),256))
        return image_scaled
    elif height > width:
        return 'Only accept landscape or sqaure images'

def convert_to_np(image):
    image_np = np.asarray(image)
    if image_np.shape[0] == 256:
        return image_np
    else:
        return 'Error with re-shaping'
    return image_np

def left_right_expand(image):
    if expand_side == 'left':
        image_sliced = image[:,:192,:]
    elif expand_side == 'right':
        width_ = image_np.shape[1] - 192
        image_sliced = image[:,width_:,:]
    return image_sliced

def normalize(image):
    image = image/255
    return image


def masked_image(image):
    mask = np.full((256,64,3),(0))
    if expand_side == 'left':
        image_out = np.concatenate((mask,image),axis=1)
    if expand_side == 'right':
        image_out = np.concatenate((image,mask),axis=1)
    return image_out


def flip_reshape(image):
        if expand_side == 'left':
            image_flipped = np.fliplr(image)

        image_to_predict = image_flipped.reshape((-1,256,256,3))
        return image_to_predict

    image_to_predict = image_flipped.reshape((-1,256,256,3))
    return image_to_predict

def preprocess(path):
'''image_jpg needs to be in the form of a jpg path, limited to landscape and square images'''

    #load image of either landscape or square shape, image is loaded in using Pillow
    image = load_image(path)

    #then resize image to be height 256
    image = resize(image)

    #image is in Pillow object, convert to an np array
    image_np = convert_to_np(image)

    #slicing the image to be the 192 pixel section, if we want a left expand this takes the left side, if we want a right expand this takes the right side
    image_sliced = left_right_expand(image_np)

    #normalize image to be in range from 0 to 1 instead of 0 to 255
    image_norm = normalize(image_sliced)

    #mask image so we create a black mask of 64 pixels wide that our model will predict on
    masked_image = masked_image(image_norm)

    #the model we have built is train on right masks, so if the 'left' option has been selected we need to flip this image horizantally
    #we then also need to add a 4th dimension to the image so it runs in the model, will now be shape(1,256,256,3)
    image_ready = flip_reshape(masked_image)

    #shape of image should now be (1,256,256,3) and ready to predict on
    return np.save("image_to_predict.npy",image_ready)
