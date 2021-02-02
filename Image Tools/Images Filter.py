from PIL import Image, ImageFilter
img = Image.open('cakep.jpg')
enc_img = img.filter(ImageFilter.DETAIL)
enc_img.show()
