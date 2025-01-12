
from cipherFile import *
from tkinter import *

###########################################################################################

def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, 
        fill = data.backgroundFill)

def incrementLetter(message, index):
    resultString = ""
    changeChar = message[index]
    changeChar = encodeCaesarShift(changeChar, -1)
    resultString += message[0:index] + changeChar + message[index + 1:]
    return resultString

def drawString(canvas, data):
    canvas.create_text(data.width//2, data.spacing, text = "Decrypt Caesar Shift", 
        font = "Courier 30", fill = data.stringFill)
    canvas.create_text(data.width//2, (data.height//2 - data.spacing), 
        text = data.encodedMessage, font = "Courier 30", 
        fill = data.stringFill)
    canvas.create_text(data.width//2, (data.height//2 - data.spacing*(2)), 
        text = data.encodedMessageCopy, font = "Courier 30", 
        fill = data.stringFill)
    canvas.create_text(data.width//2, data.height//2 + (data.spacing * 2),
        text = "Shift: %d" % (data.currShift), font = "Courier 30", fill = data.stringFill)
    canvas.create_text(data.width//2, data.height//2 + (data.spacing * 3), 
        text = "Shift = %d" % data.shift, font = "Courier 30", fill = data.stringFill)
    canvas.create_text(data.width//2, data.spacing)

def init(data):
    data.shift = 0
    data.message = ""
    data.encodedMessage = data.message
    data.encodedMessageCopy = data.encodedMessage
    data.decodedMessage = decodeCaesarShift(data.encodedMessage, data.shift)
    data.backgroundFill = "black"
    data.stringFill = "#73f440"
    data.currShift = 0
    data.speed = 3
    data.index = 0
    data.count = 0
    data.spacing = 40
    data.startAnimation = 0
    data.animationOver = False

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if data.startAnimation == 0:
        if event.char in string.printable:
            data.message += event.char
        if event.keysym == "BackSpace":
            data.message = data.message[0:-1]
        elif event.keysym == "Return":
            data.startAnimation += 1
        data.encodedMessage = data.message
        data.encodedMessageCopy = data.encodedMessage
        data.decodedMessage = decodeCaesarShift(data.message, data.shift)
    elif data.startAnimation == 1:
        if event.keysym in string.digits:
            data.shift = int(data.shift)*10 + int(event.keysym)
        elif event.keysym == "BackSpace":
            data.shift = data.shift//10
        data.encodedMessage = data.message
        data.encodedMessageCopy = data.encodedMessage
        data.decodedMessage = decodeCaesarShift(data.message, data.shift)
        if event.keysym == "Return":
            data.startAnimation += 1

def timerFired(data):
    if data.startAnimation == 2:
        data.count += 1
        if data.count % data.speed == 0:
            i = data.index
            if data.encodedMessage[i] != data.decodedMessage[i]:
                data.encodedMessage = incrementLetter(data.encodedMessage, i)
                data.currShift += 1
            elif data.index < (len(data.encodedMessage) - 1):
                data.index += 1
                data.currShift = 0
            else:
                data.animationOver = True

def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawString(canvas, data)
    if data.animationOver == True:
        canvas.create_text(data.width//2, data.height - (data.spacing*6),
            text = "Done!", font = "Courier 20", fill = data.stringFill)


###########################################################################################

# Start Citation
# From 112 Website - Animation Section
def runDecryptCaesarShift(width=300, height=300):
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

# runDecryptCaesarShift(500, 500)
# End Citation
