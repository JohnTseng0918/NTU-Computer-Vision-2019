from PIL import Image
import numpy as np

im=Image.open('lena.bmp')
img = np.asarray(im)
row,col  = img.shape

img.flags.writeable = True

for i in range(row):
    for j in range(0,col//2):
        img[i][j] , img[i][col-j-1] = img[i][col-j-1] , img[i][j]

im = Image.fromarray(img)
im.save('lena_right_left',format='BMP')