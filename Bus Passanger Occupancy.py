capacity = int(input("Bus capacity: "))
stops = int(input("Number of stops: "))
passengers = 0

for i in range(1, stops + 1):
    down = int(input("Passengers getting down: "))
    up = int(input("Passengers boarding: "))

    passengers = passengers - down + up

    print("Passengers after stop", i, "=", passengers)

    if passengers > capacity:
        print("Capacity exceeded")