from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("lena.bmp")
#im.show()

row,col = im.size
lenaHistogram = np.zeros(256,dtype=np.int32)
for i in range (row):
    for j in range(col):
        tmp = im.getpixel((i,j))
        lenaHistogram[tmp]=lenaHistogram[tmp]+1

a = np.arange(256)
plt.bar(a,lenaHistogram)
plt.savefig("histogram.png",format="png")
plt.show()