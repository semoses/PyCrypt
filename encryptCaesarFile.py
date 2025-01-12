
from tkinter import *
from fileChange import *
import string

def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")

def drawString(canvas, data):
    canvas.create_text(data.width//2, data.spacing, text = "Encrypt Caesar File", 
        fill = data.fill, font = "Courier 30")   
    canvas.create_text(data.spacing, data.spacing*3, 
        text = "Input Filename: %s" % data.inputFilename, fill = data.fill,
        font = "Courier 20", anchor = W)
    canvas.create_text(data.spacing, data.spacing*5, 
        text = "Output Filename: %s" % data.outputFilename, fill = data.fill,
        font = "Courier 20", anchor = W)
    canvas.create_text(data.spacing, data.spacing*7, 
        text = "Shift: %d" % data.shift, fill = data.fill,
        font = "Courier 20", anchor = W)

def init(data):
    data.fill = "#73f440"
    data.spacing = 40
    data.shift = 0
    data.legalString = string.ascii_letters + string.digits + string.punctuation
    data.inputFilename = ""
    data.errorMessage = False
    data.outputFilename = ""
    data.writeNextLine = 0
    data.over = False

def timerFired(data):
    if data.writeNextLine == 3 and data.over == False:
        try:
            encodeTextFileCaesar(data.inputFilename, data.outputFilename, data.shift)
            data.over = True
        except:
            data.errorMessage = True

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if data.writeNextLine == 0:
        if event.char in data.legalString or event.char == " ":
            data.inputFilename += event.char
        elif event.keysym == "BackSpace":
            data.inputFilename = data.inputFilename[:-1]
        elif event.keysym == "Return":
            data.writeNextLine += 1
    elif data.writeNextLine == 1:
        if event.char in data.legalString or event.char == " ":
            data.outputFilename += event.char
        elif event.keysym == "BackSpace":
            data.outputFilename = data.outputFilename[:-1]
        elif event.keysym == "Return":
            data.writeNextLine += 1
    elif data.writeNextLine == 2:
        if event.char in string.digits:
            data.shift = (data.shift*10) + int(event.char)
        elif event.keysym == "BackSpace":
            data.shift //= 10
        elif event.keysym == "Return":
            data.writeNextLine += 1

def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawString(canvas, data)
    if data.errorMessage == True:
        message = ["Error. Please Close window", 
        "and try again. make sure",
        "you have the correct file names."]
        numLine = 8
        for line in message:
            canvas.create_text(data.width//2, data.spacing*numLine,
                text = line, fill = "red", font = "Courier 20")
            numLine += 1
    if data.over == True:
        canvas.create_text(data.width//2, data.spacing*10, text = "Done!",
            fill = data.fill, font = "Courier 20")


################################################################################
# Start Citation
# From 112 Website
################################################################################
def runEncryptCaesarFile(width=300, height=300):
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

# runEncryptCaesarFile(500, 500)

################################################################################
# End Eitation
################################################################################