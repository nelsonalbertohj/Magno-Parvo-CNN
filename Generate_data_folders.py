import matplotlib.image
import tensorflow as tf
import os
import numpy as np

import matplotlib

print("Tensorflow version: ",tf.__version__)

root = "C:/Users/nelso/My Drive (nelsonh@mit.edu)/Vision Dataset"
N_CLASSES = 10
loc = root + f"/Imagenet-{N_CLASSES}-1500-splits/test"
target_loc = "C:/Users/nelso/Desktop" + f"/Imagenet-{N_CLASSES}-1500-splits/test_occluded"

if not os.path.exists(target_loc):
    os.makedirs(target_loc)

size = (224, 224)

stripe_width = 5
stripes_arr = np.array([False for i in range(224)])
for i in range(0,224,stripe_width+10):
  stripes_arr[i:i+stripe_width] = True


folder, dir, file = next(os.walk(loc))
print(folder, dir)
for d in dir:
    sub_f = loc + f"/{d}"
    sub_target_f = target_loc + f"/{d}"
    if not os.path.exists(sub_target_f):
        os.makedirs(sub_target_f)
    _, _, file = next(os.walk(sub_f))
    for f in file:
        if f.endswith("jpg"):
            file_name = f"/{f}"
            img_arr = matplotlib.image.imread(sub_f + file_name) / 255
            if len(img_arr.shape) == 3:
                img_arr = tf.keras.preprocessing.image.smart_resize(img_arr, size)
                img_arr[stripes_arr, :, :] = 0
                img_arr[:, stripes_arr, :] = 0
                matplotlib.image.imsave(sub_target_f + file_name, img_arr)