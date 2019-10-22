from PIL import Image
import numpy as np

im=Image.open("lena.bmp")
row,col=im.size

img=np.empty((row,col),dtype=int)
kernel=np.array([[0,1,1,1,0],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,1,1,1,0]])

dilation=np.zeros((row,col),dtype=int)
closing=np.zeros((row,col),dtype=int)


for i in range(row):
    for j in range(col):
        tmp=im.getpixel((i,j))
        if tmp>=128:
            img[i][j]=1
        else:
            img[i][j]=0

for i in range(row):
    for j in range(col):
        if(img[i][j]==1):
            for x in range(-2,3,1):
                if x+i>=512:
                    break
                for y in range(-2,3,1):
                    if j+y>=512:
                        break
                    dilation[i+x][j+y]=1

for i in range(row-4):
    for j in range(col-4):
        tmp=0
        for x in range(5):
            for y in range(5):
                tmp=tmp+kernel[x][y]*dilation[i+x][j+y]
        
        if tmp==21:
            closing[i+2][j+2]=255

closing=closing.transpose()
im=Image.fromarray(closing)
im=im.convert("L")
im.show()
im.save('lena_closing.bmp',format='BMP')