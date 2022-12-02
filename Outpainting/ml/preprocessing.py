import numpy as np
from sklearn.pipeline import make_pipeline

image_size = 256
image_size = 256
def preprocess(image_jpg):
'''image_jpg needs to be in the form of a jpg path'''
    image = img.imread(image_jpg)



    width, height = image.size

    if width == height:
        image = image.reshape(image_size,image_size,3)
    else:
        size_temp = min(width,height)
        left = width -(width-size_temp)/2
        top = height - (height-size_temp)/2
        right = width - (width-size_temp)/2
        bottom = height - (height-size_temp)/2

        image = image.crop((left, top, right, bottom))
        image = image.reshape(image_size,image_size,3)



    image_scaled = image/255

    image_np = np.asarray(image_scaled)
    return np.save("image_test.npy",image_np)
