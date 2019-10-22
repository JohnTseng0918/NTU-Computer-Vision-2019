from PIL import Image
import numpy as np

im=Image.open("lena.bmp")
row,col=im.size

img=np.empty((row,col),dtype=int)
img_c=np.empty((row,col),dtype=int)
J=np.array([[0,0,0],
            [1,1,0],
            [0,1,0]])

K=np.array([[0,1,1],
            [0,0,1],
            [0,0,0]])

for i in range(row):
    for j in range(col):
        tmp=im.getpixel((i,j))
        if tmp>=128:
            img[i][j]=1
            img_c[i][j]=0
        else:
            img[i][j]=0
            img_c[i][j]=1

AJ=np.zeros((row,col),dtype=int)
ACK=np.zeros((row,col),dtype=int)

for i in range(row-2):
    for j in range(col-2):
        tmp=0
        for x in range(3):
            for y in range(3):
                tmp=tmp+J[x][y]*img[i+x][j+y]
        
        if tmp==3:
            AJ[i+1][j+1]=1

for i in range(row-2):
    for j in range(col-2):
        tmp=0
        for x in range(3):
            for y in range(3):
                tmp=tmp+K[x][y]*img_c[i+x][j+y]
        
        if tmp==3:
            ACK[i+1][j+1]=1

HitAndMiss=np.zeros((row,col),dtype=int)

for i in range(row):
    for j in range(col):
        if AJ[i][j]==1 and ACK[i][j]==1:
            HitAndMiss[i][j]=255

HitAndMiss=HitAndMiss.transpose()
im=Image.fromarray(HitAndMiss)
im=im.convert("L")
im.show()
im.save('lena_HitAndMiss.bmp',format='BMP')