
cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven,"empty cars"
print "We can transport", carpool_capacity,"people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"

#study drills

# response: You get the 'car_pool_capacity" is not defined because the car_poopl_capacity variable is not defined/initiated beforehand

#1. You could just use 4 in python 3 because previous versions of python did not divide integer by integer and give a floating point point value

#2.