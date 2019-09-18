from PIL import Image
import numpy as np

def binarize(x):
    if x >=128:
        x = 255
    else:
        x = 0
    return x

im = Image.open('lena.bmp')
img = np.asarray(im)
row,col=img.shape

img.flags.writeable = True

for i in range(row):
    for j in range(col):
        if img[i][j]>=128:
            img[i][j]=255
        else:
            img[i][j]=0

im=Image.fromarray(img)
im.save('lena_binarize',format='BMP')