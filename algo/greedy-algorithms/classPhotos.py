def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    redTallCount = 0
    blueTallCount = 0
    for idx, blueHeight in enumerate(blueShirtHeights):
        if blueHeight > redShirtHeights[idx]:
            blueTallCount += 1
        elif blueHeight < redShirtHeights[idx]:
            redTallCount += 1

    return blueTallCount == len(blueShirtHeights) or redTallCount == len(blueShirtHeights)


def classPhotos2(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    redAtFront = True if redShirtHeights[0] < blueShirtHeights[0] else False
    for idx, height in enumerate(redShirtHeights):
        if redAtFront:
            if height >= blueShirtHeights[idx]:
                return False
        else:
            if height <= blueShirtHeights[idx]:
                return False

    return True


redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

print(classPhotos(redShirtHeights, blueShirtHeights))
