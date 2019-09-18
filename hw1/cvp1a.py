from PIL import Image
import numpy as np

im=Image.open('lena.bmp')
img = np.asarray(im)
row,col  = img.shape

img.flags.writeable = True

for i in range(0,row//2):
    for j in range(col):
        img[i][j] , img[row-i-1][j] = img[row-i-1][j] , img[i][j]

im = Image.fromarray(img)
im.save('lena_up_down',format='BMP')