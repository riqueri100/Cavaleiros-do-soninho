from PIL import Image, ImageOps

def make_cite(finput, foutput):
    with Image.open(finput) as user_avatar:
        with Image.open('assets/cite_background.jpg') as cite_image:
            box = (100, 100, 600, 600)
            region = user_avatar.resize((500,500))
            cite_image.paste(region, box)
            cite_image.save(foutput, "JPEG")

#make_cite('fotinha.webp', 'foto_nova.jpg')


def sepia(image_path):
    img = Image.open(image_path)
    width, height = img.size

    pixels = img.load() # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            pixels[px, py] = (tr,tg,tb)

    return img
#sepia('foto_nova.jpg').show()
