from PIL import Image
import numpy as np
import math

def signal_to_noise(img_noise,img_ori):
    row,col=img_ori.shape

    img_noise=img_noise/255.0
    img_ori=img_ori/255.0 

    n=row*col
    u=np.mean(img_ori)
    vs=0.0
    for i in range(row):
        for j in range(col):
            vs+=(math.pow(img_ori[i][j]-u,2))/n
    

    un=0.0
    for i in range(row):
        for j in range(col):
            un+=(img_noise[i][j]-img_ori[i][j])
    un/=n

    vn=0.0
    for i in range(row):
        for j in range(col):
            vn+=(math.pow(img_noise[i][j]-img_ori[i][j]-un,2))
    vn/=n

    return 20*math.log10(math.sqrt(vs)/math.sqrt(vn))