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

for i in range(64):
    for j in range(64):
        img[i][j]=img[i*8][j*8]
img=img[0:64,0:64]
        
im=Image.fromarray(img)
im.show()