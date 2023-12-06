from PIL import Image, ImageFilter

img = Image.open('./IMG_1904.CR2')

print(img)
print(img.format)
print(img.size)
print(img.mode)

# filetered_img = img.filter(ImageFilter.SHARPEN)
# filetered_img.save("blured.png",'png')

filetered_img = img.convert('L')
#filetered_img = filetered_img.rotate(45)
#filetered_img.save("grey.png",'png')
filetered_img = filetered_img.resize((518,346))
filetered_img.save("small.png",'png')

