destinations = {"Naples", "Rome", "Venice"}
destination = input("Where would you like to go? ")

if destination in destinations:
    print(f"Enjoy your stay in {destination}!")
else:
    print("Oops, that destination is not currently available.")