from PIL import Image
import numpy as np

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
im.show()

labelTable = np.zeros((row,col),dtype=np.int8)