from PIL import Image
import numpy as np

threshold=15

im=Image.open('lena.bmp')
img=np.asarray(im)
row,col=img.shape
img.flags.writeable=True

mask=np.array([[0,1,0],
               [1,-4,1],
               [0,1,0]])

img=np.pad(img,(1,1),'edge')
mat=np.zeros((row,col),dtype=int)

for i in range(1,row+1):
    for j in range(1,col+1):
        tmp=img[i-1:i+2,j-1:j+2]
        t=0
        for a in range(3):
            for b in range(3):
                t+=tmp[a][b]*mask[a][b]

        if t>=threshold:
            mat[i-1][j-1]=1
        elif t<=-threshold:
            mat[i-1][j-1]=-1
        else:
            mat[i-1][j-1]=0

final=np.zeros((row,col),dtype=int)

mat=np.pad(mat,(1,1),'edge')
for i in range(1,row+1):
    for j in range(1,col+1):
        if mat[i][j]!=1:
            final[i-1][j-1]=255
        else:
            final[i-1][j-1]=0


im=Image.fromarray(final)
im.show()
im=im.convert('L')
im.save('lena_laplace1.bmp',format='BMP')
