def runLengthEncoding(string):
    previous = string[0]
    count = 0
    arr = []
    for s in string:
        if count == 9 or s != previous:
            arr.append("{}{}".format(count, previous))
            count = 0
        
        count += 1
        previous = s

    arr.append("{}{}".format(count, string[len(string)-1]))
    return "".join(arr)

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))