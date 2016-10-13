#!/bin/python
# Ben Payne
import random
import math

def distance_between_points(a,b):
    return math.sqrt( (a[1]-b[1])**2 + (a[0]-b[0])**2 )

def place_destinations(rectangle_length,rectangle_width,number_of_destinations):
    list_of_destinations=[]
    for indx in range(number_of_destinations):
        this_point=[]
        this_point.append(int(random.random()*rectangle_length))
        this_point.append(int(random.random()*rectangle_width))
        list_of_destinations.append(this_point)
    return list_of_destinations

rectangle_length=100
rectangle_width=100
number_of_destinations=100
number_of_iterations=1000

source=[int(random.random()*100),int(random.random()*100)]
list_of_destinations = place_destinations(rectangle_length,rectangle_width,number_of_destinations)

# print(list_of_destinations)

# naive method 1: from source directly to each destination
'''
sum_of_iterations=0
for this_iteration in range(number_of_iterations):
    source=[int(random.random()*100),int(random.random()*100)]
    list_of_destinations = place_destinations(rectangle_length,rectangle_width,number_of_destinations)

    sum_of_distances=0
    for indx in range(number_of_destinations):
        sum_of_distances = sum_of_distances+distance_between_points(source,list_of_destinations[indx])

    sum_of_iterations=sum_of_iterations+sum_of_distances
#    print(sum_of_distances)

print("average over "+str(number_of_iterations)+" iterations: "+str(sum_of_iterations/number_of_iterations))
''' 


