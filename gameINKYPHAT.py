from inky import InkyPHAT

inky_display = InkyPHAT("black")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

questions = [
        ["What sweet food made by bees using nectar from flowers?", "honey"],
        ["Name the school that Harry Potter attended?", "hogwarts"],
        ["Which country is home to the kangaroo?", "australia"],
        ["Which country sent an Armada to attack Britain in 1588?", "spain"],
        ["Saint Patrick is the Patron Saint of which country?", "ireland"],
        ["From what tree do acorns come?", "oak"],
        ["What is the top colour in a rainbow?", "red"],
        ["In the nursery rhyme, who sat on a wall before having a great fall?", "humpty dumpty"],
        ["What is the capital of Germany?", "berlin"],
        ["Where in Scotland is there supposedly a lake monster called Nessie?", "loch ness"] 
]

def title():
    i = 1
    while i < 2:
        img = Image.open("/home/pi/mm/pictures/title1.png")
        inky_display.set_image(img)
        inky_display.show()

        img = Image.open("/home/pi/mm/pictures/title2.png")
        inky_display.set_image(img)
        inky_display.show()
        i += 1

    img = Image.open("/home/pi/mm/pictures/cutscene1.png")
    inky_display.set_image(img)
    inky_display.show()

    img = Image.open("/home/pi/mm/pictures/cutscene2.png")
    inky_display.set_image(img)
    inky_display.show()

    img = Image.open("/home/pi/mm/pictures/intro1.png")
    inky_display.set_image(img)
    inky_display.show()

    img = Image.open("/home/pi/mm/pictures/intro2.png")
    inky_display.set_image(img)
    inky_display.show()

    img = Image.open("/home/pi/mm/pictures/intro3.png")
    inky_display.set_image(img)
    inky_display.show()

    img = Image.open("/home/pi/mm/pictures/skull.png")
    inky_display.set_image(img)
    inky_display.show()
#title()

def game():
    score = 0
    for x in range(len(questions)):
        print(questions[x][0])
        answer = input()
        answer = answer.lower()
        if answer == questions[x][1]:
            score = score+1
            img = Image.open("/home/pi/mm/pictures/correct4.png")
            inky_display.set_image(img)
            inky_display.show()
        else:
           img = Image.open("/home/pi/mm/pictures/fail4.png")
           inky_display.set_image(img)
           inky_display.show()

    if score < 7:
           img = Image.open("/home/pi/mm/pictures/lessthan1.png")
           inky_display.set_image(img)
           inky_display.show()

           img = Image.open("/home/pi/mm/pictures/lessthan2.png")
           inky_display.set_image(img)
           inky_display.show()

           img = Image.open("/home/pi/mm/pictures/youlose.png")
           inky_display.set_image(img)
           inky_display.show()

           retry()
           
    else:
       img = Image.open("/home/pi/mm/pictures/morethan1.png")
       inky_display.set_image(img)
       inky_display.show()

       img = Image.open("/home/pi/mm/pictures/morethan2.png")
       inky_display.set_image(img)
       inky_display.show()

       img = Image.open("/home/pi/mm/pictures/youwin.png")
       inky_display.set_image(img)
       inky_display.show()

       retry()

def retry():
    print("Arr, another try? y/n")
    img = Image.open("/home/pi/mm/pictures/restart.png")
    inky_display.set_image(img)
    inky_display.show()
    retry = input()
    if retry == "y":
       game()
    else:
       exit()

game()

