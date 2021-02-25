from PIL import Image

def make_cite(finput, foutput):
    with Image.open(finput) as user_avatar:
        with Image.open('assets/cite_background.jpg') as cite_image:
            box = (100, 100, 600, 600)
            region = user_avatar.resize((500,500))
            cite_image.paste(region, box)
            cite_image.save(foutput, "JPEG")

#make_cite('fotinha.webp', 'foto_nova.jpg')
