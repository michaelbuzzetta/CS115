def shortestPath(cities, distance):
    if len(cities)==1:
        return 0
    else:
        return min(
            map(lambda nxtCity:
                       distance[(cities[0], cities[nxtCity])]
                       + shortestPach(cities[nxtCity:], distance),
                       range(1,len(cities))
                       ))
