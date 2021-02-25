from PIL import Image, ImageOps, PixelAccess

def make_cite(finput, foutput):
    with Image.open(finput) as user_avatar:
        with Image.open('assets/cite_background.jpg') as cite_image:
            box = (100, 100, 600, 600)
            region = user_avatar.resize((500,500))
            cite_image.paste(region, box)
            cite_image.save(foutput, "JPEG")

make_cite('fotinha.webp', 'foto_nova.jpg')

def get_sepia_pixel(red, green, blue, alpha):
    # This is a really popular implementation
    tRed = ((0.759 * red) + (0.398 * green) + (0.194 * blue))
    tGreen = ((0.676 * red) + (0.354 * green) + (0.173 * blue))
    tBlue = ((0.524 * red) + (0.277 * green) + (0.136 * blue))

    # Return sepia color
    return tRed, tGreen, tBlue, alpha


# Convert an image to sepia
def convert_sepia(image):
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = Image.new('RGB', image.size)
    pixels = new.load()

    # Convert each pixel to sepia
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            p = PixelAccess.getpixel(image, i, j)
            pixels[i, j] = get_sepia_pixel(p[0], p[1], p[2], 255)

    # Return new image
    return new

convert_sepia(Image.open('foto_nova.jpg')).show()
