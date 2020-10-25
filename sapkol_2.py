import sys
f = open('program.txt', 'r')
text = f.read().split("\n")


f.close()


def main(lines):
    Code = Interpreter(Code_Preparer(lines), lines)



def Code_Preparer(lines):
    """
    :returns: Clean code, readable list.
    """
    blank_lines = lines.count('')
    # Number of blank lines so we can remove it

    for y in range(blank_lines):
        lines.remove('')

    Code_Matrix = []
    for x in lines:
        Code_Matrix.append(x.split(' '))

    if lines[0] != "$sapkol":
        Interpreter.Error(1, 1)

    return Code_Matrix


class Interpreter:
    def __init__(self, matrix, lines):
        self.Command_DataBase = ["print", "var", "func", "lst", "#", "change"]
        # list of acceptable commands
        self.Number_of_lines = len(lines)
        # number of lines
        self.matrix = matrix
        # matrix of all the lines, each lines is split by " ".
        self.lines = lines
        # lines of all the code.

    def Error(self, errCode, errPlace = "*not specified*"):
        errDict = {1:"Invalid file, not a Sapkol file",
        2:"Invalid command run",
        3:"Invalid variable called",
        4:"Invalid function called",
        5:"Invalid parameters"}

        print("Error code " + str(errCode) + ": " + errDict[errCode] + "; at line: " + errPlace)
        sys.exit()

    def Tokenizer(self, sep1, sep2, line, which):
        """
        :return: Finds the argument(s) for the command.
        """
        possible = []

        write = ''
        is_writing = False


        counter = line.count(sep1) + line.count(sep2)
        if counter % 2 == 1 or counter == 0:
            self.Error(5)


        for i in line:
            if i == sep1 and not is_writing:
                is_writing = True

            elif i == sep2:
                is_writing = False
                possible.append(write)
                write = ''

            elif is_writing:
                write += i

        return possible[which]


    def String_Analyzer(self):
        """
        :return: Returns clean string to print.
        """
        pass




if __name__ == '__main__':
    main(text)
