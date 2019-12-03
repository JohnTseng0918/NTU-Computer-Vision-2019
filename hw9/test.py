from PIL import Image
import numpy as np
import math

threshold=24

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


op1=np.array([[-1,-2,-1],
              [0,0,0],
              [1,2,1]])
              
op2=np.array([[-1,0,1],
              [-2,0,2],
              [-1,0,1]])

img=np.pad(img,(0,2),'edge')
mat=np.zeros((row,col),dtype=int)

for i in range(row):
    for j in range(col):
        tmp=img[i:i+3,j:j+3]
        k1=pointwise_product(tmp,op1)
        k2=pointwise_product(tmp,op2)


        mat[i][j]=round(math.sqrt(k1*k1+k2*k2))

        if mat[i][j]>=threshold:
            mat[i][j]=0
        else:
            mat[i][j]=255

im=Image.fromarray(mat)
im.show()
