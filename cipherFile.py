
#3 RailFence (half done -- need decode function)

###########################################################################################

import string
import copy

# Start Citaion
# Read About Caesar Algorithms on Cryptii.com
# Used those Algorithms to write this funciton below

def encodeCaesarShift(message, shift):
	# messages should be strings
	# only letters should shift
	shiftString = ""
	lenOfAlphabet = 26
	for char in message:
		if char in string.ascii_lowercase:
			shiftChar = chr(((ord(char) - ord("a") + shift) % lenOfAlphabet) + ord("a"))
			shiftString += shiftChar
		elif char in string.ascii_uppercase:
			shiftChar = chr(((ord(char) - ord("A") + shift) % lenOfAlphabet) + ord("A"))
			shiftString += shiftChar
		else:
			shiftString += char
	return shiftString

def decodeCaesarShift(message, shift):
	return encodeCaesarShift(message, shift*(-1))
# End Citation

###########################################################################################

# Start Citaion
# Read About Caesar Algorithims on Rumkin.com
# Used those Algorithms to write this funciton below

def encodeAtbash(message):
	codeString = ""
	for char in message:
		if char in string.ascii_lowercase:
			codeChar = chr(ord("z") - ord(char) + ord("a"))
			codeString += codeChar
		elif char in string.ascii_uppercase:
			codeChar = chr(ord("Z") - ord(char) + ord("A"))
			codeString += codeChar
		else:
			codeString += char
	return codeString

def decodeAtbash(message):
	return encodeAtbash(message)
	# Atbash is convenient in the sense that applying the same process to the 
	# encoded message returns the decoded message
#End Citation

###########################################################################################

# Start Citaion
# Read About Keyword Algorithms on Rumkin.com
# Used those Algorithms to write this funciton below

def encodeKeyword(message, keyword):
	keyword = keyword.lower()
	newAlphabet, codeString = "", ""
	for char in keyword:
		if char not in string.ascii_lowercase:
			return("Keyword must contain only letters.")
		if keyword.count(char) > 1:
			return("Keyword cannot have dupicate letters.")
	newAlphabet += keyword
	for letter in string.ascii_lowercase:
		if letter not in newAlphabet:
			newAlphabet += letter
	for char in message:
		if char not in string.ascii_lowercase:
			if char not in string.ascii_uppercase:
				codeString += char
			else:
				codeString += newAlphabet[string.ascii_uppercase.find(char)].upper()
		else:
			codeString += newAlphabet[string.ascii_lowercase.find(char)]
	return codeString
			
def decodeKeyword(message, keyword):
	newAlphabet, codeString = "", ""
	newAlphabet += keyword
	for letter in string.ascii_lowercase:
		if letter not in newAlphabet:
			newAlphabet += letter
	for char in message:
		if char not in string.ascii_lowercase:
			if char not in string.ascii_uppercase:
				codeString += char
			else:
				char = char.lower()
				codeString += string.ascii_lowercase[newAlphabet.find(char)].upper()
		else:
			codeString += string.ascii_lowercase[newAlphabet.find(char)]
	return codeString

# End Citation

###########################################################################################

# Start Citaion
# Read About ROT13 Algorithms on Rumkin.com
# Used those Algorithms to write this funciton below

def encodeROT13(message, shift = 13):
	shiftString = ""
	lenOfAlphabet = 26
	shift = 13
	for char in message:
		if char in string.ascii_lowercase:
			shiftChar = chr(((ord(char) - ord("a") + shift) % lenOfAlphabet) + ord("a"))
			shiftString += shiftChar
		elif char in string.ascii_uppercase:
			shiftChar = chr(((ord(char) - ord("A") + shift) % lenOfAlphabet) + ord("A"))
			shiftString += shiftChar
		else:
			shiftString += char
	return shiftString

def decodeROT13(message):
	return encodeROT13(message, shift = -13)

# End Citation

###########################################################################################

# Start Citaion
# Read About Vigenere Algorithms on Rumkin.com and Wikipedia
# Used those Algorithms to write this funciton below

def createVigenereKeywordString(message, keyword):
	keyword = keyword.lower()
	keyString = ""
	skip = 0
	letterString = string.ascii_uppercase + string.ascii_lowercase
	lenKey = len(keyword)
	lenMes = len(message)
	for index in range(lenMes):
		if message[index] not in letterString:
			keyString += message[index]
			skip += 1
		else:
			keyString += keyword[(index - skip)%lenKey]
	return keyString

def encodeVigenere(message, keyword):
	keyword = keyword.lower()
	for char in keyword:
		if char not in string.ascii_lowercase:
			return "Keyword must only contain letters."
	codeString, lenMes, index = "", len(message), 0
	lenOfAlphabet = 26
	keyString = createVigenereKeywordString(message, keyword)
	for index in range(lenMes):
		if keyString[index] in string.ascii_lowercase:
			if message[index] in string.ascii_lowercase:
				shift = ord(keyString[index]) - ord("a")
				codeChar = chr(((ord(message[index]) - ord("a") + shift) % lenOfAlphabet) 
					+ ord("a"))
				codeString += codeChar
			elif message[index] in string.ascii_uppercase:
				shift = ord(keyString[index]) - ord("A")
				codeChar = chr(((ord(message[index]) - ord("a") + shift) % lenOfAlphabet) 
					+ ord("a")).upper()
				codeString += codeChar
		else:
			codeString += keyString[index]
	return codeString

def decodeVigenere(message, keyword):
	codeString, lenMes, index = "", len(message), 0
	lenOfAlphabet = 26
	keyString = createVigenereKeywordString(message, keyword)
	for index in range(lenMes):
		if keyString[index] in string.ascii_lowercase:
			if message[index] in string.ascii_lowercase:
				shift = ord(keyString[index]) - ord("a")
				codeChar = chr(((ord(message[index]) - ord("a") - shift) % lenOfAlphabet) 
					+ ord("a"))
				codeString += codeChar
			elif message[index] in string.ascii_uppercase:
				shift = ord(keyString[index]) - ord("a")
				codeChar = chr(((ord(message[index]) - ord("A") - shift) % lenOfAlphabet) 
					+ ord("a")).upper()
				codeString += codeChar
		else:
			codeString += keyString[index]
	return codeString

# End Citation

###########################################################################################

# Start Citaion
# Read About Route Algorithms on Cryptii.com and Wikipedia
# Used those Algorithms to write this funciton below

def encodeRoute(message, numOfCols):
	# cipher is going to take downward route
	# starting from the top left corner
	if numOfCols < 1:
		return "The Route must have at least 1 column."
	codeString = ""
	while len(message) % numOfCols != 0:
		message += " "
	route = []
	index = 0
	rows = len(message) // numOfCols
	for i in range(rows):
		route.append([None]*numOfCols)
	for row in range(rows):
		for col in range(numOfCols):
			route[row][col] = message[index]
			index += 1
	cols = len(route[0])
	rows = len(route)
	for col in range(cols):
		for row in range(rows):
			codeString += route[row][col]
	return codeString

def decodeRoute(message, numOfCols):
	if numOfCols < 1:
		return "The Route must have at least 1 column."
	codeString = ""
	while len(message) % numOfCols != 0:
		message += " "
	route = []
	index = 0
	rows = len(message) // numOfCols
	for i in range(rows):
		route.append([None]*numOfCols)
	cols = len(route[0])
	rows = len(route)
	index = 0
	for col in range(cols):
		for row in range(rows):
			route[row][col] = message[index]
			index += 1
	for row in range(rows):
		for col in range(cols):
			codeString += route[row][col]
	return codeString

# End Citation

