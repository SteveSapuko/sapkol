def Tokenizer(sep1, sep2, line, which):
    """
    :return: Finds the argument(s) for the command.
    """
    possible = []

    write = ''
    is_writing = False

    counter = line.count(sep1) + line.count(sep2)
    if counter % 2 == 1 or counter == 0:
        # self.Error("Invalid use of separators.")
        pass

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


print(Tokenizer("/","/","print /ass/ /batt/", 1))

