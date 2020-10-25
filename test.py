import sys

def Error(errCode, errPlace = "*not specified*"):
    errDict = {1:"Invalid file, not a Sapkol file",
    2:"Invalid command run",
    3:"Invalid variable called",
    4:"Invalid function called",
    5:"Invalid parameters"}

    print("Error code " + str(errCode) + ": " + errDict[errCode] + "; at line: " + errPlace)
    sys.exit()

Error(1)
