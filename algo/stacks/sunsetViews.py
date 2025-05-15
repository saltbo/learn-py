# def sunsetViews(buildings, direction):
#     start, end, step = 0, len(buildings), 1
#     if direction == "EAST":
#         start, end, step = end-1, start-1, -step

#     candidateBuildings = []
#     currentTallestHeight = 0
#     for idx in range(start, end, step):
#         if buildings[idx] > currentTallestHeight:
#             candidateBuildings.append(idx)
#             currentTallestHeight = buildings[idx]

#     return candidateBuildings if direction == "WEST" else candidateBuildings[::-1]

def sunsetViews(buildings, direction):
    start, end, step = 0, len(buildings), 1
    if direction == "WEST":
        start, end, step = end-1, start-1, -step

    candidateBuildings = []
    for idx in range(start, end, step):
        buildingHeight = buildings[idx]
        while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <= buildingHeight:
            candidateBuildings.pop()

        candidateBuildings.append(idx)

    return candidateBuildings if direction == "EAST" else candidateBuildings[::-1]


buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"
print(sunsetViews(buildings, direction))
