from PIL import Image,ImageDraw
import numpy as np

img = Image.open('lena.bmp')
row,col = img.size

imgArray = np.zeros((row+2,col+2),dtype=np.int32)
imgBinary = np.zeros((row,col),dtype=np.int32)

#load image into np_array & 0/1 array
for i in range(row):
    for j in range(col):
        imgArray[i+1][j+1]=img.getpixel((i,j))
        if imgArray[i+1][j+1]>=128:
            imgArray[i+1][j+1]=1
            imgBinary[i][j]=255
        else:
            imgArray[i+1][j+1]=0

imgBinary=imgBinary.transpose()
img2 = Image.fromarray(imgBinary)

#init
labelCount = 1
for i in range(1,row+1,1):
    for j in range(1,col+1,1):
        if imgArray[i][j]==1:
            imgArray[i][j]=labelCount
            labelCount=labelCount+1
np.savetxt("initlabel.csv",imgArray,fmt="%6d")

#iteration method
change = True
it=0
while change == True:
    it=it+1
    change = False
    for i in range(1,row+1,1):
        for j in range(1,col+1,1):
            if imgArray[i][j]!=0:
                tmplist=[imgArray[i][j]]
                if imgArray[i-1][j]!=0:
                    tmplist.append(imgArray[i-1][j])
                if imgArray[i][j-1]!=0:
                    tmplist.append(imgArray[i][j-1])
                if imgArray[i][j+1]!=0:
                    tmplist.append(imgArray[i][j+1])
                if imgArray[i+1][j]!=0:
                    tmplist.append(imgArray[i+1][j])

                if len(tmplist)!=0:
                    tmp=min(tmplist)
                    if tmp!=imgArray[i][j]:
                        change=True
                        imgArray[i][j]=tmp

    for i in range(row+1,0,-1):
        for j in range(col+1,0,-1):
            if imgArray[i][j]!=0:
                tmplist=[imgArray[i][j]]
                
                if imgArray[i-1][j]!=0:
                    tmplist.append(imgArray[i-1][j])
                if imgArray[i][j-1]!=0:
                    tmplist.append(imgArray[i][j-1])
                if imgArray[i][j+1]!=0:
                    tmplist.append(imgArray[i][j+1])
                if imgArray[i+1][j]!=0:
                    tmplist.append(imgArray[i+1][j])

                if len(tmplist)!=0:
                    tmp=min(tmplist)
                    if tmp!=imgArray[i][j]:
                        change=True
                        imgArray[i][j]=tmp
np.savetxt("label.csv",imgArray,fmt="%6d")

#count
#list [label,top,left,down,right,number]
lableList=[]
for i in range(1,row+1,1):
    for j in range(1,col+1,1):
        if imgArray[i][j]!=0:
            if len(lableList)==0:
                lableList.append([imgArray[i][j],i-1,j-1,i-1,j-1,1])
            else:
                isFind=False
                for k in range(len(lableList)):
                    if lableList[k][0]==imgArray[i][j]:
                        isFind=True
                        if lableList[k][1]>i-1:
                            lableList[k][1]=k-1
                        if lableList[k][2]>j-1:
                            lableList[k][2]=j-1
                        if lableList[k][3]<i-1:
                            lableList[k][3]=i-1
                        if lableList[k][4]<j-1:
                            lableList[k][4]=j-1
                        lableList[k][5]=lableList[k][5]+1
                        break
                if isFind==False:
                    lableList.append([imgArray[i][j],i-1,j-1,i-1,j-1,1])


finalList=[]
for i in range(len(lableList)):
    if lableList[i][5]>=500:
        finalList.append([lableList[i][0],lableList[i][1],lableList[i][2],lableList[i][3],lableList[i][4],lableList[i][5]])

img=img.convert("RGBA")
img2 = img2.convert("RGBA")

draw = ImageDraw.Draw(img)
draw2 = ImageDraw.Draw(img2)
for i in range(len(finalList)):
    top = finalList[i][1]
    left = finalList[i][2]
    down = finalList[i][3]
    right = finalList[i][4]
    
    draw.rectangle(((top,left),(down,right)),outline="blue")
    draw.line((((top+down)//2-5,(left+right)//2),((top+down)//2+5,(left+right)//2)),fill="red",width=1)
    draw.line((((top+down)//2,(left+right)//2-5),((top+down)//2,(left+right)//2+5)),fill="red",width=1)

    draw2.rectangle(((top,left),(down,right)),outline="blue")
    draw2.line((((top+down)//2-5,(left+right)//2),((top+down)//2+5,(left+right)//2)),fill="red",width=1)
    draw2.line((((top+down)//2,(left+right)//2-5),((top+down)//2,(left+right)//2+5)),fill="red",width=1)

#img.show()
#img2.show()

img.save('lena_detect.bmp',format='BMP')
img2.save('lena_binary_detect.bmp',format='BMP')