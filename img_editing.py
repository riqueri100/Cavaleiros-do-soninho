from PIL import Image, ImageOps, ImageDraw, ImageFont
from textwrap import wrap

def sepia(img):
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

def make_cite(finput, foutput):
    with Image.open(finput) as user_avatar:
        with Image.open('assets/images/cite_background.jpg') as cite_image:
            box = (100, 100, 600, 600)
            region = sepia(user_avatar.resize((500,500)))
            cite_image.paste(region, box)
            cite_image.save(foutput, "JPEG")

make_cite('fotinha.webp', 'foto_nova.jpg')

def escrita(image_input):
    img = Image.open(image_input)
    fnt = ImageFont.truetype('assets/fonts/ShipporiMincho.ttf', 50)
    d = ImageDraw.Draw(img)
    texto = '\n'.join(wrap('Barack Hussein Obama II (Honolulu, 4 de agosto de 1961) é um advogado e político norte-americano', width=23))
    d.multiline_text((666,100), texto, font=fnt, fill=(255,255,255), align='right')
    return img

escrita('foto_nova.jpg').show()
