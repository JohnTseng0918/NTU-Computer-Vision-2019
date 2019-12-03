from PIL import Image
import numpy as np
import math

threshold=135

im=Image.open('lena.bmp')
img=np.asarray(im)
row,col=img.shape
img.flags.writeable=True

def pointwise_product(a,b):
    t=0
    for i in range(3):
        for j in range(3):
            t+=a[i][j]*b[i][j]
    return t


op1=np.array([[-3,-3,5],
              [-3,0,5],
              [-3,-3,5]])
              
op2=np.array([[-3,5,5],
              [-3,0,5],
              [-3,-3,-3]])

op3=np.array([[5,5,5],
              [-3,0,-3],
              [-3,-3,-3]])

op4=np.array([[5,5,-3],
              [5,0,-3],
              [-3,-3,-3]])

op5=np.array([[5,-3,-3],
              [5,0,-3],
              [5,-3,-3]])

op6=np.array([[-3,-3,-3],
              [5,0,-3],
              [5,5,-3]])

op7=np.array([[-3,-3,-3],
              [-3,0,-3],
              [5,5,5]])

op8=np.array([[-3,-3,-3],
              [-3,0,5],
              [-3,5,5]])

img=np.pad(img,(1,1),'edge')
mat=np.zeros((row,col),dtype=int)

for i in range(1,row+1):
    for j in range(1,col+1):
        tmp=img[i-1:i+2,j-1:j+2]
        k1=pointwise_product(tmp,op1)
        k2=pointwise_product(tmp,op2)
        k3=pointwise_product(tmp,op3)
        k4=pointwise_product(tmp,op4)
        k5=pointwise_product(tmp,op5)
        k6=pointwise_product(tmp,op6)
        k7=pointwise_product(tmp,op7)
        k8=pointwise_product(tmp,op8)

        mat[i-1][j-1]=max(k1,k2,k3,k4,k5,k6,k7,k8)

        if mat[i-1][j-1]>=threshold:
            mat[i-1][j-1]=0
        else:
            mat[i-1][j-1]=255

im=Image.fromarray(mat)
im.show()
im=im.convert('L')
im.save('lena_Kirsch.bmp',format='BMP')