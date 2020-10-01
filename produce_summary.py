def melon(day, file):
    
    print("Day", day)

    openfile = open(file)

    for line in openfile:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    openfile.close()
melon(1, "um-deliveries-20140521.txt")


