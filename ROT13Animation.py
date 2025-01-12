

from cipherFile import *
from tkinter import *
import math

###########################################################################################

def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, 
        fill = "black")

def drawLetterWheel(canvas, data):
    xc, yc, r, gap = data.width//2, data.height//2 - data.spacing, data.r, data.gap
    canvas.create_oval(xc - r, yc - r, xc + r, yc + r, outline = data.stringFill, width = 3)
    canvas.create_oval(xc - r - gap, yc - r - gap, xc + r + gap, yc + r + gap, 
        outline = data.stringFill, width = 3)
    canvas.create_oval(xc - r + gap, yc - r + gap, xc + r - gap, yc + r - gap, 
        outline = data.stringFill, width = 3)
    for i in range(data.lenOfAlphabet):
        degree = data.degree * i
        canvas.create_line(xc, yc, xc + (r+data.gap)*math.cos(degree), yc - 
            (r+data.gap)*math.sin(degree), fill = data.stringFill)
    canvas.create_oval(xc - r + gap, yc - r + gap, xc + r - gap, yc + r - gap, 
        outline = data.stringFill, width = 3, fill = "black")
    degree = 0
    for i in range(data.lenOfAlphabet):
        canvas.create_text(xc + (r+(gap)/2)*math.cos(degree + data.degree/2), 
            yc - (r+(gap)/2)*math.sin(degree + data.degree/2), 
            text = data.alphabetBig[i], fill = data.stringFill)
        canvas.create_text(xc + (r+(gap)/2 - gap)*math.cos(degree + data.degree/2), 
            yc - (r+(gap)/2 - gap)*math.sin(degree + data.degree/2), 
            text = data.alphabet[i], fill = data.stringFill)
        degree += data.degree

def updateAnswerString(data):
    data.answerString = data.answerString[0:data.index] + data.decodedMessage[data.index]
    while len(data.answerString) < len(data.decodedMessage) - 1:
        data.answerString += " "
    return data.answerString

def drawString(canvas, data):
    canvas.create_text(data.width//2, data.height//2 - data.spacing, text = "ROT 13", 
        font = "Courier 40", fill = data.stringFill)
    canvas.create_text(data.width//2, (data.height//2 + data.spacing*(1.5)), 
        text = data.message, font = "Courier 30", 
        fill = data.stringFill)
    canvas.create_text(data.width//2, (data.height//2 + data.spacing*2), 
        text = data.answerString, font = "Courier 30", 
        fill = data.stringFill)
    canvas.create_text(data.width//2, data.height//2 - data.spacing/2, 
        text = data.currShift, font = "Courier 30", fill = data.stringFill)

def drawDial(canvas, data):
    space = 10
    x, y = (data.width//5)*4 + space, (data.height-data.gap*2)//3
    canvas.create_polygon(x, y, x + 20, y - 10, x + 20, y + 10, fill = data.stringFill)

def init(data):
    data.message = ""
    data.encodedMessage = data.message
    data.encodedMessageCopy = data.encodedMessage.upper()
    data.decodedMessage = decodeROT13(data.encodedMessage)
    data.stringFill = "#73f440"
    data.answerString = ""
    data.currShift = 0
    data.wheelIndex = 0
    data.lenOfAlphabet = 26
    data.alphabet = string.ascii_uppercase
    data.alphabetBig = string.ascii_uppercase
    data.r = 125
    data.gap = 25
    data.degree = (2*math.pi)/data.lenOfAlphabet
    data.speed = 3
    data.index = 0
    data.count = 0
    data.spacing = 80
    data.startAnimation = False
    data.animationOver = False

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if data.startAnimation == False:
        if event.char in string.printable:
            data.message += event.char
            data.encodedMessage = data.message
            data.decodedMessage = decodeROT13(data.message)
            data.encodedMessageCopy = data.encodedMessage.upper()
        if event.keysym == "BackSpace":
            data.message = data.message[0:-1]
            data.encodedMessage = data.message
            data.decodedMessage = decodeROT13(data.message)
            data.encodedMessageCopy = data.encodedMessage.upper()
        elif event.keysym == "Return":
            data.startAnimation = True

def timerFired(data):
    data.count += 1
    if data.startAnimation == True:
        if data.index == len(data.decodedMessage):
            data.animationOver = True
            return None
        elif data.count % data.speed == 0:
            if data.currShift < 13:
                data.alphabet =  data.alphabet[1:] + data.alphabet[0]
                data.currShift += 1
            else:
                if data.encodedMessageCopy[data.index] in string.ascii_uppercase:
                    if data.wheelIndex != string.ascii_uppercase.index(data.encodedMessageCopy[data.index]):
                        data.alphabetBig = data.alphabetBig[1:] + data.alphabetBig[0]
                        data.alphabet = data.alphabet[1:] + data.alphabet[0]
                        data.wheelIndex += 1
                    else:
                        updateAnswerString(data)
                        data.wheelIndex = 0
                        data.alphabetBig = string.ascii_uppercase
                        data.alphabet = encodeROT13(string.ascii_uppercase)
                        data.index += 1
                else:
                    updateAnswerString(data)
                    data.wheelIndex = 0
                    data.alphabetBig = string.ascii_uppercase
                    data.alphabet = encodeROT13(string.ascii_uppercase)
                    data.index += 1


def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawLetterWheel(canvas, data)
    drawString(canvas, data)
    if data.animationOver == True:
        canvas.create_text(data.width//2, data.height//2 + (data.spacing*2)+data.spacing/2,
            text = "Done!", font = "Courier 20", fill = data.stringFill)
    drawDial(canvas, data)

###########################################################################################

# Start Citation
# From 112 Website - Animation Section
def runROT13(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

# runROT13(500, 500)
# End Citation