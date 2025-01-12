
from cipherFile import *

#####################################################################################
# Start Citation
# Inputfile and output file commands found on 15-110 Website
#####################################################################################

def encodeTextFileCaesar(inputFile, outputFile, shift):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(encodeCaesarShift(line, shift))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

def encodeTextFileAtbash(inputFile, outputFile):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		line = line[:-1]
		codeList.append(encodeAtbash(line))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line + "\n")
	return("Done!")

def encodeTextFileVigenere(inputFile, outputFile, keyword):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(encodeVigenere(line, keyword))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

def encodeTextFileRoute(inputFile, outputFile, numOfCols):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		line = line[:-1]
		codeList.append(encodeRoute(line, numOfCols))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line + "\n")
	return("Done!")

def encodeTextFileKeyword(inputFile, outputFile, keyword):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(encodeKeyword(line, keyword))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

def encodeTextFileROT13(inputFile, outputFile):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(encodeROT13(line))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

#######################################################################################

def decodeTextFileCaesar(inputFile, outputFile, shift):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(decodeCaesarShift(line, shift))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

def decodeTextFileAtbash(inputFile, outputFile):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(decodeAtbash(line))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

def decodeTextFileVigenere(inputFile, outputFile, keyword):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(decodeVigenere(line, keyword))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

def decodeTextFileRoute(inputFile, outputFile, numOfCols):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		line = line[:-1]
		codeList.append(decodeRoute(line, numOfCols))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line + "\n")
	return("Done!")

def decodeTextFileKeyword(inputFile, outputFile, keyword):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(decodeKeyword(line, keyword))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

def decodeTextFileROT13(inputFile, outputFile):
	inputfile = open(inputFile, "r")
	codeList = []
	for line in inputfile:
		codeList.append(decodeROT13(line))
	outputfile = open(outputFile, "w")
	for line in codeList:
		outputfile.write(line)
	return("Done!")

#####################################################################################
# End Citation
# Inputfile and output file commands found on 15-110 Website
#####################################################################################


