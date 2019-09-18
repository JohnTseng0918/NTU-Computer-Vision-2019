from PIL import Image
import numpy as np

im=Image.open('lena.bmp')
img = np.asarray(im)
row,col  = img.shape

img.flags.writeable = True

for i in range(row):
    for j in range(i,col):
        img[i][j] , img[j][i] = img[j][i] , img[i][j]

im = Image.fromarray(img)
im.save('lena_diagonal_mirror',format='BMP')