import pickle

with open('exercise-1_4/vehicle_write.bin', 'rb') as my_file:
    vehicle = pickle.load(my_file)

print("Vehicle details - ")
print("Name:  " + vehicle['brand'] + " " + vehicle['model'])
print("Year:  " + str(vehicle['year']))
print("Color: " + vehicle['color'])