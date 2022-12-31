from PIL import Image,ImageDraw,ImageFont
#FONT_FILE = ImageFont.truetype("arial.ttf", 50)
#FONT_FILE_o = ImageFont.truetype("arial.ttf", 30)
FONT_COLOR = "#000000"
t1 = Image.open('cert/cert1.png')
WIDTH, HEIGHT = t1.size
#def make_certificates(name,event,date,venue):
def make_certificates1(name,gender,field,desig,design,n1,n2,url1,url2):
    image_source = Image.open('cert/cert1.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name)
    draw.text((762,570), name,fill=FONT_COLOR,font=ImageFont.truetype("Arial.ttf",90))
    gender_width, gender_height = draw.textsize(gender)
    draw.text((1218,849), gender, fill=FONT_COLOR,font=ImageFont.truetype("Arial.ttf",25))
    gender_width, gender_height = draw.textsize(gender)
    draw.text((974,785), gender, fill=FONT_COLOR,font=ImageFont.truetype("Arial.ttf",35))
    field_width, field_height = draw.textsize(field)
    draw.text((579,837), field, fill=FONT_COLOR,font=ImageFont.truetype("Arial.ttf",45))
    desig_width, desig_height = draw.textsize(desig)
    draw.text((520,1191), desig, fill=FONT_COLOR,font=ImageFont.truetype("Arial.ttf",40))
    design_width, design_height = draw.textsize(design)
    draw.text((1322,1197), design, fill=FONT_COLOR,font=ImageFont.truetype("Arial.ttf",40))
    n1_width, n1_height = draw.textsize(n1)
    draw.text((488,1079), n1, fill=FONT_COLOR,font=ImageFont.truetype("Arial.ttf",40))
    n2_width, n2_height = draw.textsize(n2)
    draw.text((1301,1081), n2, fill=FONT_COLOR,font=ImageFont.truetype("Arial.ttf",40))
    #event_width, event_height = draw.textsize(event)
    #draw.text((568,938), event, fill=FONT_COLOR)
    #date_width, date_height = draw.textsize(date)
    #draw.text((948,930), date, fill=FONT_COLOR)
    #venue_width, venue_height = draw.textsize(venue)
    #draw.text((1238,930), venue, fill=FONT_COLOR)
    #image_source.save("./out/" + name +".png")
    #print('Saving Certificate of:', name)

    insert_image1 = Image.open(url1)
    insert_image2 = Image.open(url2)

    width1, height1 = insert_image1.size
    width2, height2 = insert_image2.size
    x = width1/height1
    y = width2/height2
    if x <= 1.5 and y <= 1.5:
        insert_image1 = insert_image1.resize((250,75))
        insert_image2 = insert_image2.resize((250,75))
        image_source.paste(insert_image1, (453,994))
        image_source.paste(insert_image2, (1269,994))
    else:
        insert_image1 = insert_image1.resize((350,75))
        insert_image2 = insert_image2.resize((350,75))
        image_source.paste(insert_image1, (453,994))
        image_source.paste(insert_image2, (1269,994))

    image_source.show()

if __name__ == "__main__":
    names = ["Soham Chakraborty", "Kaustav Giri", "Pritha Saha","Ujjaini Ray"]
    #event = "Devfest Kolkata 2023"
    #date = "28.12.2022"
    #venue = "Taal Kutir Convention"
    field = "Robotics"
    gender = "his/her"
    desig = "Principal"
    design = "Student Head"
    n1 = "Mitra Basu"
    n2 = "P. K. Dan"
    url1 = "signs/sig1.png"
    url2 = "signs/sig2.png"
    for name in names:
        #make_certificates(name,event,date,venue)
        make_certificates1(name,gender,field,desig,design,n1,n2,url1,url2)
    print(len(names), "certificates done.")