from PIL import Image
import numpy as np

threshold=1

im=Image.open('lena.bmp')
img=np.asarray(im)
row,col=img.shape

mask=np.array([[-1,-3,-4,-6,-7,-8,-7,-6,-4,-3,-1],
               [-3,-5,-8,-11,-13,-13,-13,-11,-8,-5,-3],
               [-4,-8,-12,-16,-17,-17,-17,-16,-12,-8,-4],
               [-6,-11,-16,-16,0,15,0,-16,-16,-11,-6],
               [-7,-13,-17,15,85,160,85,15,-17,-13,-7],
               [-8,-13,-17,15,160,283,160,15,-17,-13,-8],
               [-7,-13,-17,15,85,160,85,15,-17,-13,-7],
               [-6,-11,-16,-16,0,15,0,-16,-16,-11,-6],
               [-4,-8,-12,-16,-17,-17,-17,-16,-12,-8,-4],
               [-3,-5,-8,-11,-13,-13,-13,-11,-8,-5,-3],
               [-1,-3,-4,-6,-7,-8,-7,-6,-4,-3,-1]])

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
            final[i-1][j-1]=0
        else:
            final[i-1][j-1]=255


im=Image.fromarray(final)
im.show()
im=im.convert('L')
im.save('lena_DiffofGau.bmp',format='BMP')
