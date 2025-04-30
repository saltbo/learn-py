def validIPAddresses(string):
    addresses = []
    for firstIdx in range(1, len(string)):
        part1 = string[:firstIdx]
        if not isValidIPPart(part1):
            continue
        for secondIdx in range(firstIdx+1, len(string)):
            part2 = string[firstIdx:secondIdx]
            if not isValidIPPart(part2):
                continue
            for thirdIdx in range(secondIdx+1, len(string)):
                part3 = string[secondIdx:thirdIdx]
                part4 = string[thirdIdx:]
                if isValidIPPart(part3) and isValidIPPart(part4):
                    ipParts = [part1, part2, part3, part4]
                    addresses.append(".".join(ipParts))

    return addresses


def isValidIPPart(part):
    partInt = int(part)
    if partInt > 255:
        return False

    return len(part) == len(str(partInt))


string = "1921680"
print("\n".join(validIPAddresses(string)))
