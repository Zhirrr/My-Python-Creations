from PIL import ImageEnhance,Image,ImageChops 
img = Image.open('cakep.jpg')
Enhancer = ImageEnhance.Color( img )
Cimg = Enhancer.enhance(1.8)
Enhancer = ImageEnhance.Brightness(Cimg)
Cimg = Enhancer.enhance(1.2)
Enhancer = ImageEnhance.Sharpness(Cimg)
Cimg = Enhancer.enhance(1.5)
Cimg.save('/storage/emulated/0/cakepbingits.png')
