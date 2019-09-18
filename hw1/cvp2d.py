from PIL import Image
im = Image.open('lena.bmp')
out=im.rotate(-45)
out.save('lena_rotate',format='BMP')