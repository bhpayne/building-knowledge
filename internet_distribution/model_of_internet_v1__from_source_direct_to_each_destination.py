#!/bin/python
# Ben Payne
import random
import math

def distance_between_points(a,b):
    return math.sqrt( (a[1]-b[1])**2 + (a[0]-b[0])**2 )

list_of_destinations=[]
# rectangle of size 100x100
source=[int(random.random()*100),int(random.random()*100)]
number_of_destinations=100

for indx in range(number_of_destinations):
    this_point=[]
    this_point.append(int(random.random()*100))
    this_point.append(int(random.random()*100))
    list_of_destinations.append(this_point)

# print(list_of_destinations)

sum_of_distances=0
for indx in range(number_of_destinations):
    sum_of_distances = sum_of_distances+distance_between_points(source,list_of_destinations[indx])

print(sum_of_distances)
