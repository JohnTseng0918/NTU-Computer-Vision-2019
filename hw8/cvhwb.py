from PIL import Image
import numpy as np
from SNR import signal_to_noise

im=Image.open('lena.bmp')
img = np.asarray(im)
row,col=img.shape
img_ori=np.zeros((row,col),dtype=int)
img_ori[0:row,0:col]=img[0:row,0:col]

img.flags.writeable = True

noise = np.random.uniform(0.0,1.0,(row,col))

for i in range(row):
    for j in range(col):
        if noise[i][j]>0.95:
            img[i][j]=255
        elif noise[i][j]<0.05:
            img[i][j]=0

snr=signal_to_noise(img,img_ori)
print(snr)

im=Image.fromarray(img)
im.show()
im=im.convert("L")
im.save('lena_salt_and_pepper0.05.bmp',format='BMP')

img[0:row,0:col]=img_ori[0:row,0:col]

noise = np.random.uniform(0.0,1.0,(row,col))

for i in range(row):
    for j in range(col):
        if noise[i][j]>0.9:
            img[i][j]=255
        elif noise[i][j]<0.1:
            img[i][j]=0

snr=signal_to_noise(img,img_ori)
print(snr)

im=Image.fromarray(img)
im.show()
im=im.convert("L")
im.save('lena_salt_and_pepper0.1.bmp',format='BMP')