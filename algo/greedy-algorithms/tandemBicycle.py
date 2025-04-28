def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)

    speed = 0
    for idx in range(len(redShirtSpeeds)):
        if (fastest):
            speed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
        else:
            speed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])

    return speed


redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True
print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))
