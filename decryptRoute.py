
from tkinter import *
from cipherFile import *

def drawBackground(canvas, data):
	canvas.create_rectangle(0, 0, data.width, data.height, 
		fill = "black")

def drawString(canvas, data):
	canvas.create_text(data.width//2, data.spacing, text = "Decrypt Route Cipher", 
		font = "Courier 30", fill = data.stringFill) 
	canvas.create_text(data.spacing, data.height//2 + data.spacing*3.5,
		text = data.answerString[0:35], font = "Courier 20",
		fill = data.stringFill, anchor = W)
	canvas.create_text(data.spacing, data.height//2 + data.spacing*4,
		text = data.answerString[35:70], font = "Courier 20",
		fill = data.stringFill, anchor = W)
	canvas.create_text(data.spacing, data.height//2 + data.spacing*4.5,
		text = data.answerString[70:], font = "Courier 20",
		fill = data.stringFill, anchor = W)
	canvas.create_text(data.width//2, data.height//2 + data.spacing*5,
		text = "Rows: %d" % (data.numOfRows), font = "Courier 30",
		fill = data.stringFill)
	canvas.create_text(data.width//2, data.height//2 + data.spacing * 5.5,
        text = "Use up and down arrows!",
        font = "Courier 15", fill = data.stringFill)

def drawGrid(canvas, data):
	space = data.spacing
	margin = data.margin
	for col in range(data.numOfCols):
		for row in range(data.numOfRows):
			x0, y0 = (data.boxWidth*col) + margin, row*data.boxWidth + space*2
			x1, y1 = x0 + data.boxWidth, y0 + data.boxWidth
			canvas.create_rectangle(x0, y0, x1, y1, outline = data.stringFill)

def fillGrid(canvas, data):
	margin = data.margin
	space = data.spacing
	index = 0
	for col in range(data.numOfCols):
		for row in range(data.numOfRows):
			x = col*data.boxWidth + margin + data.boxWidth/2
			y = row*data.boxWidth + space*2 + data.boxWidth/2
			if index < len(data.message):
				canvas.create_text(x, y, text = data.message[index],
					fill = data.stringFill, font = "Courier 20")
			index += 1

def drawHighlightBox(canvas, data):
	row = data.row
	col = data.col
	margin = data.margin
	space = data.spacing
	x0, y0 = (col*data.boxWidth) + margin, row*data.boxWidth + space*2
	x1, y1 = x0 + data.boxWidth, y0 + data.boxWidth
	canvas.create_rectangle(x0, y0, x1, y1, fill = "blue")

def init(data):
	data.message = ""
	data.answerString = ""
	data.numOfRows = 2
	data.lenOfAlphabet = 26
	data.stringFill = "#73f440"
	data.speed = 4 # A higher speed actually makes the animation slower
	data.count = 0
	data.index = 0
	data.row, data.col = 0, 0
	data.legalString = string.ascii_letters + string.digits + string.punctuation
	data.boxWidth = 30
	data.numOfCols = 1
	data.margin = (data.width - (data.boxWidth * data.numOfCols)) / 2
	data.spacing = 40
	data.animationOver = False
	data.startAnimation = 0
	data.highlightRow = 0
	data.highlightCol = 0

def keyPressed(event, data):
	if data.startAnimation == 1:
		if event.char in data.legalString:
			data.message += event.char
		if event.keysym == "space":
			data.message += " "
		if event.keysym == "BackSpace":
			data.message = data.message[0:-1]
		if data.message != "":
			data.decodedMessage = decodeRoute(data.message, data.numOfCols)
		if event.keysym == "Return":
			data.startAnimation += 1
		if len(data.message) >= data.numOfRows:
			data.numOfCols = (len(data.message) - 1) // data.numOfRows + 1
		data.margin = (data.width - (data.boxWidth * data.numOfCols)) / 2
	elif data.startAnimation == 0:
		if event.keysym in "Up" and data.numOfRows < 10:
			data.numOfRows += 1
		elif event.keysym == "Down" and data.numOfRows > 2:
			data.numOfRows -= 1
		if len(data.message) >= data.numOfRows:
			data.numOfCols = (len(data.message) - 1) // data.numOfRows + 1
		data.margin = (data.width - (data.boxWidth * data.numOfCols)) / 2
		if data.message != "":
			data.decodedMessage = decodeRoute(data.message, data.numOfCols)
		if event.keysym == "Return":
			data.startAnimation += 1

def mousePressed(event, data):
	pass

def timerFired(data):
	data.count += 1
	if data.startAnimation == 2 and data.animationOver == False:
		if data.count % data.speed == 0:
			if data.row == 0 and data.col == 0 and data.message[0] != " ":
				data.answerString += data.message[0]
			if data.row == (data.numOfRows - 1) and data.col == (data.numOfCols - 1):
				data.animationOver = True
			elif data.row != (data.numOfRows) and data.col != (data.numOfCols): 
				if data.col == (data.numOfCols - 1):
					data.row += 1
					data.col = 0
					data.index += 1
					data.answerString += data.decodedMessage[data.index]
				else:
					data.col += 1
					data.index += 1
					data.answerString += data.decodedMessage[data.index]
			

def redrawAll(canvas, data):
	drawBackground(canvas, data)
	if data.startAnimation == 2:
		drawHighlightBox(canvas, data)
	drawGrid(canvas, data)
	fillGrid(canvas, data)
	drawString(canvas, data)
	if data.animationOver == True:
		canvas.create_text(data.width//2, data.height//2 + data.spacing*6,
			text = "Done!", font = "Courier 20",
			fill = data.stringFill)

################################################################################

# Start Citation
# From 112 Website - Animation Section
def runDecryptRoute(width=300, height=300):
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

# runDecryptRoute(500, 500)
# End Citation