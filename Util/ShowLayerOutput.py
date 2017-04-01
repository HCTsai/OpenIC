import math
import numpy as np
import matplotlib.pyplot as plt
import skimage.io
import skimage.transform
import skimage.filters
import keras
from keras.applications import vgg16
from keras import backend as K
from keras import backend 
from matplotlib.mlab import donothing_callback

#part of visualization
#https://github.com/waleedka/cnn-visualization/blob/master/cnn_visualization.ipynb



    
def apply_mask(image, mask):
    # Resize mask to match image size
    
    img1 = skimage.transform.resize(normalize(mask), image.shape[:,:])
    mask = img1[:,:,np.newaxis].copy()
    # Apply mask to image
    image_heatmap = image * mask
    tensor_summary(image_heatmap)
    display_images([image_heatmap], cols=2)
        
    
def tensor_summary(tensor):
    """Display shape, min, and max values of a tensor."""
    print("shape: {}  min: {}  max: {}".format(tensor.shape, tensor.min(), tensor.max()))

    
def normalize(image):
    """Takes a tensor of 3 dimensions (height, width, colors) and normalizes it's values
    to be between 0 and 1 so it's suitable for displaying as an image."""
    image = image.astype(np.float32)
    return (image - image.min()) / (image.max() - image.min() + 1e-5)


def display_images(images, titles=None, cols=5, interpolation=None, cmap="Greys_r"):
    """
    images: A list of images. I can be either:
        - A list of Numpy arrays. Each array represents an image.
        - A list of lists of Numpy arrays. In this case, the images in
          the inner lists are concatentated to make one image.
    """
   
    titles = titles or [""] * len(images)
    rows = math.ceil(len(images) / cols)
    height_ratio = 1.2 * (rows/cols) * (0.5 if type(images[0]) is not np.ndarray else 1)
    plt.figure(figsize=(11, 11 * height_ratio))
    i = 1
    for image, title in zip(images, titles):
        plt.subplot(rows, cols, i)
        plt.axis("off")
        # Is image a list? If so, merge them into one image.
        if type(image) is not np.ndarray:
            image = [normalize(g) for g in image]
            image = np.concatenate(image, axis=1)
        else:
            image = normalize(image)
        plt.title(title, fontsize=9)
        plt.imshow(image, cmap=cmap, interpolation=interpolation)
        
        i += 1
    plotlist.append(plt)
    #plt.show() 

#image = skimage.io.imread("http://lorempixel.com/224/224/animals/")
#tensor_summary(image)
#display_images([image], cols=1)

from Model import CNN as cnn
model = cnn.get_model('..\\clothes_8_cnn.h5',0)

def read_layer(model, x, layer_name):
    """Return the activation values for the specifid layer"""
    # Create Keras function to read the output of a specific layer
    get_layer_output = K.function([model.layers[0].input], [model.get_layer(layer_name).output])
    
    outputs = get_layer_output([x])[0]
    tensor_summary(outputs)
    return outputs[0]
    
def view_layer(model, x, layer_name, cols=4):
    outputs = read_layer(model, x, layer_name)
    #dimension : filter x, y
    #cmap=plt.cm.Reds, Greys_r
    display_images([outputs[i,:,:] for i in range(16)], cols=cols)    

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np
from Util import config as c
img = load_img('..\\data\\train\\long\\111_a4cd0a60136e439aaea33bf738580e25.jpg', target_size=(c.img_width, c.img_height)) 
x = img_to_array(img)  #
x = x.reshape((1,) + x.shape)  
# 3 x (conv + relu + pooling)
plotlist = [] 
for i in range(6) :
    view_layer(model, x, model.layers[i].name)
    pass
for i in range(6) :
    plotlist[i].show()
    pass

'''
outputs = read_layer(model, x, model.layers[len(model.layers)-3].name)
print outputs
outputs = read_layer(model, x, model.layers[len(model.layers)-2].name)
print outputs
outputs = read_layer(model, x, model.layers[len(model.layers)-1].name)
print outputs
'''

'''  
w = model.layers[0].get_weights()[0]
print w.shape, w.min(), w.max()
display_images([w[i,:,:,::-1] for i in range(16)], cols=16, interpolation="none")
plotlist[0].show()
'''