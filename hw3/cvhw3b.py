from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("lena.bmp")
img = np.asarray(im)
row,col  = img.shape

img.flags.writeable = True

for i in range(row):
    for j in range(col):
        img[i][j]=img[i][j]//3

im = Image.fromarray(img)
im.show()
im.save('lena_div3.bmp',format='BMP')
lenaHistogram = np.zeros(256,dtype=np.int32)
for i in range (row):
    for j in range(col):
        tmp = im.getpixel((i,j))
        lenaHistogram[tmp]=lenaHistogram[tmp]+1

a = np.arange(256)
plt.bar(a,lenaHistogram)
plt.savefig("histogram_div3.png",format="png")
plt.show()