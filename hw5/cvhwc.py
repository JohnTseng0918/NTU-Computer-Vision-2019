from PIL import Image
import numpy as np

im=Image.open("lena.bmp")
row,col=im.size

img=np.asarray(im)
img.flags.writeable = True
kernel=np.array([[0,1,1,1,0],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,1,1,1,0]])

erosion=np.zeros((row,col),dtype=int)
opening=np.zeros((row,col),dtype=int)

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
        erosion[i][j]=tmp

for i in range(row):
    for j in range(col):
        tmp=erosion[i][j]
        for x in range(-2,3,1):
            if x+i>=512:
                break
            for y in range(-2,3,1):
                if j+y>=512:
                    break
                if kernel[x+2][y+2]==1 and erosion[x+i][y+j]>tmp:
                    tmp=erosion[x+i][y+j]
        opening[i][j]=tmp

im=Image.fromarray(opening)
im=im.convert("L")
im.show()
im.save('lena_opening.bmp',format='BMP')