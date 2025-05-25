# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    oneDepth = getDepth(topAncestor, descendantOne)
    twoDepth = getDepth(topAncestor, descendantTwo)
    print(oneDepth, twoDepth)

    if oneDepth > twoDepth:
        return findYCA(descendantOne, descendantTwo, oneDepth-twoDepth)
    else:
        return findYCA(descendantTwo, descendantOne, twoDepth - oneDepth)


def findYCA(deeperOne, shalloerOne, diff):
    while diff > 0:
        deeperOne = deeperOne.ancestor
        diff -= 1

    while deeperOne != shalloerOne:
        deeperOne = deeperOne.ancestor
        shalloerOne = shalloerOne.ancestor

    return deeperOne


def getDepth(topAncestor, descendant):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor

    return depth
