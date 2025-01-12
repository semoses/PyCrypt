
from cipherFile import *
from tkinter import *

################################################################################

def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, 
        fill = data.backgroundFill)

def drawString(canvas, data):
    alphabet = string.ascii_uppercase
    index = 0
    canvas.create_text(data.width//2, data.spacing, text = "Decrypt Keyword", 
        font = "Courier 40", fill = data.stringFill)
    width = (data.width - 6)/data.lenOfAlphabet
    for col in range(data.lenOfAlphabet):
        x0, y0 = width*col + 3, data.width//3 + width
        x1, y1 = x0 + width, y0 + width
        canvas.create_rectangle(x0, y0, x1, y1, outline = data.stringFill)
        canvas.create_text(x0 + width/2, y0 + width/2, 
            text = alphabet[index], 
            font = "Courier 15", fill = data.stringFill)
        index += 1
    index = 0
    data.alphabet = updateAlphabet(data)
    for col in range(data.lenOfAlphabet):
        x0, y0 = width*col + 3, data.width//3
        x1, y1 = x0 + width, y0 + width
        canvas.create_rectangle(x0, y0, x1, y1, outline = data.stringFill)
        canvas.create_text(x0 + width/2, y0 + width/2, 
            text = data.alphabet[index], 
            font = "Courier 15", fill = data.stringFill)
        index += 1
    canvas.create_text(data.width//2, data.spacing*8,
        text = data.message, font = "Courier 30",
        fill = data.stringFill)
    canvas.create_text(data.width//2, data.height//2 + (data.spacing/2),
        text = "Keyword: %s" % data.keyword, font = "Courier 30",
        fill = data.stringFill)
    canvas.create_text(data.width//2, data.spacing*9,
        text = data.answerString, font = "Courier 30",
        fill = data.stringFill)

def drawHighlightBox(canvas, data):
    width = (data.width - 6)/data.lenOfAlphabet
    x0, y0 = width*data.col + 3, data.width//3
    x1, y1 = x0 + width, y0 + width*2
    canvas.create_rectangle(x0, y0, x1, y1, fill = "blue")

def updateAlphabet(data):
    data.keywordCopy = data.keyword.upper()
    endAlphabet = ""
    for char in string.ascii_uppercase:
        if char not in data.keywordCopy:
            endAlphabet += char
    data.alphabet = data.keywordCopy + endAlphabet
    return data.alphabet

def updateAnswerString(data):
    data.answerString = data.answerString[0:data.index] + data.decodedMessage[data.index]
    while len(data.answerString) < len(data.decodedMessage):
        data.answerString += " "
    return data.answerString

def init(data):
    data.message = ""
    data.keyword = ""
    data.encodedMessage = encodeKeyword(data.message, data.keyword)
    data.messageCopy = data.encodedMessage
    data.lenOfAlphabet = 26
    data.backgroundFill = "black"
    data.alphabet = string.ascii_uppercase
    data.stringFill = "#73f440"
    data.col = 0
    # A higher speed actually makes the animation slower
    data.speed = 2
    data.count = 0
    data.index = 0
    data.spacing = 40
    data.animationOver = False
    data.answerString = ""
    data.startAnimation = 0

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if data.startAnimation == 0:
        if event.keysym in string.ascii_lowercase + string.ascii_uppercase \
        and event.keysym.upper() not in data.keyword.upper():
            data.keyword += event.keysym 
        elif event.keysym == "BackSpace":
            data.keyword = data.keyword[0:-1]
        if event.keysym == "Return":
            data.startAnimation += 1
    elif data.startAnimation == 1:
        if event.keysym in string.ascii_lowercase + string.ascii_uppercase + string.digits:
            data.message += event.keysym
        if event.keysym == "space":
            data.message += " "
        if event.keysym == "BackSpace":
            data.message = data.message[0:-1]
        data.decodedMessage = decodeKeyword(data.message, data.keyword)
        data.messageCopy = data.decodedMessage
        if event.keysym == "Return":
            data.startAnimation += 1
            return None

def timerFired(data):
    data.count += 1
    if data.startAnimation == 2 and data.animationOver == False:
        if data.messageCopy != "":
            if data.count % data.speed == 0:
                if data.messageCopy[0] in string.ascii_lowercase:
                    if data.col != ord(data.messageCopy[0]) - ord("a"):
                        data.col += 1
                    else:
                        data.answerString = updateAnswerString(data)
                        data.messageCopy = data.messageCopy[1:]
                        data.index += 1
                        data.col = 0
                elif data.messageCopy[0] in string.ascii_uppercase:
                    if data.col != ord(data.messageCopy[0]) - ord("A"):
                        data.col += 1
                    else:
                        data.answerString = updateAnswerString(data)
                        data.messageCopy = data.messageCopy[1:]
                        data.index += 1
                        data.col = 0
                else:
                    data.answerString = updateAnswerString(data)
                    data.messageCopy = data.messageCopy[1:]
                    data.index += 1
                    data.col = 0
        else:
            data.startAnimation += 1
            data.animationOver = True

def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawHighlightBox(canvas, data)
    drawString(canvas, data)
    if data.animationOver == True:
        canvas.create_text(data.width//2, data.height - (data.spacing*2),
            text = "Done!", font = "Courier 20", fill = data.stringFill)

################################################################################

# Start Citation
# From 112 Website - Animation Section
def runDecryptKeyword(width=300, height=300):
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

# runDecryptKeyword(500, 500)
# End Citation