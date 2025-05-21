def validStartingCity(distances, fuel, mpg):
    totalDistance = sum(distances)
    totalFuel = sum(fuel)
    if totalDistance > totalFuel*mpg:
        return -1

    totalFuelRemaining = 0
    minimumFuelRemaining = 0
    validStartingCityIdx = 0
    for idx, distance in enumerate(distances):
        if totalFuelRemaining < minimumFuelRemaining:
            minimumFuelRemaining = totalFuelRemaining
            validStartingCityIdx = idx

        fuelRemaining = round(fuel[idx] - distance/mpg, 2)
        totalFuelRemaining += fuelRemaining
        print(totalFuelRemaining, fuelRemaining)

    return validStartingCityIdx


# distances = [5, 25, 15, 10, 15]
# fuel = [1, 2, 1, 0, 3]
# mpg = 10
distances = [30, 40, 10, 10, 17, 13, 50, 30, 10, 40]
fuel = [1, 2, 0, 1, 1, 0, 3, 1, 0, 1]
mpg = 25
print(validStartingCity(distances, fuel, mpg))
