from PIL import Image
im = Image.open('lena.bmp')
out = im.resize((256, 256))
out.save('lena_shrink',format='BMP')