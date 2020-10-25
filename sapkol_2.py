import sys
import re

program = open("program.txt", "r")

proLst = program.read().lower().split("\n")





def errorPrint(type): #which error to print
    errorDict = {1:"Invalid file, not a Sapkol file.",
    2:"invalid command run.",
    3:"Invalid variable called.",
    4:"Invalid function called."}

    print("Error " + str(type) + ": " + errorDict[type])

def interpreter():
    if proLst[0] != "$sapkol":
        errorPrint(1)
        sys.exit()
interpreter()

program.close()
