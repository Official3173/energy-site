from PIL import Image, ImageDraw, ImageFont

#image opening will become dynamic
img = Image.open('3stardryer.png')

#aragon sans bold
#replaces "<Clothes Dryer Model>" & "<Load capacity xx kg"
fnt1 = ImageFont.truetype('Aragon_Sans_Bold.otf', 22)

#this font looks incorrect
#replaces "xxx"
fnt3 = ImageFont.truetype('Aragon_Sans_Bold.otf', 80)

#replaces "<program name> used once per week"
fnt4 = ImageFont.truetype('Aragon_Sans_Bold.otf', 18)

d1 = ImageDraw.Draw(img)
d2 = ImageDraw.Draw(img)
d3 = ImageDraw.Draw(img)
d4 = ImageDraw.Draw(img)


# finds center coordinate for text box by comparing center of image and center of textbox, then subracting to find
# the point at which the image will be centered.

'''
text_size = ImageDraw.Draw.textsize('big ol pp capacity 25kg', font=fnt1) #syntax error on this line
image_width = image.size[0]
x = (image_width / 2) - (text_size[0] / 2)
# x will replace the x coordinate in text(x, y) below.
'''

#COLORS: ORANGE fill = (241, 92, 48); WHITE fill = (255, 255, 255)
d1.text((250, 625), 'Clothes Dryer 3000',        font = fnt1, fill=(241, 92, 48))
d2.text((250, 650), 'big ol pp capacity 25kg', font = fnt1, fill=(241, 92, 48), align="right")
d3.text((280, 745), '366',                       font = fnt3, fill=(255, 255, 255))
d4.text((220, 860), 'program name, we need to figure what this is', font = fnt4, fill=(241, 92, 48))

img.save('test-img.png')
