
from tkinter import *
from cipherFile import *

################################################################################

# decode
 
def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, 
        fill = "black")

def updateAnswerString(data):
    data.answerString = data.answerString[0:data.index] + data.encodedMessage[data.index]
    while len(data.answerString) < len(data.encodedMessage) - 1:
        data.answerString += " "
    return data.answerString

def drawString(canvas, data):
    canvas.create_text(data.width//2, data.spacing, text = "Encrypt Vigenere Cipher", 
        font = "Courier 40", fill = data.stringFill)
    canvas.create_text(data.width//2, data.height//2 + data.spacing*7,
        text = data.message, font = "Courier 30",
        fill = data.stringFill)
    canvas.create_text(data.width//2, data.height//2 + data.spacing*6,
        text = ("Keyword: %s") % (data.keyword), font = "Courier 30",
        fill = data.stringFill)
    canvas.create_text(data.width//2, data.height//2 + data.spacing*8,
        text = data.answerString, font = "Courier 30",
        fill = data.stringFill)

def drawAlphabetGrid(canvas, data):
    for row in range(data.lenOfAlphabet+1):
        for col in range(data.lenOfAlphabet+1):
            box = data.boxWidth
            canvas.create_rectangle(box*row + data.margin, box*col + data.spacing * 2, 
                box*(row+1) + data.margin, box*(col+1) + data.spacing * 2,
                outline = data.stringFill)

def fillAlphabetGrid(canvas, data):
    box = data.boxWidth
    space = data.spacing * 2
    alphabet = string.ascii_uppercase
    index = 0
    for row in range(data.lenOfAlphabet):
        canvas.create_text(box*(row+1) + box/2 + data.margin, box/2 + space, 
            text = alphabet[index], fill = data.stringFill)
        index += 1
    index = 0
    for col in range(data.lenOfAlphabet):
        canvas.create_text(box/2 + data.margin, box*(col+1) + box/2 + space, 
            text = alphabet[index], fill = data.stringFill)
        index += 1
    index = 0
    for row in range(data.lenOfAlphabet):
        for col in range(data.lenOfAlphabet):
            canvas.create_text(box*(row+1) + data.margin + box/2, box*(col+1) + box/2 + space, 
                text = alphabet[index], fill = data.stringFill)
            index += 1
            if index == 26:
                alphabet = alphabet[1:] + alphabet[0]
            index = (index % len(alphabet))

def highlightGridRowColBox(canvas, data):
    # col
    x0 = data.boxWidth*(data.highlightCol+1)
    space = data.spacing * 2
    numOfBoxes = 27
    canvas.create_rectangle(x0 + data.margin, space, x0+data.boxWidth 
        + data.margin, data.boxWidth*numOfBoxes + space, fill = "blue")
    # row
    y0 = data.boxWidth*(data.highlightRow+1)
    canvas.create_rectangle(data.margin, y0 + space, data.boxWidth*numOfBoxes 
        + data.margin, y0 + data.boxWidth + space, fill = "blue")
    # block
    canvas.create_rectangle(x0 + data.margin, y0 + space, x0+data.boxWidth 
        + data.margin, y0 + data.boxWidth + space, fill = "white")

def init(data):
    data.message = ""
    data.keyword = ""
    data.decodedMessage = data.message
    data.encodedMessage = encodeVigenere(data.message, data.keyword)
    data.lenOfAlphabet = 26
    data.stringFill = "#73f440"
    data.speed = 1 # A higher speed actually makes the animation slower
    data.count = 0
    data.index = 0
    data.spacing = 40
    data.animationOver = False
    data.answerString = ""
    data.startAnimation = 0
    data.gridWidth = 500
    data.boxWidth = (data.gridWidth)/(data.lenOfAlphabet + 1)
    data.highlightRow = 0
    data.highlightCol = 0
    data.margin = margin = (data.width - data.gridWidth)/2

def keyPressed(event, data):
    if data.startAnimation == 0:
        if event.keysym in string.ascii_lowercase + string.ascii_uppercase:
            data.keyword += event.keysym
        if event.keysym == "space":
            data.keyword += " "
        if event.keysym == "BackSpace":
            data.keyword = data.keyword[0:-1]
        data.decodedMessage = data.message
        data.encodedMessage = encodeVigenere(data.decodedMessage, data.keyword)
        if event.keysym == "Return":
            data.startAnimation += 1
    elif data.startAnimation == 1:
        if event.char in string.printable:
            data.message += event.char
        if event.keysym == "BackSpace":
            data.message = data.message[0:-1]
        data.decodedMessage = data.message
        data.encodedMessage = encodeVigenere(data.decodedMessage, data.keyword)
        if event.keysym == "Return":
            data.startAnimation += 1

def mousePressed(event, data):
    pass

def timerFired(data):
    if data.startAnimation == 2 and data.animationOver == False:
        if data.index == len(data.decodedMessage): data.animationOver = True
        if data.animationOver == False:
            data.count += 1
            if data.count % data.speed == 0:
                data.messageCopy = data.message.lower()
                data.keywordCopy = createVigenereKeywordString(data.message, data.keyword)
                if data.messageCopy[data.index] in string.ascii_lowercase:
                    if data.highlightCol != string.ascii_lowercase.index(data.keywordCopy[data.index]):
                        data.highlightCol += 1
                    elif (data.highlightRow)%data.lenOfAlphabet \
                    != string.ascii_lowercase.index(data.messageCopy[data.index]):
                        data.highlightRow += 1
                    else:
                        updateAnswerString(data)
                        data.index += 1
                        data.highlightCol, data.highlightRow = 0, 0
                else:
                    updateAnswerString(data)
                    data.index += 1
                    data.highlightCol, data.highlightRow = 0, 0

def redrawAll(canvas, data):
    drawBackground(canvas, data)
    highlightGridRowColBox(canvas, data)
    drawAlphabetGrid(canvas, data)
    fillAlphabetGrid(canvas, data)
    drawString(canvas, data)
    if data.animationOver == True:
        canvas.create_text(data.width//2, data.height//2 + data.spacing*9,
            text = "Done!", font = "Courier 20",
            fill = data.stringFill)

################################################################################

# Start Citation
# From 112 Website - Animation Section
def runEncryptVigenere(width=300, height=300):
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

# runEncryptVigenere(750, 750)
# End Citation