import os

from PIL import Image, ImageFont, ImageDraw
import win32com.client as win32

def GetContext(Name):
    title_font = ImageFont.truetype('PlayfairDisplay-Italic.ttf',32)
    title_text  = Name

    my_image = Image.open("MerryChristmas.jpg")

    image_editable = ImageDraw.Draw(my_image)

    image_editable.text((460,700), title_text, (255,215,130,255), font=title_font)

    my_image.save("result.jpg")
    html = """\
<html>
    <body>
        <h1>Merry Christmas</h1>
    </body>
</html>


"""
    


    return html


