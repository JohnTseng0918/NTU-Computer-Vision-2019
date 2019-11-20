from PIL import Image
import numpy as np
from SNR import signal_to_noise

def dilation(img):
    kernel=np.array([[0,1,1,1,0],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [0,1,1,1,0]])
    row,col=img.shape
    retImg=np.zeros((row,col),dtype=int)
    for i in range(row):
        for j in range(col):
            tmp=img[i][j]
            for x in range(-2,3,1):
                if x+i>=512:
                    break
                for y in range(-2,3,1):
                    if j+y>=512:
                        break
                    if kernel[x+2][y+2]==1 and img[x+i][y+j]>tmp:
                        tmp=img[x+i][y+j]
            retImg[i][j]=tmp
    return retImg

def erosion(img):
    kernel=np.array([[0,1,1,1,0],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [0,1,1,1,0]])
    row,col=img.shape
    retImg=np.zeros((row,col),dtype=int)
    for i in range(row):
        for j in range(col):
            tmp=img[i][j]
            for x in range(-2,3,1):
                if x+i>=512:
                    break
                for y in range(-2,3,1):
                    if j+y>=512:
                        break
                    if kernel[x+2][y+2]==1 and img[x+i][y+j]<tmp:
                        tmp=img[x+i][y+j]
            retImg[i][j]=tmp
    return retImg

def opening(img):
    return dilation(erosion(img))

def closing(img):
    return erosion(dilation(img))


im=Image.open('lena.bmp')
img = np.asarray(im)

im1=Image.open('lena_Gaussian10.bmp')
im2=Image.open('lena_Gaussian30.bmp')
im3=Image.open('lena_salt_and_pepper0.1.bmp')
im4=Image.open('lena_salt_and_pepper0.05.bmp')

img1oc=np.asarray(im1)
img1co=np.asarray(im1)

img2oc=np.asarray(im2)
img2co=np.asarray(im2)

img3oc=np.asarray(im3)
img3co=np.asarray(im3)

img4oc=np.asarray(im4)
img4co=np.asarray(im4)

tmpImg=opening(closing(img1oc))
snr=signal_to_noise(tmpImg,img)
print(snr)
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_closing_opening.bmp',format='BMP')

tmpImg=closing(opening(img1co))
snr=signal_to_noise(tmpImg,img)
print(snr)
im1=Image.fromarray(tmpImg)
im1.show()
im1=im1.convert("L")
im1.save('lena_gauss10_opening_closing.bmp',format='BMP')

tmpImg=opening(closing(img2oc))
snr=signal_to_noise(tmpImg,img)
print(snr)
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_closing_opening.bmp',format='BMP')

tmpImg=closing(opening(img2co))
snr=signal_to_noise(tmpImg,img)
print(snr)
im2=Image.fromarray(tmpImg)
im2.show()
im2=im2.convert("L")
im2.save('lena_gauss30_opening_closing.bmp',format='BMP')

tmpImg=opening(closing(img3oc))
snr=signal_to_noise(tmpImg,img)
print(snr)
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap0.1_closing_opening.bmp',format='BMP')


tmpImg=closing(opening(img3co))
snr=signal_to_noise(tmpImg,img)
print(snr)
im3=Image.fromarray(tmpImg)
im3.show()
im3=im3.convert("L")
im3.save('lena_sap0.1_opening_closing.bmp',format='BMP')


tmpImg=opening(closing(img4oc))
snr=signal_to_noise(tmpImg,img)
print(snr)
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap0.05_closing_opening.bmp',format='BMP')


tmpImg=closing(opening(img4co))
snr=signal_to_noise(tmpImg,img)
print(snr)
im4=Image.fromarray(tmpImg)
im4.show()
im4=im4.convert("L")
im4.save('lena_sap0.05_opening_closing.bmp',format='BMP')