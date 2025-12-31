def find_station(stations, name):

    for i in range(len(stations)):
        if stations[i] == name:
            return i
    return None
    
def count_stops(stations, start, stop):
    start_count = find_station(stations, start)
    stop_count = find_stations(stations, stop)
    count = 0




