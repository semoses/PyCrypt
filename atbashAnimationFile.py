
from cipherFile import *
from tkinter import *

################################################################################

# Atbash

def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, 
        fill = data.backgroundFill)

def makeAlphabetList(data):
    alphabetList = [[],[]]
    for index in range(data.lenOfAlphabet):
        alphabetList[0].append(string.ascii_uppercase[index])
    for index in range(data.lenOfAlphabet):
        alphabetList[1].append(string.ascii_uppercase[-index -1])
    return(alphabetList)


def drawString(canvas, data):
    canvas.create_text(data.width//2, data.spacing, text = "Encrypt/Decrypt Atbash", 
        font = "Courier 30", fill = data.stringFill)
    alphabetList = makeAlphabetList(data)
    width = (data.width - 6)/data.lenOfAlphabet
    for row in range(2):
        for col in range(data.lenOfAlphabet):
            x0, y0 = width*col + 3, width*row + data.width//3
            x1, y1 = x0 + width, y0 + width
            canvas.create_rectangle(x0, y0, x1, y1, outline = data.stringFill)
            canvas.create_text(x0 + width/2, y0 + width/2, 
                text = alphabetList[row][col], 
                font = "Courier 15", fill = data.stringFill)
    
    canvas.create_text(data.width//2, data.height//2 + (data.spacing/2),
        text = data.message, font = "Courier 30",
        fill = data.stringFill)
    canvas.create_text(data.width//2, data.height//2 + (data.spacing * 1.5),
        text = data.answerString, font = "Courier 30",
        fill = data.stringFill)

def drawHighlightBox(canvas, data):
    width = (data.width - 6)/data.lenOfAlphabet
    x0, y0 = width*data.col + 3, data.width//3
    x1, y1 = x0 + width, y0 + width*2
    canvas.create_rectangle(x0, y0, x1, y1, fill = "blue")

def updateAnswerString(data):
    data.answerString = data.answerString[0:data.index] + data.decodedMessage[data.index]
    while len(data.answerString) < len(data.decodedMessage) - 1:
        data.answerString += " "
    return data.answerString

def init(data):
    data.message = ""
    data.encodedMessage = encodeAtbash(data.message)
    data.encodedMessageCopy = data.encodedMessage
    data.decodedMessage = decodeAtbash(data.encodedMessage)
    data.lenOfAlphabet = 26
    data.backgroundFill = "black"
    data.stringFill = "#73f440"
    data.col = 0
    # A higher speed actually makes the animation slower
    data.speed = 2
    data.count = 0
    data.index = 0
    data.spacing = 40
    data.animationOver = False
    data.answerString = ""
    data.startAnimation = False

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if data.startAnimation == False:
        if event.char in string.printable:
            data.message += event.char
        if event.keysym == "BackSpace":
            data.message = data.message[0:-1]
        data.encodedMessage = data.message
        data.decodedMessage = decodeAtbash(data.message)
        if event.keysym == "Return":
            data.startAnimation = True
            return None

def timerFired(data):
    data.count += 1
    if data.startAnimation == True:
        if data.count % data.speed == 0 and data.encodedMessage != "":
            blackSpace = " " * (len(data.encodedMessage) - 1)
            if data.encodedMessage[0] in string.ascii_lowercase:
                if data.col != ord(data.encodedMessage[0]) - ord("a"):
                    data.col += 1
                else:
                    data.answerString = updateAnswerString(data)
                    data.encodedMessage = data.encodedMessage[1:]
                    data.index += 1
                    data.col = 0
            elif data.encodedMessage[0] in string.ascii_uppercase:
                if data.col != ord(data.encodedMessage[0]) - ord("A"):
                    data.col += 1
                else:
                    data.answerString = updateAnswerString(data)
                    data.encodedMessage = data.encodedMessage[1:]
                    data.index += 1
                    data.col = 0
            else:
                data.answerString = updateAnswerString(data)
                data.encodedMessage = data.encodedMessage[1:]
                data.index += 1
                data.col = 0
        elif data.encodedMessage == "":
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
def runAtbash(width=300, height=300):
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

# runAtbash(500, 500)
# End Citation