import sys
f = open('code.txt', 'r')
text = f.read().split("\n")


f.close()


def main(lines):
    pass


class Interpreter:
    def __init__(self):
        self.Command_DataBase = ["print", "var", "func", "lst", "#", "change"]
        # Array of usable commands

    def Code_Preparer(self):
        """
        :returns: Clean code, readable list.
        """
        pass

    def Tokenizer(self):
        """
        :return: Finds the argument(s) for the command.
        """
        pass

    def String_Analyzer(self):
        """
        :return: Returns clean string to print.
        """


if __name__ == '__main__':
    main(text)
