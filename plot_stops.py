

def read_stops(filepath):
    file = open(filepath, "r")

    for line in file:
        #arr = line
        stop = line.split(",")
        print("Stop id: " + stop[0])
        print("Stop name: " + stop[2])
        print("Latitude: " + stop[4])
        print("Longitude: " + stop[5])
        print()

    file.close()

read_stops("static/stops.txt")
