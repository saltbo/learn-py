def generateDocument(characters, document):
    map = {}
    for c in characters:
        map[c] = map.get(c, 0) + 1

    for s in document:
        if s in map and map[s] > 0:
            map[s] -= 1
        else:
            return False

    return True

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
print(generateDocument(characters, document))