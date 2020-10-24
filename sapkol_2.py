import sys
import re

program = open("program.txt", "r")

proLst = program.read().lower().split("\n")

#print(proLst)

if proLst[0] != "#sapkol":
    print("Invalid File")
    sys.exit()




program.close()
