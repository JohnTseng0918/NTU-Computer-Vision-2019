from PIL import Image
import numpy as np

threshold=3000

im=Image.open('lena.bmp')
img=np.asarray(im)
row,col=img.shape
img.flags.writeable=True

mask=np.array([[0,0,0,-1,-1,-2,-1,-1,0,0,0],
               [0,0,-2,-4,-8,-9,-8,-4,-2,0,0],
               [0,-2,-7,-15,-22,-23,-22,-15,-7,-2,0],
               [-1,-4,-15,-24,-14,-1,-14,-24,-15,-4,-1],
               [-1,-8,-22,-14,52,103,52,-14,-22,-8,-1],
               [-2,-9,-23,-1,103,178,103,-1,-23,-9,-2],
               [-1,-8,-22,-14,52,103,52,-14,-22,-8,-1],
               [-1,-4,-15,-24,-14,-1,-14,-24,-15,-4,-1],
               [0,-2,-7,-15,-22,-23,-22,-15,-7,-2,0],
               [0,0,-2,-4,-8,-9,-8,-4,-2,0,0],
               [0,0,0,-1,-1,-2,-1,-1,0,0,0]])

img=np.pad(img,(5,5),'edge')
mat=np.zeros((row,col),dtype=int)

for i in range(5,row+5):
    for j in range(5,col+5):
        tmp=img[i-5:i+6,j-5:j+6]
        t=0
        for a in range(11):
            for b in range(11):
                t+=tmp[a][b]*mask[a][b]

        if t>=threshold:
            mat[i-5][j-5]=1
        elif t<=-threshold:
            mat[i-5][j-5]=-1
        else:
            mat[i-5][j-5]=0

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
im.save('lena_Gaulaplace.bmp',format='BMP')
