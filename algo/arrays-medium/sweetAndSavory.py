def sweetAndSavory(dishes, target):
    dishes.sort()
    sweetDishes = [dish for dish in dishes if dish < 0]
    savoryDishes = [dish for dish in dishes if dish > 0]

    bestLevel = float("Inf")
    bestPair = [0, 0]
    sweetIdx, savoryIdx = len(sweetDishes)-1, 0
    while sweetIdx >= 0 and savoryIdx < len(savoryDishes):
        sweetLevel, savoryLevel = sweetDishes[sweetIdx], savoryDishes[savoryIdx]
        current = sweetLevel + savoryLevel
        if current > target:
            # too savory, should add sweet
            sweetIdx -= 1
        else:
            # tracking the idxes
            diff = target - current
            if diff < bestLevel:
                bestLevel = diff
                bestPair = [sweetDishes[sweetIdx], savoryDishes[savoryIdx]]
            savoryIdx += 1

    return bestPair


dishes = [-3, 7]
# dishes = [-3, -5, 1, 7]
target = 8
print(sweetAndSavory(dishes, target))
