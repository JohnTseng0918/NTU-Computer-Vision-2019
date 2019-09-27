from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("lena_div3.bmp")
#im.show()

img = np.asarray(im)
row,col  = img.shape

img.flags.writeable = True

lenaHistogram = np.zeros(256,dtype=np.int32)
for i in range (row):
    for j in range(col):
        tmp = im.getpixel((i,j))
        lenaHistogram[tmp]=lenaHistogram[tmp]+1

lenaEqualization = np.zeros(256,dtype=np.int32)

lenaEqualization[0]=lenaHistogram[0]
for i in range(1,256,1):
    lenaEqualization[i]=lenaEqualization[i-1]+lenaHistogram[i]
for i in range(256):
    lenaEqualization[i]=round((lenaEqualization[i]*255)/(row*col))
    lenaHistogram[i]=0

for i in range(row):
    for j in range(col):
        img[i][j]=lenaEqualization[img[i][j]]
        lenaHistogram[img[i][j]]=lenaHistogram[img[i][j]]+1

im = Image.fromarray(img)
im.show()
im.save('lena_equalization.bmp',format='BMP')
a = np.arange(256)
plt.bar(a,lenaHistogram)
plt.savefig("histogram_equalization.png",format="png")
plt.show()