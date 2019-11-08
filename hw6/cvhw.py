from PIL import Image
import numpy as np

im = Image.open('lena.bmp')
img = np.asarray(im)
row,col=img.shape

img.flags.writeable = True

for i in range(row):
    for j in range(col):
        if img[i][j]>=128:
            img[i][j]=1
        else:
            img[i][j]=0

for i in range(64):
    for j in range(64):
        img[i][j]=img[i*8][j*8]
img=img[0:64,0:64]

table=np.zeros((66,66),dtype=int)
table[1:65,1:65]=img

def h(b,c,d,e):
    if b==c and (d!=b or e!=b): return 'q'
    if b==c and (d==b and e==b): return 'r'
    if b!=c: return 's'

def f(a1,a2,a3,a4):
    if a1=='r' and a2=='r' and a3=='r' and a4=='r': return 5
    count=0
    if a1=='q':count=count+1
    if a2=='q':count=count+1
    if a3=='q':count=count+1
    if a4=='q':count=count+1
    return count

for i in range(1,65,1):
    for j in range(1,65,1):
        if table[i][j]==1:
            x7,x2,x6=table[i-1][j-1],table[i-1][j],table[i-1][j+1]
            x3,x0,x1=table[i][j-1],table[i][j],table[i][j+1]
            x8,x4,x5=table[i+1][j-1],table[i+1][j],table[i+1][j+1]

            a1=h(x0,x1,x6,x2)
            a2=h(x0,x2,x7,x3)
            a3=h(x0,x3,x8,x4)
            a4=h(x0,x4,x5,x1)

            img[i-1][j-1]=f(a1,a2,a3,a4)

f=open("hw6.txt",'w')

for i in range(64):
    for j in range(64):
        if img[i][j]==0:
            print(" ",end='')
            f.write(" ")
        else:
            print(img[i][j],end="")
            f.write(str(img[i][j]))
    print()
    f.write("\n")