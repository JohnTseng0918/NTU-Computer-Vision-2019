from PIL import Image
import numpy as np
import math

threshold=38

im=Image.open('lena.bmp')
img=np.asarray(im)
row,col=img.shape
img.flags.writeable=True

op1=np.array([[-1,-2,-1],
              [0,0,0],
              [1,2,1]])
              
op2=np.array([[-1,0,1],
              [-2,0,2],
              [-1,0,1]])

img=np.pad(img,(1,1),'edge')
mat=np.zeros((row,col),dtype=int)

for i in range(1,row+1):
    for j in range(1,col+1):
        tmp=img[i-1:i+2,j-1:j+2]
        p1=0
        for a in range(3):
            for b in range(3):
                p1+=tmp[a][b]*op1[a][b]
        p2=0
        for a in range(3):
            for b in range(3):
                p2+=tmp[a][b]*op2[a][b]

        mat[i-1][j-1]=round(math.sqrt(p1*p1+p2*p2))
        if mat[i-1][j-1]>=threshold:
            mat[i-1][j-1]=0
        else:
            mat[i-1][j-1]=255


im=Image.fromarray(mat)
im.show()
im=im.convert('L')
im.save('lena_Sobel.bmp',format='BMP')