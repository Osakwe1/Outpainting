import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


def postprocess(image,n_colors):
    if image.ndim == 4:
        image = image[0:,:,:,:]

    image = np.reshape(image,(256*256,3))
    kmeans = KMeans(n_clusters=n_colors,random_state=0).fit(image)
    labels = kmeans.predict(image)
    p = lambda x : kmeans.cluster_centers_[x]
    return p(labels)

# _                 _                            _
#| |               (_)                          | |
#| |     ___  _   _ _ ___  __      ___   _ ____ | |__   ___ _ __ ___
#| |    / _ \| | | | / __| \ \ /\ / / | | |_  / | '_ \ / _ \ '__/ _ \
#| |___| (_) | |_| | \__ \  \ V  V /| |_| |/ /  | | | |  __/ | |  __/
#\_____/\___/ \__,_|_|___/   \_/\_/  \__,_/___| |_| |_|\___|_|  \___|
