
########################################################################################################################
# Im super sorry about all of the imports below, but I made every page it's own unique file
# because the functions were running into each other because they had the same function names.
########################################################################################################################

from caesarShiftAnimationFile import *
from encryptCaesarShift import *
from ROT13Animation import *
from atbashAnimationFile import *
from routeAnimation import *
from decryptRoute import *
from vigenereAnimation import *
from encryptVigenereCipher import *
from keywordAnimation import *
from decryptKeyword import *
from fileChange import *
from encryptCaesarFile import *
from encryptAtbashFile import *
from encryptVigenereFile import *
from encryptRouteFile import *
from encryptKeywordFile import *
from encryptROT13File import *
from decryptCaesarFile import *
from decryptVigenereFile import *
from decryptRouteFile import *
from decryptKeywordFile import *

def init(data):
    data.message = ""
    data.backgroundFill = "black"
    data.stringFill = "#73f440"
    data.currScreen = "startScreen"
    data.speed = 5
    data.labelPack = 1
    data.index = 0
    data.buttonWidth = 50
    data.count = 0
    data.spacing = 40


def drawStartScreen(canvas, data):
    font, fill = "Courier 40", data.stringFill
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, data.spacing*2, text = "Welcome to PyCrypt", 
        fill = fill, font = font)
    canvas.create_rectangle(data.width//4, data.spacing*4, (data.width//4)*3, 
        data.spacing * 5, outline = data.stringFill, width = 3)
    canvas.create_text(data.width//2, data.spacing*4.5, text = "Press 'E' to Encrypt", 
        font = "Courier 20", fill = fill)
    canvas.create_rectangle(data.width//4, data.spacing*6, (data.width//4)*3, 
        data.spacing * 7, outline = data.stringFill, width = 3)
    canvas.create_text(data.width//2, data.spacing*6.5, text = "Press 'D' to Decrypt", 
        font = "Courier 20", fill = fill)
    canvas.create_rectangle(data.width//4, data.spacing*8, (data.width//4)*3, 
        data.spacing * 9, outline = data.stringFill, width = 3)
    canvas.create_text(data.width//2, data.spacing*8.5, text = "Press 'A' for About", 
        font = "Courier 20", fill = fill)
    canvas.create_text(data.width//2, data.height - data.spacing, 
        text = "Press '?' for help screen")
    canvas.create_text(data.width//2, data.spacing*11, text = "Press '?' for the Help Page",
        font = "Courier 20", fill = fill)

def drawHelpScreen(canvas, data):
    font, fill = "Courier 40", data.stringFill
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, data.spacing, text = "Help", fill = fill, font = font)
    spacing, gap = 30, 40
    spaceNum = 0
    paragraph = [
    "Follow any key instructions written on the screen.",
    "(They are there to help!)", " "
    "Key Commmand List:",
    "Space Bar - Return to Home Page",
    "'?' - Go to Help Screen",
    "'A' - Go to About Page",
    "'E' - Go to Encryption Page",
    "'D' - Go to Decryption Page",
    "When you are typing a word, keyword, or shift, lock in your",
    "answer with the enter key. Then you can begin typing the next",
    "required input until you are done. Pressing enter also begins",
    "the animation, when all of the inputs are filled in.",
    "Have fun, and happy ciphering! :-)"]
    for i in range(len(paragraph)):
        canvas.create_text(data.width//2, spacing * spaceNum + gap*2.5, 
            text = paragraph[i], 
            fill = data.stringFill, font = "Ariel 16")
        spaceNum += 1

def drawDedicationPage(canvas, data):
    spacing = 20
    font, fill = "Courier 40", data.stringFill
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, data.spacing, text = "Dedication", 
        fill = fill, font = font)
    font = "Ariel 16"
    gap = 40
    spaceNum = 3
    paragraph = [
    "           PyCrypt was inspired by two of my dearest high school",
    "friends: Michael Maslokowski and Kellie O’Toole. Our shared yet    ",
    "secret forms of communication allowed our friendship to grow   ",
    "as well as our love of ciphers and puzzles. I hope that PyCrypt    ",
    "brings as much joy and inpires as much interest as Mike and     ",
    "Kellie themselves, and for that, I'd like to dedicate this term",
    "project to them."]
    for i in range(len(paragraph)):
        canvas.create_text(spacing, spacing * spaceNum + gap, 
            text = paragraph[i], 
            fill = data.stringFill, font = font, anchor = NW)
        spaceNum += 1
    ################################################################################ 
    # Start Citation - From Tkinter Book Online
    # Not modified except for file name
    # Photo was created from Bitmoji which is Snapchat affiliated
    ################################################################################
    photo = PhotoImage(file = "3.gif")
    label = Label(image = photo)
    label.image = photo
    canvas.create_image((data.width//2,data.height//2 + data.spacing * 3), 
        image = photo)
    canvas.create_text(data.width//2, data.height//2 + data.spacing * 5.5,
        text = "      Me                   Mike                   Kellie", fill = data.stringFill,
        font = "Ariel 15")
    ################################################################################
    # End Eitation
    ################################################################################

def drawAboutPage(canvas, data):
    spacing = 30
    font, fill = "Courier 40", data.stringFill
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, data.spacing, text = "About", 
        fill = fill, font = font)
    font = "Ariel 16"
    gap = 60
    spaceNum = 3
    paragraph = ["PyCrypt is a program that encrypts and decrypts messages",
    "based on selected cipher, message, and sometimes keywords",
    "or phrases. With six different ciphers and an infinite",
    "combination of keys and mesages, PyCrypt hopes to take",
    "the mystery out of code-breaking!",
    "For help regarding the program: press the '?' key",
    "To go back to the home page: press the space bar"]
    for i in range(len(paragraph)):
        canvas.create_text(data.width//2, spacing * spaceNum + gap, 
            text = paragraph[i], 
            fill = data.stringFill, font = font)
        spaceNum += 1
    canvas.create_text(data.width//2, data.spacing*2, text = "PyCrypt (Version 1.0)",
        font = "Courier 20", fill = fill)
    x0, y0 = 10, data.height - 10
    x1, y1 = x0 + data.buttonWidth, y0 - data.buttonWidth
    canvas.create_text(data.width//2, data.spacing*11, 
        text = "Press '*' to view the Dedication Page!", 
        font = "Courier 20", fill = data.stringFill)

def drawEncryptPage(canvas, data):
    spacing = 30
    font, fill = "Courier 40", data.stringFill
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, data.spacing, text = "Encrypt Page", 
        fill = fill, font = font)
    spaceNum = 3
    paragraph = ["Caesar Shift Cipher: Press 1", "ROT-13 Cipher: Press 2", "Atbash Cipher: Press 3",
    "Route Cipher: Press 4", "Vigenere Cipher: Press 5", "Keyword Cipher: Press 6", "Encrypt Files: Press 'F'"]
    for line in paragraph:
    	canvas.create_text(data.width//2, data.spacing * spaceNum, text = line, 
    		font = "Courier 25", fill = fill)
    	spaceNum += 1

def drawDecryptPage(canvas, data):
    spacing = 30
    font, fill = "Courier 40", data.stringFill
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, data.spacing, text = "Decrypt Page", 
        fill = fill, font = font)
    spaceNum = 3
    paragraph = ["Caesar Shift Cipher: Press 1", "ROT-13 Cipher: Press 2", "Atbash Cipher: Press 3",
    "Route Cipher: Press 4", "Vigenere Cipher: Press 5", "Keyword Cipher: Press 6", "Decrypt Files: Press 'F'"]
    for line in paragraph:
        canvas.create_text(data.width//2, data.spacing * spaceNum, text = line, 
            font = "Courier 25", fill = fill)
        spaceNum += 1

def drawEncryptFilePage(canvas, data):
    spacing = 30
    font, fill = "Courier 40", data.stringFill
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, data.spacing, text = "Encrypt File Page", 
        fill = fill, font = font)
    spaceNum = 3
    paragraph = ["Caesar Shift Cipher: Press 1", "ROT-13 Cipher: Press 2", "Atbash Cipher: Press 3",
    "Route Cipher: Press 4", "Vigenere Cipher: Press 5", "Keyword Cipher: Press 6"]
    for line in paragraph:
        canvas.create_text(data.width//2, data.spacing * spaceNum, text = line, 
            font = "Courier 25", fill = fill)
        spaceNum += 1

def drawDecryptFilePage(canvas, data):
    spacing = 30
    font, fill = "Courier 40", data.stringFill
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, data.spacing, text = "Decrypt File Page", 
        fill = fill, font = font)
    spaceNum = 3
    paragraph = ["Caesar Shift Cipher: Press 1", "ROT-13 Cipher: Press 2", "Atbash Cipher: Press 3",
    "Route Cipher: Press 4", "Vigenere Cipher: Press 5", "Keyword Cipher: Press 6"]
    for line in paragraph:
        canvas.create_text(data.width//2, data.spacing * spaceNum, text = line, 
            font = "Courier 25", fill = fill)
        spaceNum += 1

def timerFired(data):
    pass

def mousePressed(event, data):
	pass

def keyPressed(event, data):
    if event.char == " ": data.currScreen = "startScreen"
    elif event.char == "?": data.currScreen = "helpScreen"
    elif (event.char).upper() == "A": data.currScreen = "aboutPage"
    elif (event.char).upper() == "E": data.currScreen = "encryptPage"
    elif (event.char).upper() == "D": data.currScreen = "decryptPage"
    if data.currScreen == "encryptPage":
        if event.keysym == "1": runEncryptCaesarShift(500, 500)
        elif event.keysym == "2": runROT13(500, 500) #same
        elif event.keysym == "3": runAtbash(500, 500) #same
        elif event.keysym == "4": runEncryptRoute(500, 500)
        elif event.keysym == "5": runEncryptVigenere(750, 750)
        elif event.keysym == "6": runEncryptKeyword(500, 500)
        elif (event.char).upper() == "F": data.currScreen = "encryptFilePage"
    elif data.currScreen == "decryptPage":
        if event.keysym == "1": runDecryptCaesarShift(500, 500)
        elif event.keysym == "2": runROT13(500, 500) #same
        elif event.keysym == "3": runAtbash(500, 500) #same
        elif event.keysym == "4": runDecryptRoute(500, 500)
        elif event.keysym == "5": runDecryptVigenere(750, 750)
        elif event.keysym == "6": runDecryptKeyword(500, 500)
        elif (event.char).upper() == "F": data.currScreen = "decryptFilePage"
    elif data.currScreen == "aboutPage":
        if event.char == "*": data.currScreen = "dedicationPage"
    elif data.currScreen == "encryptFilePage":
        if event.keysym == "1": runEncryptCaesarFile(500, 500)
        elif event.keysym == "2": runEncryptROT13File(500, 500) #same
        elif event.keysym == "3": runEncryptAtbashFile(500, 500) #same
        elif event.keysym == "4": runEncryptRouteFile(500, 500)
        elif event.keysym == "5": runEncryptVigenereFile(500, 500)
        elif event.keysym == "6": runEncryptKeywordFile(500, 500)
    elif data.currScreen == "decryptFilePage":
        if event.keysym == "1": runDecryptCaesarFile(500, 500)
        elif event.keysym == "2": runEncryptROT13File(500, 500) #same
        elif event.keysym == "3": runEncryptAtbashFile(500, 500) #same
        elif event.keysym == "4": runDecryptRouteFile(500, 500)
        elif event.keysym == "5": runDecryptVigenereFile(500, 500)
        elif event.keysym == "6": runDecryptKeywordFile(500, 500)

def redrawAll(canvas, data):
    if data.currScreen == "startScreen":
        drawStartScreen(canvas, data)
    elif data.currScreen == "helpScreen":
        drawHelpScreen(canvas, data)
    elif data.currScreen == "aboutPage":
        drawAboutPage(canvas, data)
    elif data.currScreen == "dedicationPage":
        drawDedicationPage(canvas, data)
    elif data.currScreen == "encryptPage":
        drawEncryptPage(canvas, data)
    elif data.currScreen == "decryptPage":
        drawDecryptPage(canvas, data)
    elif data.currScreen == "decryptFilePage":
        drawDecryptFilePage(canvas, data)
    elif data.currScreen == "encryptFilePage":
        drawEncryptFilePage(canvas, data)

################################################################################
# Start Citation
# From 112 Website
################################################################################
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

################################################################################
# End Eitation
################################################################################
