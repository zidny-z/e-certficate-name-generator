# import pillow
from PIL import Image, ImageFont, ImageDraw

gambar = Image.open("PESERTA.jpg")
draw = ImageDraw.Draw(gambar)

fontnya = ImageFont.truetype("Viga-Regular.ttf", size=100)
(x, y) = (540,1045)
isi = str(input('Masukkan nama :'))
colornya = "rgb(0,0,0)"
draw.text((x,y), isi, fill=colornya, font=fontnya)

gambar.save(isi+".jpg")


print("Done")