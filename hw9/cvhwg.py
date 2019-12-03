from PIL import Image
import numpy as np
import math

threshold=12500

im=Image.open('lena.bmp')
img=np.asarray(im)
row,col=img.shape
img.flags.writeable=True

def pointwise_product(a,b):
    t=0
    for i in range(5):
        for j in range(5):
            t+=a[i][j]*b[i][j]
    return t


op0=np.array([[100,100,100,100,100],
              [100,100,100,100,100],
              [0,0,0,0,0],
              [-100,-100,-100,-100,-100],
              [-100,-100,-100,-100,-100]])
              
op60=np.array([[100,100,100,32,-100],
               [100,100,92,-78,-100],
               [100,100,0,-100,-100],
               [100,78,-92,-100,-100],
               [100,-32,-100,-100,-100]])

op60neg=np.array([[-100,32,100,100,100],
                  [-100,-78,92,100,100],
                  [-100,-100,0,100,100],
                  [-100,-100,-92,78,100],
                  [-100,-100,-100,-32,100]])

op30=np.array([[100,100,100,100,100],
               [100,100,100,78,-32],
               [100,92,0,-92,-100],
               [32,-78,-100,-100,-100],
               [-100,-100,-100,-100,-100]])

op90neg=np.array([[-100,-100,0,100,100],
                  [-100,-100,0,100,100],
                  [-100,-100,0,100,100],
                  [-100,-100,0,100,100],
                  [-100,-100,0,100,100]])

op30neg=np.array([[100,100,100,100,100],
                  [-32,78,100,100,100],
                  [-100,-92,0,92,100],
                  [-100,-100,-100,-78,32],
                  [-100,-100,-100,-100,-100]])

img=np.pad(img,(2,2),'edge')
mat=np.zeros((row,col),dtype=int)

for i in range(2,row+2):
    for j in range(2,col+2):
        tmp=img[i-2:i+3,j-2:j+3]
        k1=pointwise_product(tmp,op0)
        k2=pointwise_product(tmp,op30)
        k3=pointwise_product(tmp,op30neg)
        k4=pointwise_product(tmp,op60)
        k5=pointwise_product(tmp,op60neg)
        k6=pointwise_product(tmp,op90neg)


        mat[i-2][j-2]=max(k1,k2,k3,k4,k5,k6)

        if mat[i-2][j-2]>=threshold:
            mat[i-2][j-2]=0
        else:
            mat[i-2][j-2]=255

im=Image.fromarray(mat)
im.show()
im=im.convert('L')
im.save('lena_Nevatia-Babu.bmp',format='BMP')