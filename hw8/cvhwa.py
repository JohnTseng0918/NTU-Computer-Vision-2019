from PIL import Image
import numpy as np
from SNR import signal_to_noise

im=Image.open('lena.bmp')
img = np.asarray(im)
row,col=img.shape
img_ori=np.zeros((row,col),dtype=int)
img_ori[0:row,0:col]=img[0:row,0:col]

img.flags.writeable = True

img=img+10*np.random.normal(0,1,(row,col))
im=Image.fromarray(img)
im.show()
im=im.convert("L")
im.save('lena_Gaussian10.bmp',format='BMP')
snr=signal_to_noise(img,img_ori)
print(snr)

img[0:row,0:col]=img_ori[0:row,0:col]
img=img+30*np.random.normal(0,1,(row,col))
im=Image.fromarray(img)
im.show()
im=im.convert("L")
im.save('lena_Gaussian30.bmp',format='BMP')
snr=signal_to_noise(img,img_ori)
print(snr)