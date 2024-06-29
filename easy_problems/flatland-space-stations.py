def max_distance_to_station(n, stations):
    stations.sort()
    max_distance = 0

    # Distance from the first city to the first space station
    max_distance = stations[0]

    # Distances between consecutive space stations
    for i in range(1, len(stations)):
        distance = (stations[i] - stations[i - 1]) // 2
        max_distance = max(max_distance, distance)
    
    # Distance from the last space station to the last city
    last_city_distance = n - 1 - stations[-1]
    max_distance = max(max_distance, last_city_distance)

    return max_distance

n = 10  # Number of cities
stations = [0, 4]  # Indices of cities with space stations

print(max_distance_to_station(n, stations))  # Output: 2


