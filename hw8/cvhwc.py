from PIL import Image
import numpy as np
from SNR import signal_to_noise

def box33(img):
    row,col=img.shape
    img=np.pad(img,(1,1),'edge')
    box=np.array([[1,1,1],
                  [1,1,1],
                  [1,1,1]])
    coef=1.0/box.sum()
    retMatrix=np.zeros((row,col),dtype=int)
    for i in range(1,row+1,1):
        for j in range(1,col+1,1):
            s=0.0
            for a in range(3):
                for b in range(3):
                    s+=img[i-1+a][j-1+b]*box[a][b]
            retMatrix[i-1][j-1]=s*coef
    return retMatrix

def box55(img):
    row,col=img.shape
    img=np.pad(img,(2,2),'edge')
    box=np.array([[1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1],
                  [1,1,1,1,1]])
    coef=1.0/box.sum()
    retMatrix=np.zeros((row,col),dtype=int)
    for i in range(2,row+2,1):
        for j in range(2,col+2,1):
            s=0.0
            for a in range(5):
                for b in range(5):
                    s+=img[i-2+a][j-2+b]*box[a][b]
            retMatrix[i-2][j-2]=s*coef
    return retMatrix


im=Image.open('lena.bmp')
img = np.asarray(im)

im1=Image.open('lena_Gaussian10.bmp')
im2=Image.open('lena_Gaussian30.bmp')
im3=Image.open('lena_salt_and_pepper0.1.bmp')
im4=Image.open('lena_salt_and_pepper0.05.bmp')

img133=np.asarray(im1)
img155=np.asarray(im1)

img233=np.asarray(im2)
img255=np.asarray(im2)

img333=np.asarray(im3)
img355=np.asarray(im3)

img433=np.asarray(im4)
img455=np.asarray(im4)

tmpImg=box33(img133)
snr=signal_to_noise(tmpImg,img)
print(snr)
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_box33.bmp',format='BMP')

tmpImg=box55(img155)
snr=signal_to_noise(tmpImg,img)
print(snr)
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_box55.bmp',format='BMP')

tmpImg=box33(img233)
snr=signal_to_noise(tmpImg,img)
print(snr)
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_box33.bmp',format='BMP')

tmpImg=box55(img255)
snr=signal_to_noise(tmpImg,img)
print(snr)
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_box55.bmp',format='BMP')

tmpImg=box33(img333)
snr=signal_to_noise(tmpImg,img)
print(snr)
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap0.1_box33.bmp',format='BMP')


tmpImg=box55(img355)
snr=signal_to_noise(tmpImg,img)
print(snr)
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap0.1_box55.bmp',format='BMP')


tmpImg=box33(img433)
snr=signal_to_noise(tmpImg,img)
print(snr)
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap0.0.5_box33.bmp',format='BMP')


tmpImg=box55(img455)
snr=signal_to_noise(tmpImg,img)
print(snr)
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap0.0.5_box55.bmp',format='BMP')