with open("chr_list.txt", "w+") as fil:
    fil.write("id ; char\n")

    line = str(0) + " ; " + chr(0) + "\n"
    print(line)
    fil.write(line)

    i = 1
    while i != 55295:
        line = str(i) + " ; " + chr(i) + "\n"
        print(line)
        fil.write(line)
        if i != 55295:
            i += 1
