from PIL import Image, ImageFilter

image = Image.open('./astro.jpg')
image.thumbnail((400, 400))
image.save('thumbnail.jpg')
