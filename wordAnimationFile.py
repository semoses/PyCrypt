# Moving Letters Code Cracking Animation

from cipherFile import *
from tkinter import *

def incrementLetter(message, index):
    resultString = ""
    changeChar = message[index]
    changeChar = encodeCaesarShift(changeChar, 1)
    resultString += message[0:index] + changeChar + message[index + 1:]
    return resultString

def drawString(canvas, data):
    canvas.create_text(data.width//2, (data.height//2 + data.offset/2), 
        text = data.encodedMessage, font = "Courier 30", 
        fill = data.stringFill)
    canvas.create_text(data.width//2, (data.height//2 - data.offset/2), 
        text = data.encodedMessageCopy, font = "Courier 30", 
        fill = data.stringFill)

def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, 
        fill = data.backgroundFill)

def init(data):
    data.encodedMessage = encodeAtbash("Hello World!")
    data.decodedMessage = "Hello World!"
    data.encodedMessageCopy = data.encodedMessage
    data.backgroundFill = "black"
    data.stringFill = "#73f440"
    data.speed = 1
    data.count = 0
    data.index = 0
    data.offset = 40

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    data.count += 1
    if data.count % data.speed == 0:
        i = data.index
        if data.encodedMessage[i] != data.decodedMessage[i]:
            data.encodedMessage = incrementLetter(data.encodedMessage, i)
        elif data.index < (len(data.encodedMessage) - 1):
            data.index += 1

def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawString(canvas, data)


# Start Citation
# From 112 Website - Animation Section
def run(width=300, height=300):
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

run(500, 500)
# End Citation